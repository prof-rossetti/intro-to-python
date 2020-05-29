# The `bigquery` Package

## Installation

```sh
pip install ___________
```

## Usage

```py
```

















from datetime import datetime
import os
from dotenv import load_dotenv
from google.cloud import bigquery

from app import APP_ENV

load_dotenv()

GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS") # implicit check by google.cloud (and keras)
PROJECT_NAME = os.getenv("BIGQUERY_PROJECT_NAME", default="tweet-collector-py")
DATASET_NAME = os.getenv("BIGQUERY_DATASET_NAME", default="impeachment_development") #> "_test" or "_production"
DESTRUCTIVE_MIGRATIONS = (os.getenv("DESTRUCTIVE_MIGRATIONS", default="false") == "true")
VERBOSE_QUERIES = (os.getenv("VERBOSE_QUERIES", default="false") == "true")

def generate_timestamp(): # todo: maybe a class method
    """Formats datetime for storing in BigQuery (consider moving)"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class BigQueryService():

    def __init__(self, project_name=PROJECT_NAME, dataset_name=DATASET_NAME, init_tables=False,
                        verbose=VERBOSE_QUERIES, destructive=DESTRUCTIVE_MIGRATIONS):
        self.project_name = project_name
        self.dataset_name = dataset_name
        self.dataset_address = f"{self.project_name}.{self.dataset_name}"

        self.verbose = (verbose == True)
        self.destructive = (destructive == True)

        self.client = bigquery.Client()
        self.dataset_ref = self.client.dataset(self.dataset_name) # WARNING: PendingDeprecationWarning: Client.dataset is deprecated and will be removed in a future version. Use a string like 'my_project.my_dataset' or a cloud.google.bigquery.DatasetReference object, instead.
        if init_tables == True:
            self.init_tables()

    @property
    def metadata(self):
        return {"dataset_address": self.dataset_address, "destructive": self.destructive, "verbose": self.verbose}

    @classmethod
    def cautiously_initialized(cls):
        service = BigQueryService()
        print("-------------------------")
        print("BIGQUERY CONFIG...")
        print("  DATASET ADDRESS:", service.dataset_address.upper())
        print("  DESTRUCTIVE MIGRATIONS:", service.destructive)
        print("  VERBOSE QUERIES:", service.verbose)
        print("-------------------------")
        if APP_ENV == "development":
            if input("CONTINUE? (Y/N): ").upper() != "Y":
                print("EXITING...")
                exit()
        service.init_tables()
        return service

    def init_tables(self):
        """ Creates new tables for storing follower graphs """
        self.migrate_populate_users()
        self.migrate_user_friends()
        user_friends_table_ref = self.dataset_ref.table("user_friends")
        self.user_friends_table = self.client.get_table(user_friends_table_ref) # an API call (caches results for subsequent inserts)

    def execute_query(self, sql):
        """Param: sql (str)"""
        if self.verbose:
            print(sql)
        job = self.client.query(sql)
        return job.result()

    def migrate_populate_users(self):
        """
        Resulting table has a row for each user id / screen name combo
            (multiple rows per user id if they changed their screen name)
        """
        sql = ""
        if self.destructive:
            sql += f"DROP TABLE IF EXISTS `{self.dataset_address}.users`; "
        sql += f"""
            CREATE TABLE IF NOT EXISTS `{self.dataset_address}.users` as (
                SELECT DISTINCT
                    user_id
                    ,user_screen_name as screen_name
                FROM `{self.dataset_address}.tweets`
                WHERE user_id IS NOT NULL AND user_screen_name IS NOT NULL
                ORDER BY 1
            );
        """
        results = self.execute_query(sql)
        return list(results)

    def migrate_user_friends(self):
        sql = ""
        if self.destructive:
            sql += f"DROP TABLE IF EXISTS `{self.dataset_address}.user_friends`; "
        sql += f"""
            CREATE TABLE IF NOT EXISTS `{self.dataset_address}.user_friends` (
                user_id STRING,
                screen_name STRING,
                friend_count INT64,
                friend_names ARRAY<STRING>,
                start_at TIMESTAMP,
                end_at TIMESTAMP
            );
        """
        results = self.execute_query(sql)
        return list(results)

    def fetch_remaining_users(self, min_id=None, max_id=None, limit=None):
        """Returns a list of table rows"""
        sql = f"""
            SELECT
                u.user_id
                ,u.screen_name
            FROM `{self.dataset_address}.users` u
            LEFT JOIN `{self.dataset_address}.user_friends` f ON u.user_id = f.user_id
            WHERE f.user_id IS NULL
        """
        if min_id and max_id:
            sql += f"  AND CAST(u.user_id as int64) BETWEEN {int(min_id)} AND {int(max_id)} "
        sql += f"ORDER BY u.user_id "
        if limit:
            sql += f"LIMIT {int(limit)};"
        results = self.execute_query(sql)
        return list(results)

    def append_user_friends(self, records):
        """
        Param: records (list of dictionaries)
        """
        rows_to_insert = [list(d.values()) for d in records]
        #rows_to_insert = [list(d.values()) for d in records if any(d["friend_names"])] # doesn't store failed attempts. can try those again later
        #if any(rows_to_insert):
        errors = self.client.insert_rows(self.user_friends_table, rows_to_insert)
        return errors

    def fetch_user_friends(self, min_id=None, max_id=None, limit=None):
        sql = f"""
            SELECT user_id, screen_name, friend_count, friend_names, start_at, end_at
            FROM `{self.dataset_address}.user_friends`
        """
        if min_id and max_id:
            sql += f" WHERE CAST(user_id as int64) BETWEEN {int(min_id)} AND {int(max_id)} "
        sql += f"ORDER BY user_id "
        if limit:
            sql += f"LIMIT {int(limit)};"
        #return list(self.execute_query(sql))
        return self.execute_query(sql) # return the generator so we can avoid storing the results in memory

    def fetch_user_friends_in_batches(self, limit=None):
        sql = f"""
            SELECT user_id, screen_name, friend_count, friend_names
            FROM `{self.dataset_address}.user_friends`
        """
        if limit:
            sql += f"LIMIT {int(limit)};"

        job_name = datetime.now().strftime('%Y_%m_%d_%H_%M_%S') # unique for each job
        job_config = bigquery.QueryJobConfig(
            priority=bigquery.QueryPriority.BATCH,
            allow_large_results=True,
            destination=f"{self.dataset_address}.user_friends_temp_{job_name}"
        )

        job = self.client.query(sql, job_config=job_config)
        print("JOB (FETCH USER FRIENDS):", type(job), job.job_id, job.state, job.location)
        return job

    def partition_user_friends(self, n=10):
        """Params n (int) the number of partitions, each will be of equal size"""
        sql = f"""
            SELECT
                partition_id
                ,count(DISTINCT user_id) as user_count
                ,min(user_id) as min_id
                ,max(user_id) as max_id
            FROM (
            SELECT
                NTILE({int(n)}) OVER (ORDER BY CAST(user_id as int64)) as partition_id
                ,CAST(user_id as int64) as user_id
            FROM (SELECT DISTINCT user_id FROM `{self.dataset_address}.user_friends`)
            ) user_partitions
            GROUP BY partition_id
        """
        results = self.execute_query(sql)
        return list(results)



if __name__ == "__main__":

    service = BigQueryService()
    print("BIGQUERY DATASET:", service.dataset_address.upper())
    print("DESTRUCTIVE MIGRATIONS:", service.destructive)
    print("VERBOSE QUERIES:", service.verbose)
    if APP_ENV == "development":
        print("--------------------")
        if input("CONTINUE? (Y/N): ").upper() != "Y":
            print("EXITING...")
            exit()

    #print("--------------------")
    #print("FETCHING TOPICS...")
    #sql = f"""
    #    SELECT topic, created_at
    #    FROM `{self.dataset_address}.topics`
    #    ORDER BY created_at;
    #"""
    #results = service.execute_query(sql)
    #for row in results:
    #    print(row)
    #    print("---")

    print("--------------------")
    #print("COUNTING TWEETS AND USERS...")
    sql = f"""
        SELECT
            count(distinct status_id) as tweet_count
            ,count(distinct user_id) as user_count
        FROM `{service.dataset_address}.tweets`
    """
    results = service.execute_query(sql)
    first_row = list(results)[0]
    user_count = first_row.user_count
    print(f"TWEETS: {first_row.tweet_count:,}") # formatting with comma separators for large numbers
    print(f"USERS: {user_count:,}") # formatting with comma separators for large numbers

    #print("--------------------")
    #print("FETCHING LATEST TWEETS...")
    #sql = f"""
    #    SELECT
    #        status_id, status_text, geo, created_at,
    #        user_id, user_screen_name, user_description, user_location, user_verified
    #    FROM `{service.dataset_address}.tweets`
    #    ORDER BY created_at DESC
    #    LIMIT 3
    #"""
    #results = service.execute_query(sql)
    #for row in results:
    #    print(row)
    #    print("---")

    service.init_tables()

    sql = f"""
    SELECT
        count(distinct user_id) as user_count
        ,round(avg(runtime_seconds), 2) as avg_duration
        ,round(sum(has_friends) / count(distinct user_id), 2) as pct_friendly
        ,round(avg(CASE WHEN has_friends = 1 THEN runtime_seconds END), 2) as avg_duration_friendly
        ,round(avg(CASE WHEN has_friends = 1 THEN friend_count END), 2) as avg_friends_friendly
    FROM (
        SELECT
            user_id
            ,friend_count
            ,if(friend_count > 0, 1, 0) as has_friends
            ,start_at
            ,end_at
            ,DATETIME_DIFF(CAST(end_at as DATETIME), cast(start_at as DATETIME), SECOND) as runtime_seconds
        FROM `{service.dataset_address}.user_friends`
    ) subq
    """
    results = service.execute_query(sql)
    row = list(results)[0]
    #print(dict(row))

    collected_count = row.user_count
    pct = collected_count / user_count
    print("--------------------")
    print("USERS COLLECTED:", collected_count)
    print("  PCT COLLECTED:", f"{(pct * 100):.1f}%")
    print("  AVG DURATION:", row.avg_duration)
    if collected_count > 0:
        print("--------------------")
        print(f"USERS WITH FRIENDS: {row.pct_friendly * 100}%")
        print("  AVG FRIENDS:", round(row.avg_friends_friendly))
        print("  AVG DURATION:", row.avg_duration_friendly)

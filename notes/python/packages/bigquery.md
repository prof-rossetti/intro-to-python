# The `bigquery` Package

For interfacing with Google BigQuery databases.

> Serverless, highly scalable, and cost-effective cloud data warehouse designed for business agility. - [BigQuery website](https://cloud.google.com/bigquery/)

References:

  + https://cloud.google.com/bigquery/docs/reference/standard-sql/operators
  + https://cloud.google.com/bigquery/docs/reference/standard-sql/conversion_rules
  + https://cloud.google.com/dataprep/docs/html/DATEDIF-Function_57344707
  + https://towardsdatascience.com/google-bigquery-sql-dates-and-times-cheat-sheet-805b5502c7f0
  + https://cloud.google.com/bigquery/docs/reference/standard-sql/timestamp_functions
  + https://cloud.google.com/bigquery/docs/running-queries#batch
  + https://cloud.google.com/bigquery/docs/paging-results

## Installation

```sh
pip install google-cloud-bigquery
```

## Usage

To setup this example, gain access to a Google BigQuery database, download the corresponding "google-credentials.json" file into your local repository, ignore it from version control, then set the path to that file as the `GOOGLE_APPLICATION_CREDENTIALS` environment variable. Also set the `BIGQUERY_PROJECT_NAME` and `BIGQUERY_DATASET_NAME` environment variables to reference your project.

```py
import os
from datetime import datetime

from google.cloud import bigquery
from dotenv import load_dotenv

load_dotenv()

GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS") # implicit check by google.cloud
PROJECT_NAME = os.getenv("BIGQUERY_PROJECT_NAME", default="my-project")
DATASET_NAME = os.getenv("BIGQUERY_DATASET_NAME", default="my_database")

# CONNECT TO DATABASE

client = bigquery.Client()

# CREATING TABLES

dataset_address = f"{PROJECT_NAME}.{DATASET_NAME}"
table_address = f"{dataset_address}.my_table_123"

sql = f"""
    CREATE TABLE IF NOT EXISTS `{table_address}` (
        user_id STRING,
        screen_name STRING,
        friend_count INT64,
        friend_names ARRAY<STRING>
    );
"""
client.query(sql)

# INSERTS

my_table = client.get_table(table_address) # an API call (caches results for subsequent inserts)
rows_to_insert = [
    ["id1", "screen_name1", 2, ["friend1", "friend2"]],
    ["id2", "screen_name2", 2, ["friend3", "friend4"]],
]
errors = client.insert_rows(my_table, rows_to_insert)
print(errors)

# QUERYING / FETCHING RESULTS

sql = f"SELECT * FROM `{table_address}`;"
job = client.query(sql)
results = list(job.result())
for row in results:
    print(row)
    print("---")

# QUERYING / FETCHING RESULTS IN BATCHES

sql = f"SELECT * FROM `{table_address}`"

job_name = datetime.now().strftime('%Y_%m_%d_%H_%M_%S') # unique for each job
job_destination_address = f"{dataset_address}.job_{job_name}"
job_config = bigquery.QueryJobConfig(
    priority=bigquery.QueryPriority.BATCH,
    allow_large_results=True,
    destination=job_destination_address
)

job = client.query(sql, job_config=job_config)
print("JOB (FETCH USER FRIENDS):", type(job), job.job_id, job.state, job.location)
for row in job:
    print(row)

```

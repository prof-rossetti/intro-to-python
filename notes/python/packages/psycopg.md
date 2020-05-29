# The `psycopg2` Package


The `psycopg2` ("psycho pee gee") package provides a way for Python to interface with [PostgreSQL](https://www.postgresql.org/) databases.

> Psycopg is the most popular PostgreSQL adapter for the Python programming language. At its core it fully implements the Python DB API 2.0 specifications. Several extensions allow access to many of the features offered by PostgreSQL. - [Psycopg website](https://www.psycopg.org/)

Reference:

  + https://github.com/psycopg/psycopg2
  + https://www.psycopg.org/docs/
  + https://www.postgresql.org/docs/9.5/datatype.html
  + https://www.psycopg.org/docs/usage.html
  + https://www.psycopg.org/docs/cursor.html#cursor
  + https://www.psycopg.org/docs/cursor.html#fetch
  + https://www.psycopg.org/docs/extras.html
  + https://www.psycopg.org/docs/extras.html#dictionary-like-cursor

Run a `psycopg2` application "in development" using a database server on your local machine, and/or "in production" using a remote database server hosted by a provider like Heroku. If you run it in development, you should be able to connect via localhost, whereas if you run it in production, you should be able to connect using the production server's credentials. The professor recommends using [Table Plus](https://tableplus.com/) or some other GUI interface to your PostgreSQL databases, local or remote.

## Installation

As a prerequisite: install PostgreSQL on your local machine. If you are on a Mac, use Homebrew: `brew install postgresql` and follow the post-installation instructions. Make sure you can connect to your local PostgreSQL installation via a GUI or command-line interface. If attempting to connect from the command-line, try running `psql` or perhaps `psql -U your_username`, depending on the name of your computer's user and method of PostgreSQL installation. Note the username and password you are using to connect.

After demonstrating your ability to connect to a local PostgreSQL installation, install the Python package:

```sh
pip install psycopg2
```

## Usage

To setup this example, gain access to an existing PostgreSQL database, and observe its connection credentials.

```py
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import DictCursor, execute_values

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

# CONNECT TO THE DATABASE

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor(cursor_factory=DictCursor)
print("CURSOR:", cursor)

# CREATE A TABLE

query = """
CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    survived bool,
    full_name varchar,
    gender varchar,
    age int,
    fare float8
);
"""
cursor.execute(query)

# INSERTING RECORDS (SINGLE)

insertion_query = "INSERT INTO passengers (survived, full_name, gender, age, fare) VALUES (%s, %s, %s, %s, %s)"
record_to_insert = (False, "Passenger X", "male", 45, 100.00)
cursor.execute(insertion_query, record_to_insert)

# INSERTING RECORDS (MULTIPLE)

records_to_insert = [
  (False, "Passenger 1", "male", 45, 100.00),
  (True, "Passenger 2", "female", 42, 100.00),
  (True, "Passenger 3", "male", 10, 50.00),
  (True, "Passenger 4", "female", 8, 50.00),
]
multi_insertion_query = "INSERT INTO passengers (survived, full_name, gender, age, fare) VALUES %s"
execute_values(cursor, multi_insertion_query, records_to_insert) # third param: data as a list of tuples!

# EXECUTING QUERIES

cursor.execute("SELECT * from passengers;")
result = cursor.fetchall()
print("RESULT:", type(result))
for row in result:
    print("-----")
    print(type(row))
    print(row)

# CLEANING UP

connection.commit() # actually save the transaction (necessary only when creating tables or inserting data)
cursor.close()
connection.close()

```

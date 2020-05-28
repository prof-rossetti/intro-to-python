# The `psycopg2` Package

Reference:

  + [Package](https://pypi.python.org/pypi/psycopg2)
  + [Website](http://initd.org/psycopg/)
  + [Docs](http://initd.org/psycopg/docs/)
  + [Source Repo](https://github.com/psycopg/psycopg2)
  + [Usage Example](http://initd.org/psycopg/docs/usage.html)
  + [`connect()`](http://initd.org/psycopg/docs/module.html#psycopg2.connect)
  + [`connection`](http://initd.org/psycopg/docs/connection.html)
  + [`cursor`](http://initd.org/psycopg/docs/cursor.html)
  + [Transactions Control](http://initd.org/psycopg/docs/usage.html#transactions-control)

The `psycopg2` ("psycho pee gee") package provides a way for Python to interface with [PostgreSQL](https://www.postgresql.org/) databases.

> Psycopg is the most popular PostgreSQL adapter for the Python programming language. At its core it fully implements the Python DB API 2.0 specifications. Several extensions allow access to many of the features offered by PostgreSQL. - [Psycopg website](http://initd.org/psycopg/)

Run a `psycopg2` application "in development" using a database server on your local machine, and/or "in production" using a remote database server hosted by a provider like Heroku. If you run it in development, you should be able to connect via localhost, whereas if you run it in production, you should be able to connect using the production server's credentials. The professor recommends using [Table Plus](https://tableplus.com/) or some other GUI interface to your PostgreSQL databases, local or remote.

## Installation

As a prerequisite: install PostgreSQL on your local machine. If you are on a Mac, use Homebrew: `brew install postgresql` and follow the post-installation instructions. Make sure you can connect to your local PostgreSQL installation via a GUI or command-line interface. If attempting to connect from the command-line, try running `psql` or perhaps `psql -U your_username`, depending on the name of your computer's user and method of PostgreSQL installation. Note the username and password you are using to connect.

After demonstrating your ability to connect to a local PostgreSQL installation, install `psycopg2`, if necessary:

```sh
pip install psycopg2
```

## Usage

To setup this example, gain access to an existing PostgreSQL database, and observe its connection credentials.

```py
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
print("CURSOR:", cursor)

cursor.execute("SELECT * from my_table;")
result = cursor.fetchall()
print("RESULT:", type(result))
print(result)

for row in result:
    print("-----")
    print(type(row))
    print(row)
```

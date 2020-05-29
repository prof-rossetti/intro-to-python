# The `sqlite3` Module

For interfacing with SQLite databases.

> SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world. - [SQLite website](https://www.sqlite.org/index.html)

References:
    + https://www.sqlitetutorial.net/
    + https://docs.python.org/3/library/sqlite3.html
    + https://kite.com/python/examples/3884/sqlite3-use-a-row-factory-to-access-values-by-column-name

## Usage

To setup this example, first download the example ["Chinook" SQLite database](https://www.sqlitetutorial.net/sqlite-sample-database/) and reference the corresponding [schema diagram](https://www.sqlitetutorial.net/wp-content/uploads/2018/03/sqlite-sample-database-diagram-color.pdf).


```py
import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "chinook.db") # a path to wherever your database exists

# CONNECT TO THE DATABASE

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

# EXECUTE QUERIES

result = cursor.execute("SELECT * FROM customers;").fetchall()
print("RESULT:", type(result))
print(result)

for row in result:
    print("-----")
    print(type(row))
    print(row)
```

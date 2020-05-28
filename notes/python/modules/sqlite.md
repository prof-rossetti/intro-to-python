# The `sqlite3` Module

See documentation here: https://docs.python.org/3/library/sqlite3.html

## Usage

To setup this example, first download the example ["Chinook" SQLite database](https://www.sqlitetutorial.net/sqlite-sample-database/) and reference the corresponding [schema diagram](https://www.sqlitetutorial.net/wp-content/uploads/2018/03/sqlite-sample-database-diagram-color.pdf).


```py
import os
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "chinook.db")

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row # h/t: https://kite.com/python/examples/3884/sqlite3-use-a-row-factory-to-access-values-by-column-name
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

result = cursor.execute("SELECT * FROM customers;").fetchall()
print("RESULT:", type(result))
print(result)

for row in result:
    print("-----")
    print(type(row))
    print(row)
```

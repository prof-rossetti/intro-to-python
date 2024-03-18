# Databases and SQL Exercises

## Setup

We will be working with SQL databases, so you need a DBMS tool that allows you to interface with them. Unless you already have a preferred DBMS tool, I recommend you download and install [Table Plus](https://tableplus.com/), a free tool which will allow you to connect to all different kinds of databases.

Also [download](https://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip) this [example SQLite database](https://www.sqlitetutorial.net/sqlite-sample-database/) called "chinook.db", and put it somewhere like the Desktop. We will be working a lot with this database during class. Attached is a schema diagram, or ERD for this database.

We will hope to also introduce you to tools for working with big data, namely Google BigQuery. It will be very easy to interface with Google BigQuery from a Colab notebook, but first you'll need to perform some Google APIs setup:
  + Create a new project in [Google Cloud console](https://console.cloud.google.com/), and note its name (e.g. "my-project-123"). If you are asked for a credit card, no worries, you should have $300 of free credits and we shouldn't use much with this exercise.
  + Enable the Google BigQuery API from the [enabled APIs menu](https://console.cloud.google.com/apis), as necessary.
  + Create a new database / data set, from the [Google BigQuery console](https://console.cloud.google.com/bigquery). Call it something like "example_database".

## Concepts

Motivating the use of databases. Why not just use a CSV file?

Databases, and Datastores:
  + Relational (SQL) Databases vs "No-SQL" Datastores
  + Open Source Relational Database options: SQLite, MySQL, PostgreSQL


## Exercises and Notes

Intro to SQL for Data Analysis, using an existing database, in the [SQL Practice notebook](./../databases-sql/SQL_Practice_Chinook_DB_(Fall_2023).ipynb):
  + [Single Table Queries](https://github.com/prof-rossetti/intro-to-databases/blob/main/notes/databases/analysis/single-table-sql.md): `SELECT`, `FROM`, `WHERE` , `ORDER BY` , `LIMIT` clauses`
  + [Single Table Aggregations](https://github.com/prof-rossetti/intro-to-databases/blob/main/notes/databases/analysis/single-table-aggregations.md): `GROUP BY`, `HAVING` clauses
  + [Multi-Table Queries](https://github.com/prof-rossetti/intro-to-databases/blob/main/notes/databases/analysis/multi-table-sql.md): `JOIN` clause
    
Database Management and Collecting your own Data, in the [Database Management notebook](./../databases-sql/Database_Management_Demo_SQLite_and_BigQuery_(Fall_2023).ipynb):
  + [Management SQL](https://github.com/prof-rossetti/intro-to-databases/blob/main/notes/databases/management/management-sql.md): Creating and deleting tables. Populating tables with data.

Database Design (STRETCH GOAL):
  + [Design Concepts](https://github.com/prof-rossetti/intro-to-databases/blob/main/notes/databases/design/concepts.md)
  + [Physical Design](https://github.com/prof-rossetti/intro-to-databases/blob/main/notes/databases/design/physical-design.md)
  + [Logical Design](https://github.com/prof-rossetti/intro-to-databases/blob/main/notes/databases/design/logical-design.md)
  + [Entity Relationship Diagramming (ERDs)](https://github.com/prof-rossetti/intro-to-databases/blob/main/notes/databases/design/entity-relationship-diagramming.md)
  + [Database Relations Example (Google Sheet)](https://docs.google.com/spreadsheets/d/1xZ98yXEieMtaWuVQh3lQjCuP5aIqhinQcnzbnux52tY/edit?usp=sharing)

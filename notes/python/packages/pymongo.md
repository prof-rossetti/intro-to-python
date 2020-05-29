# The `pymongo` Package

For interfacing with MongoDB databases.

> MongoDB is a general purpose, document-based, distributed database built for modern application developers and for the cloud era. No database makes you more productive. - [MongoDB website](https://www.mongodb.com/)

Reference:

  + https://account.mongodb.com/
  + https://api.mongodb.com/python/current/tutorial.html
  + https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.insert_one
  + https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.insert_many
  + https://api.mongodb.com/python/current/tutorial.html#range-queries
  + https://docs.mongodb.com/manual/reference/operator/query/

## Installation

```sh
pip install pymongo dnspython # installing dnspython may help with some IP-address related issues
```

## Usage

To setup this example, gain access to an existing MongoDB database (for example via [MongoDB Atlas](https://account.mongodb.com/)), and observe its connection credentials.

```py
# app/mongo_queries.py

import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

# CONNECT TO THE DATABASE

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

# CREATE A COLLECTION

db = client.test_database # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.pokemon_test # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

# INSERTING RECORDS (SINGLE)

collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
})

# INSERTING RECORDS (MULTIPLE)

new_objects = [
    {"name": "Bulbasaur", "attack": 70},
    {"name": "Charmander", "attack": 100},
    {"name": "Jigglypuff", "attack": 50},
]

# QUERIES

print("DOCS:", collection.count_documents({}))

print(collection.count_documents({"name": "Pikachu"}))

# which pokemon have an attack greater than 60?
attackers = collection.find({"attack": {"$gt": 60}})
for attacker in attackers:
    print(attacker)
```

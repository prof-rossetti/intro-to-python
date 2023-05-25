# Dictionaries

Reference:

  + https://docs.python.org/3/library/stdtypes.html#dict
  + https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects
  + https://docs.python.org/3/tutorial/datastructures.html#dictionaries
  + https://docs.python.org/3/tutorial/datastructures.html#looping-techniques

Many programming languages provide an "associative array" datatype which represents an object with named attributes. Associative arrays are said to have "key/value" pairs, where the "key" represents the name of the attribute and the "value" represents the attribute's value.

Python's implementation of the associative array concept is known as a "dictionary". A Python dictionary comprises curly braces (`{}`) containing one or more key/value pairs, with each key separated from its value by a colon (`:`) and each key/value pair separated by a comma (`,`).

Example dictionaries:

```python
{}

{"a": 1, "b": 2, "c": 3}

{"a": 1, "b": 2, "c": 3, "fruits": ["apple", "banana", "pear"]} # dictionaries can contain lists, or even other nested dictionaries

{"first_name": "Ophelia", "last_name": "Clark", "message": "Hello Again"}
```

Each dictionary is similar to a row in a CSV-formatted spreadsheet or a record in a database, where the dictionary's "keys" represent the column names and its "values" represent the cell values.

city | name | league
--- | --- | ---
New York | Yankees | major
New York | Mets | major
Boston | Red Sox | major
New Haven | Ravens | minor


```python
[ # LIST OF DICTIONARIES:
    {"city": "New York", "name": "Yankees", "league":"major"}, 
    {"city": "New York", "name": "Mets", "league":"major"},
    {"city": "Boston", "name": "Red Sox", "league":"major"},
    {"city": "New Haven", "name": "Ravens", "league":"minor"}
]
```

## Operations


Accessing dictionary values by their key, or attribute name:

```python
person = {
    "first_name": "Ophelia",
    "last_name": "Clarke",
    "message": "Hi, thanks for the ice cream!",
    "fav_flavors": ["Vanilla Bean", "Mocha", "Strawberry"]
}

print(person["first_name"]) #> "Ophelia"
print(person["last_name"]) #> "Clark"
print(person["message"]) #> "Hi, thanks for the ice cream!"
print(person["fav_flavors"]) #> ["Vanilla Bean", "Mocha", "Strawberry"]
print(person["fav_flavors"][1]) #> "Mocha" (a list is still a list, even if it exists inside a dictionary!)
```

Adding, updating, or removing attributes from a dictionary:

```python
person = {
    "first_name": "Ophelia",
    "last_name": "Clarke",
    "message": "Hi, thanks for the ice cream!",
    "fav_flavors": ["Vanilla Bean", "Mocha", "Strawberry"]
}

# adding an attribute:
person["message"] = "New Message" # this is mutating

# updating an attribute:
person["fav_color"] = "blue" # this is mutating

# removing an attribute:
del person["fav_flavors"] # this is mutating

print(person) 
#> {'first_name': 'Ophelia', 'last_name': 'Clark', 'message': 'New Message', 'fav_color': 'blue' }
```

Accessing a dictionary's keys and/or values seperately, and iterating through them:

```python
person = {
    "first_name": "Ophelia",
    "last_name": "Clarke",
    "message": "Hi, thanks for the ice cream!",
    "fav_flavors": ["Vanilla Bean", "Mocha", "Strawberry"]
}

#
# KEYS:
#

print(person.keys()) #> dict_keys(['first_name', 'last_name', 'message', 'fav_flavors'])
# print(list(person.keys())) #> ['first_name', 'last_name', 'message', 'fav_flavors']

for k in person.keys():
    print("KEY:", k)
    

#
# VALUES:
#

print(person.values()) #> dict_values(['Ophelia', 'Clark', 'Hi, thanks for the ice cream!', ["Vanilla Bean", "Mocha", "Strawberry"]])
# print(list(person.values()) #> ['Ophelia', 'Clark', 'Hi, thanks for the ice cream!', ["Vanilla Bean", "Mocha", "Strawberry"]]

for v in person.values():
    print("VALUE:", v)
    
#
# KEY/VALUE PAIRS:
#

print(person.items()) #> dict_items([('first_name', 'Ophelia'), ('last_name', 'Clark'), ('message', 'Hi, thanks for the ice cream!'), ('fav_flavors', ["Vanilla Bean", "Mocha", "Strawberry"])])
# print(list(person.items())) #> [('first_name', 'Ophelia'), ('last_name', 'Clark'), ('message', 'Hi, thanks for the ice cream!'), ('fav_flavors', ["Vanilla Bean", "Mocha", "Strawberry"])]

# referencing key-value tuple separately as k and v, using a "destructuring" approach:
for k, v in person.items():
    print("KEY:", k, "... VALUE:", v)
```


> NOTE: the `dict_keys`, `dict_values`, and `dict_items` are list-like, so we can convert them to lists by passing them into the `list()` function, or do list-like things such as looping through them.















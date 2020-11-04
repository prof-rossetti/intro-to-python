# The `json` Module

Reference: https://docs.python.org/3/library/json.html.

## Usage

### Writing JSON

Use `json.dumps()` to convert a dictionary to a JSON-formatted string:

```python
import json

person = {
    "first_name": "Ophelia",
    "last_name": "Clarke",
    "message": "Hi, thanks for the ice cream!",
    "fav_flavors": ["Vanilla Bean", "Mocha", "Strawberry"]
}

raw_data = json.dumps(person)

print(type(raw_data)) #> <class 'str'>

print(raw_data) #> '{"first_name": "Ophelia", "last_name": "Clarke", "message": "Hi, thanks for the ice cream!", "fav_flavors": ["Vanilla Bean", "Mocha", "Strawberry"]}'
```

### Reading JSON

Use `json.loads()` to convert a JSON-formatted string into a Python dictionary.

```py
raw_data = '{"first_name": "Ophelia", "last_name": "Clarke", "message": "Hi, thanks for the ice cream!", "fav_flavors": ["Vanilla Bean", "Mocha", "Strawberry"]}'

person = json.loads(raw_data)

print(type(person)) #> <class 'dict'>

print(person) #> {'first_name': 'Ophelia', 'last_name': 'Clarke', 'message': 'Hi, thanks for the ice cream!', 'fav_flavors': ['Vanilla Bean', 'Mocha', 'Strawberry']}
```

### Reading and Writing JSON Files

Combine these JSON-parsing techniques with [file management](/notes/python/file-management.md) techniques to read and write JSON data from a .json file.

Writing:

```py
json_filepath = "path/to/gradebook.json" # for example (see os module notes for constructing filepaths more reliably)

with open(json_filepath, "w") as json_file:
    json.dump(data, json_file)
```

Reading:

```py
json_filepath = "path/to/gradebook.json" # for example (see os module notes for constructing filepaths more reliably)

with open(json_filepath, "r") as json_file:
    my_data = json.load(json_file)

print(my_data)
```







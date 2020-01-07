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

#### Processing JSON Files

Combine this JSON-parsing technique with [file management](/notes/python/file-management.md) techniques to read JSON data from a .json file (e.g. "path/to/gradebook.json"):

```py
gradebook_filepath = "path/to/gradebook.json"

with open(gradebook_filepath, "r") as json_file:
    file_contents = json_file.read()

gradebook = json.loads(file_contents)

print(type(gradebook)) #> <class 'dict'>

print(gradebook)
#> {
#>   "downloadDate": "2018-06-05",
#>   "professorId": 123,
#>   "students":[
#>     {"studentId": 1, "finalGrade": 76.7},
#>     {"studentId": 2, "finalGrade": 85.1},
#>     {"studentId": 3, "finalGrade": 50.3},
#>     {"studentId": 4, "finalGrade": 89.8},
#>     {"studentId": 5, "finalGrade": 97.4},
#>     {"studentId": 6, "finalGrade": 75.5},
#>     {"studentId": 7, "finalGrade": 87.2},
#>     {"studentId": 8, "finalGrade": 88.0},
#>     {"studentId": 9, "finalGrade": 93.9},
#>     {"studentId": 10, "finalGrade": 92.5}
#>   ]
#> }
```

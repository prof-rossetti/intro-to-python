# Python Datatypes Overview

Common Python datatypes include:

  + [None](none.md)
  + [Booleans](booleans.md)
  + [Strings](strings.md)
  + [Numbers](numbers.md)
  + [Dates and Times](dates.md)
  + [Lists and Sets](lists.md)
  + [Dictionaries](dictionaries.md)

## Detection

Use the `type()` function to detect the datatype of any object:

```python
type("Hello") #> <type 'str'>
type("100") #> <type 'str'>
type(100) #> <type 'int'>
type(0.45) #> <type 'float'>
type(True) #> <type 'bool'>
type(False) #> <type 'bool'>
type(None) #> <type 'NoneType'>
type({"a":1, "b":2, "c":3}) #> <type 'dict'>
type([1,2,3]) #> <type 'list'>
```

Alternatively call `.__class__.__name__` on any object to detect its class name:

```py
"Hello".__class__.__name__ #> 'str'

{"a": 1, "b": 2, "c": 3}.__class__.__name__ #> 'dict'

[1, 2, 3].__class__.__name__ #> 'list'
```

Use the `isinstance` function when comparing datatypes:

```py
isinstance("Hello", str) #> True
isinstance([1,2,3], list) #> True
isinstance([1,2,3], str) #> False
```

## Conversion

Here are a few examples of how to convert between datatypes:

```python
# converting to numbers:

int("500") #> 500

float("0.45") #> 0.45

# converting to strings:

str(100) #> "100"

str(0.45) #> "0.45"

# converting to lists:

list("Hello World") #> ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

list({"color": "blue", "size": "small"}) #> ['color', 'size']
```

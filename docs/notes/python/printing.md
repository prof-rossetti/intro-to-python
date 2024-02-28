# Printing and Logging

Reference: https://docs.python.org/3/library/functions.html#print

In Python, we use the `print()` statement to output information onto the command-line. This is helpful for providing user feedback, as well as for debugging purposes.

```python
print("HELLO WORLD") #> HELLO WORLD
```

It is possible to print multiple objects, including different kinds of objects, by separating each with a comma:

```python
print("HELLO", "WORLD") #> HELLO WORLD
print("HELLO", "WORLD", 5, {'a': 1, 'c': 3, 'b': 2}) #> HELLO WORLD 5 {'a': 1, 'c': 3, 'b': 2}
```

See also: pretty printing with [the `pprint` module](/notes/python/modules/pprint.md).

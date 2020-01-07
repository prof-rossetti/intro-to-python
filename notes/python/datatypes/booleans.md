# Booleans

## Values

Reference: https://docs.python.org/3/library/stdtypes.html#boolean-values.

In Python, `True` and `False` are reserved words which indicate boolean values.

```python
True #> True
False #> False
```

## Operations

Reference:

  + https://docs.python.org/3/library/stdtypes.html#truth-value-testing
  + https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
  + https://docs.python.org/3/library/stdtypes.html#comparisons

It is common to evaluate the combination of multiple boolean conditions. The keywords `and` and `or` are reserved for this purpose. The `and` operator will return `True` only if all values are `True`, whereas the `or` operator will return `True` if any of the values are `True`:

```python
True and True #> True
True and False #> False
False and True #> False
False and False #> False

True or True #> True
True or False #> True
False or True #> True
False or False #> False
```

The most relevant boolean operator is the equality operator, `==`. Its functionality is represented by the phrase, "Is this equal to that?":

```python
True == True #> True
True == False #> False
False == False #> True
```

The inverse is the inequality operator, `!=`. Its functionality is represented by the phrase, "Is this not equal to that?":

```python
True != True #> False
True != False #> True
False != False #> False
```

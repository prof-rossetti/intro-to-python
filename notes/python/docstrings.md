# Docstrings

Reference:

  + https://www.python.org/dev/peps/pep-0257/
  + https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format
  + https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

Example (Pandas):

  + https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
  + https://github.com/pandas-dev/pandas/blob/master/pandas/core/frame.py#L319

## About

Docstrings allow Python developers to document their code in a way which can be interpreted by other computers and humans alike.

> "The docstring for a function or method should summarize its behavior and document its arguments, return value(s), side effects, exceptions raised, and restrictions on when it can be called (all if applicable). Optional arguments should be indicated. It should be documented whether keyword arguments are part of the interface." - [PEP 257](https://www.python.org/dev/peps/pep-0257/)

## Examples

Before documentation:

```py
def enlarge(n):
    return n * 100

```

Complete, with documentation:

```py
def enlarge(n):
    """
    Enlarges a number.

    Params:
        n (numeric, like int or float) the number to be enlarged

    Examples:
        enlarge(8)
        enlarge(4.5)
    """
    return n * 100
```

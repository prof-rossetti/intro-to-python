


# The `types` Module

## The `SimpleNamespace` Class

We can use the `SimpleNamespace` class to construct custom objects from named attributes, without defining a new class with those attributes.

This allows us to use dot notation to access attributes.

```py
from types import SimpleNamespace

obj = SimpleNamespace(year=2100, color="blue")

print(obj.year) #> 2100
print(obj.color) #> 'blue'
```

We can use the "splat" operator to create a new object from a dictionary of attributes:

```py
from types import SimpleNamespace

attrs = {'year': 2100, 'color': 'blue'}

obj = SimpleNamespace(**attrs)

print(obj.year) #> 2100
print(obj.color) #> 'blue'
```

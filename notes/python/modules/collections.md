# The `collections` Module

Reference: https://docs.python.org/3/library/collections.html

## Ordered Dictionary

Reference: https://docs.python.org/dev/library/collections.html#collections.OrderedDict

The `collection` module's `OrderedDict` datatype allows us to convert normal dictionaries to special dictionaries which respect the order of their keys. This datatype may prove useful for processing and transforming data.

## Counter

Reference: https://docs.python.org/3/library/collections.html#collections.Counter

The `collection` module's `Counter` datatype allows us to count items in a list, in a computationally efficient way:

```py
from collections import Counter

flavors = ["vanilla bean", "choc", "choc", "choc", "strawberry"]

# initialize the counter object, passing the list:
c = Counter(flavors)

# ask how many times a given item appears in the list:
print(c["vanilla bean"]) #> 1
print(c["choc"]) #> 3
print(c["oops"]) #> 0
```

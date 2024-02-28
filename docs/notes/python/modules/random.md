# The `random` Module

Reference: https://docs.python.org/3/library/random.html.

```python
import random # load the module to avoid `NameError: name 'random' is not defined`

random.random() #> 0.6357193086559119
random.random() #> 0.9374153182597137
random.random() #> 0.6894107277064547

random.randint(1, 100) #> 43
random.randint(1, 100) #> 15
random.randint(1, 100) #> 95
```

Once you have learned about lists, you can perform randomness-related operations on them:

```python
arr = [1,2,3,4,5,6,7,8,9]

random.shuffle(arr) # FYI, this is a mutating operation
arr #> [9, 2, 3, 8, 6, 4, 1, 7, 5]

random.choice(arr) #> 5
random.choice(arr) #> 7
random.choice(arr) #> 6

random.sample(arr, 5) #> [9, 5, 3, 8, 6]
```

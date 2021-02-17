# Errors

Reference:

  + https://docs.python.org/3/library/exceptions.html#bltin-exceptions
  + https://docs.python.org/3/tutorial/errors.html

## Handling Errors

We can use a `try... except` block to handle errors:

```python
try:
  empty_list = []
  matching_item = empty_list[0] # triggers an IndexError (list index out of range)
  print("EVERYTHING IS GOING FINE")
except IndexError:
  print("OOPS - MY ERROR")

#> OOPS - MY ERROR
```

```python
try:
  100 / 0 # triggers a DivisionByZeroError
  print("EVERYTHING IS GOING FINE")
except DivisionByZeroError:
  print("OOPS - MY ERROR")

#> OOPS - MY ERROR
```

We can also catch errors generically, and learn more about the one that got caught:

```py
try:
    do_something()
except Exception as err:
    print("OOPS")
    print(type(err)) #> this will tell you the error class
    print(err)
```

## Raising Errors

We can use the `raise` keyword to stop program execution if a certain condition is met.

```python
options = ["rock", "paper", "scissors"]

choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

if choice in options:
    print("YOU CHOSE", choice)
else:
    raise ValueError("OOPS - Please type 'rock', or 'paper', or 'scissors'.")
```

### Defining and Raising Custom Errors

We can define our own errors if that's helpful, by inheriting a class from the base `Exception` class (or preferably a more specific one):
```py
class MyCustomError(Exception):
   pass

raise MyCustomError("My custom message")
```

# Errors

Reference:

  + https://docs.python.org/3/library/exceptions.html#bltin-exceptions
  + https://docs.python.org/3/tutorial/errors.html

## Handling Errors

Sometimes our programs will encounter errors. In Python, we can use a `try... except` block to handle these errors.

After running into an error for the first time, we should observe what type of error we are experiencing (e.g. `KeyError`, `IndexError`, `DivisionByZeroError`, etc.).

Once we know what type of error we need to handle, we should wrap the problematic code inside the `try` clause, and specify the known error type in the `except` clause:

```python
try:
  empty_list = []
  matching_item = empty_list[0] # triggers an IndexError (list index out of range)
  print("EVERYTHING IS GOING FINE") # this never gets reached
except IndexError:
  print("OOPS - MY ERROR")

#> OOPS - MY ERROR
```

```python
try:
  100 / 0 # triggers a DivisionByZeroError
  print("EVERYTHING IS GOING FINE") # this never gets reached
except DivisionByZeroError:
  print("OOPS - MY ERROR")

#> OOPS - MY ERROR
```

If we're not yet sure what type of error we're experiencing, we can temporarily catch all error classes that inherit from the base error class (`Exception`), and once caught, we print the specific error's datatype to learn how to handle it:

```python
try:
    do_something() # some hypothetical problematic code
except Exception as err:
    print(type(err)) #> this will tell you the error type
    print(err) #> the error message
```





## Raising Errors

If we find the need to trigger our own errors to stop program execution (less common), we can use the `raise` keyword followed by the type of error (e.g. `ValueError`):

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

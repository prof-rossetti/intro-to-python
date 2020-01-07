# Control Flow

## Reference

  + https://docs.python.org/3/tutorial/controlflow.html#if-statements
  + https://docs.python.org/3/tutorial/controlflow.html#for-statements
  + https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
  + https://docs.python.org/3/tutorial/controlflow.html#pass-statements

## If Statements

Reference:

  + https://docs.python.org/3/tutorial/controlflow.html#if-statements

Use "If" statements to handle conditional logic (i.e. checking whether or not something is true and responding accordingly).

In Python, an "If" statement is defined using the `if` keyword, followed by a condition to be evaluated, followed by a colon (`:`), followed by one or more indented lines which contain statement(s) to be executed if the condition is met.

```python
if True:
    print("YES THIS IS TRUE")

#> YES THIS IS TRUE

if 1 == 1:
    print("YES THIS IS TRUE")

#> YES THIS IS TRUE

if False:
    print("YES THIS IS TRUE")

if 1 == 2:
    print("YES THIS IS TRUE")
```

An "If" statement may include an `else` keyword, followed by a colon (`:`), followed by one or more indented lines which contain statement(s) to be executed if the original condition is not met.

```python
if 1 == 2:
    print("YES THIS IS TRUE")
else:
    print("NO THIS IS FALSE")

#> NO THIS IS FALSE
```

An "If" statement, regardless of whether or not it contains an `else` keyword, can contain any number of `elif` keywords, each followed by a colon (`:`), followed by one or more indented lines which contain statement(s) to be executed if the condition is met. If there is an `else` keyword, it should come last.

```python
# run this script a few times in a row...
import random

fruit = random.choice(["Apple", "Banana", "Orange"])

if fruit == "Orange":
    print("WE GOT AN ORANGE HERE")
elif fruit == "Banana":
    print("WE GOT A BANANA HERE")
elif fruit == "Peach":
    print("WE GOT A PEACH HERE")
else:
    print("NOT SURE WHAT WE GOT HERE")
```

As in other languages, statement order matters:

```python
if True:
    print("First")
elif True:
    print("Second")

#> "First"
```

## Case Statements

Python doesn't have "Case" statements. Try to use an "If" statement or a dictionary to accomplish what you are trying to do.

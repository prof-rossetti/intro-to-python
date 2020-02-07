# Syntax and Style

Reference: https://www.python.org/dev/peps/pep-0008/ for official style guidance.

## Indentation

Python enforces a line indentation style which distinguishes it from other languages. The indentation-level of a given line of Python code is very important. Always start at the left-margin, and if you need to indent a new line of code, do so using four spaces:


    some line of code:
        an indented line of code
        another line of code at the first indentation level:
            a line of code at a nested indentation level
            this is starting to look like a snake maybe?
            hence the name "Python"


Unlike other languages, when you start a statement in Python, you don't need to also specify an explicit "end" of that statement. In other words, it is not necessary to close the statement at the same indentation-level from which it began.

## Naming

Always observe lower-case variable and function names. If your variable or function name is comprised of two words, use snake case, not camel-case. As usual, only use title case for class names. Use snake case for Python (`.py`) files as well.

DO:

  + `name`
  + `first_name`
  + `last_name`
  + `first_and_last_name`
  + `Human` - use title case for classes only
  + `SuperHuman` - use title case for classes only

DON'T:

  + `firstName`
  + `lastName`
  + `firstAndLastName`

> PROFESSOR'S SIDE-NOTE: When in doubt, use lowercase snake case like `my_var = ...` or `def my_func(): ...` . You'll see me sometimes use all caps variable names like `CSV_FILEPATH = ...` which I think is the cause of some confusion. In other languages, a variable name in all caps like this is a "constant", or a variable whose value can't be changed. Although this behavior does not apply to Python, I have carried over this convention into my Python out of habit, perhaps providing you with a poor example. I also generally do this when I'm converting environment variables into Python variables, for consistency there. But this isn't a rule and I encourage each of you to adopt a pattern that makes sense to you!

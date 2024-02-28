# Functions

Reference:

  + https://docs.python.org/3/tutorial/controlflow.html#defining-functions
  + https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
  + https://docs.python.org/3/tutorial/controlflow.html#default-argument-values
  + https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments

The primary responsibilities of a function are to perform some specified set of logical operations (i.e. "do something"), and optionally also to return a value (i.e. "return something").

In practice, we will move some expression into its own function if we need to re-use it over and over again. Then instead of repeating the entire expression again, we can easily invoke our function as a short-hand way of referencing the pre-defined functionality. This helps us keep our code maintainable. See also: [Refactoring](/notes/software/refactoring).

Functions must first be defined (just once), then they can subsequently be used (i.e. "called" or "invoked") any number of times. Remember to use trailing parenthesis when defining and invoking functions.

```python

# FUNCTION DEFINITION

def do_stuff(): 
    print("DOING STUFF HERE!")


# FUNCTION INVOCATIONS

do_stuff() 
#> "DOING STUFF HERE!"

do_stuff() 
#> "DOING STUFF HERE!"

do_stuff() 
#> "DOING STUFF HERE!"
```

## Parameters (Input Values)

A function may accept input arguments called parameters which are essentially variable references for whatever values are passed in.

### Single Parameter

```python

# FUNCTION DEFINITION

def display_heading(message):
    print("------------------")
    print(message.upper())
    print("------------------")


# FUNCTION INVOCATIONS

display_heading("hello")
#> ------------------
#> HELLO
#> ------------------

display_heading("hello again")
#> ------------------
#> HELLO AGAIN
#> ------------------

m = "hello world" 
display_heading(m)
#> ------------------
#> HELLO WORLD
#> ------------------

```

### Multiple Parameters

For a function that accepts multiple parameters, order matters. By default, the function assumes we are passing the parameters in the same order as specified during the function definition. However it is also possible to pass the parameters in a different order, by explicitly specifying the parameter name during function invocation.


```python
# FUNCTION DEFINITION

def display_height(feet, inches):
  print("THE HEIGHT IS: ", feet, "FEET AND", inches, "INCHES")


# FUNCTION INVOCATIONS

display_height(6, 3)
#> THE HEIGHT IS 6 FEET AND 3 INCHES 

display_height(feet=6, inches=3)
#> THE HEIGHT IS 6 FEET AND 3 INCHES 

display_height(inches=3, feet=6)
#> THE HEIGHT IS 6 FEET AND 3 INCHES 
```

### Default Parameters

It is possible to specify default parameter values that should be used if the parameter is omitted during invocation:


```py

# FUNCTION DEFINITION

def motivate(name="everyone"):
    print("ROW FASTER,", name.upper())


# FUNCTION INVOCATIONS

motivate() 
#> ROW FASTER, EVERYONE

motivate("Mike") 
#> ROW FASTER, MIKE

```

When we define a function that has default parameters, if it also has required parameters, the required parameters are listed first, and the default parameters are listed afterwards:


```py

# FUNCTION DEFINITION

def format_temp(temp, temp_unit="F"):
    DEGREE_SIGN = u"\N{DEGREE SIGN}"
    print(f"{round(temp)} {DEGREE_SIGN}{temp_unit}")


# FUNCTION INVOCATIONS

format_temp(90.3) 
#> 90 °F

format_temp(90.3, "C") 
#> 90 °C
```




## Return Values

A function can pass back a value to its caller by using the `return` keyword, which helps us store the results in a variable for later. 

```python

# FUNCTION DEFINITION

def enlarge(n):
    return n * 100


# FUNCTION INVOCATIONS

print(enlarge(3))
#> 300

result = enlarge(5)
print(result)
#> 500

my_number = 7
bigger_number = enlarge(my_number)
print(bigger_number)
#> 700
```



## Function Documentation

When defining our own functions, we'll want to include some documentation / helpful notes to help other people understand what the function is about, and how to invoke it. 

See the notes on [Docstrings](/notes/python/docstrings.md) for more info.




# "Modules and Imports" Exercise

## Setup

Create a new directory on your computer called "modules-overview" and create two new files inside - one called "my_script.py" (i.e. the script) and the other called "my_mod.py" (i.e. the module).

Place inside the following contents:

``` python
# this is the "modules-overview/my_script.py" file...

# IMPORT STRATEGY A) import the entire module and all it's functions
import my_module

# IMPORT STRATEGY B) only import a certain function
from my_module import my_message, other_message

print("INVOKING MY SCRIPT...")

# INVOCATION STRATEGY A) prefix with the module name
my_module.my_message()
my_module.other_message()

# INVOCATION STRATEGY B) no module prefix
my_message()
other_message()
```

Most of the code in a Python module file should be nested inside functions or the "main" conditional:

``` python
# this is the "modules-overview/my_module.py" file...

def my_message():
    print("HELLO FROM A MODULE")

def other_message():
    print("GREETINGS EARTHLING")


if __name__ == "__main__":

    print("INVOKING MY MODULE AS A SCRIPT...")

    my_message()

    other_message()
```

## Usage

Then execute the script to prove it has access to code in the module:

```sh
python my_script.py
```

And execute the module file directly, to show that is possible as well:

```sh
python my_module.py
```

You'll notice only the module code nested inside the "main" conditional gets executed when we run the module file from the command-line

## Further Exploration

If you're interested, also learn about how to import modules from a [subdirectory structure](subdirectory-imports.md).
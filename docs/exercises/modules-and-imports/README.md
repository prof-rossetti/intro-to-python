


# "Modules and Imports" Exercise

## Part I - Files in Same Directory

Create a new directory on your computer called "modules-overview" and create two new files inside - one called "my_script.py" (i.e. the script) and the other called "my_mod.py" (i.e. the module).

Place inside the following contents:

``` python
# this is the "modules-overview/my_script.py" file...

# IMPORT STRATEGY A) import the entire module and all it's functions
import my_mod

# IMPORT STRATEGY B) only import a certain function
from my_mod import my_message, other_message

print("RUNNING MY SCRIPT...")

# INVOCATION STRATEGY A) prefix with the module name
my_mod.my_message()
my_mod.other_message()

# INVOCATION STRATEGY B) no module prefix
my_message()
other_message()
```

``` python
# this is the "modules-overview/my_mod.py" file...

def my_message():
    print("HELLO WORLD")

def other_message():
    print("GREETINGS EARTHLING")


if __name__ == "__main__":

    print("RUNNING MY MODULE AS A SCRIPT...")

    my_message()

    other_message()
```

Most of the code in a Python "module" file should be nested inside functions or the "main" conditional.


Execute the script to prove it has access to code in the module:

```sh
python my_script.py
```

And execute the module file directly, to show that is possible as well:

```sh
python my_mod.py
```

You'll notice only the module code nested inside the "main" conditional gets executed when we run the module file from the command-line.

## Part II - Files in Subdirectories

Now make a subdirectory of the "modules-overview" directory called "things" and place inside a file called "robot.py", with the following contents:

``` python
# this is the "modules-overview/things/robot.py" file...

def robot_message():
    print("HELLO I'M A ROBOT")
```

If a Python module is located in a subdirectory like this, we can reference it using dot notation, like `[directory_name].[file_name]`. For example, add the following contents to the "my_script.py" file:

``` python
# this is the "modules-overview/my_script.py" file...

# ...

from things.robot import robot_message

robot_message()
```

Finally, run the script again to see the new imports working:

```sh
python my_script.py
```

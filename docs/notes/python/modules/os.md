# The `os` Module

Reference: https://docs.python.org/3/library/os.html.

Use the `os` module perform command-line-style file and directory operations, and to access system environment variables.

> NOTE: On Windows, the filepaths may need different slashes (i.e. `\`  vs. `/`). To mitigate this difference, we'll ideally follow the techniques suggested in the "Constructing Filepaths" section, to make filepaths that will work on any operating system.

## Directory Operations

Detect the path of the current working directory (in scripts, this reflects the dir from which the command is being run):

```python
os.getcwd() #> '/Users/mjr/Desktop/my-dir'
```

In scripts, detect the path of the directory where the script file exists:

```py
os.path.dirname(__file__)
```

Change directory:

```py
os.chdir("/path/to/Desktop")
```

Make a new directory:

```py
os.mkdir("/path/to/Desktop/my-dir")

# make all parent directories as well, if necessary:
os.makedirs("/path/to/Desktop/my-dir", exist_ok=True)
```

List all files in a given directory:

```python
os.listdir("/path/to/Desktop")
```

## File Operations

Delete a file:

```py
os.remove("demofile.txt")
```

Detect whether a specific file exists:

```py
os.path.isfile("/path/to/Desktop/some_file.txt") #> returns True or False
```

### Constructing Filepaths

Since different operating systems use different slashes, we must standardize filepaths across operating systems. To do this, we use `os.path.join` in conjunction with commas, to apply the proper slashes depending on the user's operating system.

Since certain filepaths will break if we run the same script from different locations on the command line, we also must ensure our filepaths work no matter which directory we are running the script from. So we use `os.path.dirname(__file__)` to reference the location of the current Python script, and start to form a relative reference from there.

```py
# BAD:
"my_receipt.txt"
"../data/monthly_sales.csv"

# GOOD:
os.path.join(os.path.dirname(__file__), "my_receipt.txt")
os.path.join(os.path.dirname(__file__), "..", "data", "monthly_sales.csv")
```

More filepath construction examples:

```py
#
# Assumes the following files and directories exist on your computer (might want to set these up to follow along yourself):
#
#   /Users/mjr/Desktop/desktop_message.txt
#   /Users/mjr/Desktop/my-dir
#   /Users/mjr/Desktop/my-dir/paths.py (this file)
#   /Users/mjr/Desktop/my-dir/my_message.txt
#   /Users/mjr/Desktop/my-dir/subdir/
#   /Users/mjr/Desktop/my-dir/subdir/other_message.txt
#

import os

# what's the name of this file?
print(__file__)
#> /Users/mjr/Desktop/my-dir/paths.py

# what directory is this file in?
print(os.path.dirname(__file__))
#> /Users/mjr/Desktop/my-dir

# examples of constructing paths to the various files...

print(os.path.join(os.path.dirname(__file__), "my_message.txt"))
#> /Users/mjr/Desktop/my-dir/my_message.txt

print(os.path.join(os.path.dirname(__file__), "subdir"))
#> /Users/mjr/Desktop/my-dir/subdir

print(os.path.join(os.path.dirname(__file__), "subdir", "other_message.txt"))
#> /Users/mjr/Desktop/my-dir/subdir/other_message.txt

print(os.path.join(os.path.dirname(__file__), "..", "desktop_message.txt"))
#> /Users/mjr/Desktop/my-dir/../desktop_message.txt

print(os.path.isfile(os.path.join(os.path.dirname(__file__), "..", "desktop_message.txt")))
#> True
```

## Environment Variables

> Prerequisite: [Environment Variables](/notes/environment-variables/README.md)

It is possible to access all variables in the entire environment:

```py
import os

my_env = os.environ

print("------------")
print(type(my_env)) #> <class 'os._Environ'>
print(my_env)

# can be converted to a dictionary:
print("------------")
print(type(dict(my_env))) #> <class 'dict'>
```

But most commonly, we'll access a specific environment variable by its name (e.g. `MY_SECRET_MESSAGE`). There are a few ways to do this, but we'll prefer the latest `os.getenv` approach:

```py
import os

# OPTION A (OLD) ... using a dictionary-like approach:
my_var = os.environ["MY_SECRET_MESSAGE"]
print(my_var) #> SecretPassword123

# OPTION B (OLD) ... using a getter function:
my_var = os.environ.get("MY_SECRET_MESSAGE")
print(my_var) #> SecretPassword123

# OPTION C (RECOMMENDED) ... using the newer, more high-level getter function:
my_var = os.getenv("MY_SECRET_MESSAGE")
print(my_var) #> SecretPassword123
```

Using the recommended `os.getenv` approach, it is also possible to specify a default fall-back value to use if the environment variable has not been set:

```py
import os

my_var = os.getenv("MY_SECRET_MESSAGE", default="This is a default / fallback message.")
print(my_var) #> SecretPassword123
```

You can see we have stored the environment variable's value in a Python variable (i.e. `my_var`) for future use, and the Python variable could be named anything. However, as a best practice, to help you stay organized, the professor recommends using Python variable names that match the environment variable name (i.e. `MY_SECRET_MESSAGE`):


```py
import os

MY_SECRET_MESSAGE = os.getenv("MY_SECRET_MESSAGE", default="This is a default / fallback message.")
print(MY_SECRET_MESSAGE) #> SecretPassword123
```

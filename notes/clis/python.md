# The `python` Utility

> "Python is a programming language that lets you work quickly and integrate systems more effectively" - [Python Website](https://www.python.org/)

Before you can execute Python programs on your computer, you'll first need to install the Python command-line utility.

Over the past few years there has been a shift in the community from Python Version 2 to Python Version 3. This semester we will be using Python 3, exclusively. We might use different minor versions of Python 3 (like 3.6 or 3.7), depending on the third-party packages we need to use for any given project.

Anaconda provides a command-line utility called `conda` to help us manage different versions of Python. Before proceeding, please take a moment to [install Anaconda and get familiar with the `conda` utility](conda.md).

When you are ready, create and activate a new Anaconda virtual environment, and execute the following commands inside that virtual environment.

## Detecting Installations

To see if Python is already installed, and if so where:

```sh
# Mac Terminal:
which python

# Windows Command Prompt:
where python
```

If you see a filepath output, it means Python is installed at the location specified, so you can advance to the version detection instructions below. Otherwise, if you see an empty result or an error message, that usually means Python is not installed.

## Detecting Versions

Let's see which version of Python is installed:

```sh
python --version
```

## Usage

After Python is installed, you should be able to execute Python commands.

### Interactive Console

If you type `python` on the command-line and press "enter", you will enter into an interactive Python console where you can evaluate Python statements and expressions. When you are done using the Python console, you can shut it down by typing `exit()` and pressing "enter".

![a screenshot of using the python console to perform a simple calculation (2+2 = 4)](/img/notes/clis/python/python-console.png)

### Executing Scripts

You can alternatively use the `python` utility to execute pre-written Python programs. To test this out, create a new project directory called "my-first-project" with a new file called "my_script.py", and use your text editor to place inside the following contents:


```py
# my_script.py

print("--------------------------")
print("HELLO FROM A PYTHON SCRIPT")
print("--------------------------")
```

Make sure to save the file.

Then use the `python` utility to execute the script by specifying its filepath:

```sh
# using a relative filepath:
python my_script.py

# OR using an absolute filepath:
python path/to/my-first-project/my_script.py
```

![a screenshot of the output resulting from running a python script from the command-line. the hello message is printed in the terminal](/img/notes/clis/python/running-python-scripts.png)

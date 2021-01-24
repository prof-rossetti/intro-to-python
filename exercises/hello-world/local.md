# "Hello World (Local)" Exercise

## Learning Objectives

In this exercise, we'll practice using our local development environment for the first time by writing and executing a simple Python program.

## Prerequisites

This exercise assumes you have already done the [Command-line Computing Exercise](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf).

## Instructions

  1. Use your text editor to create a new file called "my_script.py" and save it on your Desktop.
  2. Use your text editor to write some python in the file.
  3. Remember to save the file.
  4. From the command-line, ensure your Anaconda "base" environment is active.
  5. where Python has been installed, run the file to see its output.

In your command-line application, navigate to the desktop:

```sh
cd ~/Desktop
```

Create a new Python file, perhaps called "my_script.py". For file naming, we use all lower case, with underscores between words as necessary. And the file must end with a ".py" extension:

```sh
touch my_script.py
```

Use your text editor to open the Python file:

```sh
code my_script.py
```






Example markdown:

```
# My First Repo!

This is the README.md file. It uses the markdown language. The line above is a heading, starting with the # sign. Don't be confused that # means something different in .md and .py files.

We can make links like [this](https://github.com/prof-rossetti/intro-to-python).

And lists too:

  + Item 1
  + Item 2
  + Item 3

For more information about Markdown syntax, see the [Markdown Guide](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf).
```


Example Python code:

```py
# This is an example python code cell
# Run it and see the output below
# These lines are "comments", starting with the #
# Don't be confused that # means something different in .md and .py files.

print("HELLO WORLD!")

x = 2 + 2
print(x)
```

## Success Criteria

Once you see the changes reflected in your remote project repository on GitHub.com, you have succeeded. Edit your existing text and code cells, and/or create new ones, then repeat steps 5-7 at least once for good measure.

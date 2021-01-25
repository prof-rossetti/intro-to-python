# "Hello World (Version Control)" Exercise

## Learning Objectives

In this exercise, we'll practice incorporating version control into our local development workflow.

## Prerequisites

This exercise assumes you have already done the ["Hello World (Local)" Exercise](local.md).

## Instructions

  1. On GitHub, create a new repository named something like "my-first-repo", and include a "README.md" file. We'll refer to this as the "remote repository".
  2. Use your Git client of choice to "clone" (download) the remote repository onto your local machine, perhaps onto the Desktop. We'll refer to this as the "local repository".
  3. Use your command-line application to navigate into the local repository.
  4. Open the local repository with your text editor.
  5. Use your text editor to edit the README.md file, using content like the example markdown below. Remember to save the file when you're done editing.
  6. Use your text editor to create a new file called "my_script.py" in the root directory of the repository. Add content like the example Python code below. Remember to save the file when you're done editing.
  7. Using your command-line application, ensure you've activated the Anaconda "base" environment, then run the Python file to make sure it produces the desired output.
  8. Use your Git Client to "make a commit" (save a new version) with a message like "Setup project repository".
  9. Use your Git Client to "push" the changes to GitHub / sync with the remote repository.


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

Once you see the new file contents reflected in your remote repository on GitHub, you have succeeded. Repeat the file-editing, committing and pushing steps at least one more time for good measure.


<hr>

## Solutions

Here are some of the commands you might use during the course of this exercise:

```sh
# create the remote repo and obtain its remote address - either the HTTPS or the SSH version, then ...

cd ~/Desktop
git clone REMOTE_ADDRESS # where REMOTE_ADDRESS is the remote address of your repo
cd my-first-repo/

code . # opens the project in the text editor
touch my_script.py # or do this via the text editor

# edit and save the files, then...
git add .
git commit -m "My first commit"
git push origin main

# edit and save the files, then...
git add .
git commit -m "My second commit"
git push origin main

# edit and save the files, then...
git add .
git commit -m "My third commit"
git push origin main
```

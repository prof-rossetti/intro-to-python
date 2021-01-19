# "Command-line Computing" Exercise

## Terminal (Mac OS) / Git Bash (Windows OS)

Open the Terminal application on Mac, or the Git Bash application on Windows.

> FYI: Mac users who are into maximum efficiency through keyboard shortcuts can get there quickly by pressing the "command + space" buttons to start a spotlight search, then begin typing the word "terminal", then hit enter when you see "Terminal" show up. :smiley_cat:
>
> ![a screenshot of the terminal app showing up as a result of a spotlight search](/img/exercises/command-line-computing/mac-shortcut.png)

![a screenshot of the terminal](/img/exercises/command-line-computing/mac-terminal.png)

> FYI: Mac users who are interested in customizing Terminal app color themes and keyboard shortcuts can reference the professor's [Terminal app configuration notes](mac-terminal-config.md). :smiley_cat:


## Instructions

After typing each of the commands below, press "enter" to execute it.

Optionally clear previous terminal output at any time by pressing "command + k", or by typing `clear` and pressing "enter".

### Current User

Print the current user's name:

```sh
whoami
```

### Present Working Directory

Print the current/present working directory:

```sh
pwd
```

### Listing Files in a Directory

List files in the current working directory:

```sh
ls
ls -al # for a different display
```

### Navigating and Managing Directories

Change directories (specifying an absolute file path):

```sh
cd ~/Desktop
```

> FYI: the tilde (`~`) represents your "home" filepath

> FYI: you can use `cd ..` to move "up" one directory relative to the current working directory

Open a directory via the operating system's filesystem explorer:

```sh
# Mac Terminal:
open .

# Windows Git Bash:
explorer .
```

Make a new directory:

```sh
mkdir my_folder
```

Remove a directory:

```sh
rm my_folder # triggers an error
rm -rf my_folder # recursively (-r) forces (-f) removal
```

### Managing Files

Setup a new directory in which to add some files, and navigate into that directory:

```sh
mkdir my_folder
cd my_folder
```

Create one or more files in the new directory you just created:

```sh
touch README.md
touch index.html
touch my_data.csv
touch my_message.txt
```

Remove a file:

```sh
rm index.html
```

Edit and save a file, using a command-line utility provided by your preferred text editor (just choose one of these, depending on which editor you're using):

```sh
# VS Code text editor, may first require installation of shell commands from the settings: 
code my_message.txt 

# Atom text editor, may first require installation of shell commands from the settings:
atom my_message.txt 
```

> NOTE: these text editor commands may require preliminary setup. For Mac users wanting to configure the `code` command, see these [VS Code shell command setup instructions](/notes/devtools/vs-code.md#shell-commands).

Print file contents:

```sh
cat my_message.txt
```

Move a file:

```sh
mv ~/Desktop/my_folder/my_message.txt ~/Desktop
```

> FYI: If you are into maximum efficiency, press "tab" to auto-complete file paths so you don't have to type the whole thing. :smiley_cat:

Copy a file:

```sh
cp ~/Desktop/my_message.txt ~/Desktop/my_folder
```

Copy contents of a file into the clipboard for pasting:

```sh
pbcopy < ~/Desktop/my_folder/my_message.txt
# ... then just paste as you normally would after copying some text
```

### Further Exploration (Mac only)

There are many other utilities to use from the command-line.

First, turn up the volume on your computer so everyone around you can hear, then make it speak:

```sh
say "Hello, I am your computer. Let's be friends." # or something else polite and appropriate
```

Optionally explore additional command-line interfaces, if you're curious.

#### Internet Computing

Trace the route traveled by a network request:

```sh
traceroute google.com
# ... stop after a few seconds if necessary by pressing: control + c
```

Time the duration of a network request:

```sh
ping google.com
# ... stop after a few seconds if necessary by pressing: control + c
```

Request the contents of a webpage:

```sh
curl google.com
curl http://www.google.com
curl https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json
```

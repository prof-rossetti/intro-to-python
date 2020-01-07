# Command-line Computing Exercise

## Terminal (Mac OS)

Open the Terminal application.

> FYI: If you are into maximum efficiency through keyboard shortcuts, get there quick by pressing the "command + space" buttons to start a spotlight search, then begin typing the word "terminal", then hit enter when you see "Terminal" show up. :smiley_cat:
>
> ![a screenshot of the terminal app showing up as a result of a spotlight search](/img/exercises/command-line-computing/mac-shortcut.png)

![a screenshot of the terminal](/img/exercises/command-line-computing/mac-terminal.png)

> FYI: If you are interested in learning how to customize color themes and keyboard shortcuts, you may reference a copy of [the professor's terminal configuration](mac-terminal-config.md). :smiley_cat:

## Instructions

After typing each of the commands below, press "enter" to execute it.

Optionally clear previous terminal output at any time by pressing "command + k".

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

### List Files in a Directory

List files in the current working directory:

```sh
ls
ls -al # for a different display
```

### Navigate and Manage Directories

Change directories (specifying an absolute file path):

```sh
cd ~/Desktop
```

> FYI: the tilde (`~`) represents your "home" filepath

Make a new directory:

```sh
mkdir my_folder
```

Remove a directory:

```sh
rm my_folder # triggers an error
rm -rf my_folder # recursively (-r) forces (-f) removal
```

### Manage Files

Change directories (using relative file path):

```sh
cd my_folder # first re-create this directory if it doesn't exist, else this will trigger an error
```

> FYI: Use the command `cd ..` to move "up" one directory relative to the current working directory.

Create one or more files:

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
code my_message.txt # VS Code text editor, may first require installation of shell commands from the settings
atom my_message.txt # Atom text editor, may first require installation of shell commands from the settings
```

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

### Further Exploration

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
curl https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-201905/master/data/products.json
```

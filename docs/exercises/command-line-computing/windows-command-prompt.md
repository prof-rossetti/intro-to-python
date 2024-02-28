# Command-line Computing Exercise

## Command Prompt (Windows OS)

Open the Command Prompt application.

> FYI: If you are into maximum efficiency through keyboard shortcuts, get there quick by pressing the "windows" button, then begin typing the word "command", then hit enter when you see "Command Prompt" show up. :smiley_cat:
>
> ![a screenshot of the command prompt app showing up as a result of a search](/img/exercises/command-line-computing/windows-shortcut.png)

![a screenshot of the command prompt](/img/exercises/command-line-computing/windows-command-prompt.png)

## Instructions

After typing each of the commands below, press "enter" to execute it.

Optionally, clear previous output at any time by typing "CLS" and pressing "enter".

### Current User

Print the current user's name:

```sh
whoami
```

### Present Working Directory

Print the current/present working directory:

```sh
cd
```

### List Files in a Directory

List files in the current working directory:

```sh
dir
```

### Navigate and Manage Directories

Change directories (specifying absolute file path):

```sh
cd C:\Users\YOUR_USERNAME\Desktop\ # where YOUR_USERNAME is the name of the user currently operating your local machine
```

> NOTE: if your username has a space in it (e.g. "Sammy Student"), then you may run into issues unless you surround the name of that directory with quotes (e.g. `cd C:\Users\"Sammy Student"\Desktop\`. This usage of quotes applies to any / all files and directories which may have spaces in them, so in general you are encouraged to create new files and directories without any spaces in them, to make life easier on yourself.

Make a new directory:

```sh
mkdir my_folder
```

Remove a directory:

```sh
rmdir my_folder
```

### Manage Files

Change directories (using relative file path):

```sh
cd my_folder # first re-create this directory if it doesn't exist, else this will trigger an error
```

> FYI: Use the command `cd ..` to move "up" one directory relative to the current working directory.

Create one or more files:

```sh
type nul > README.md
type nul > index.html
type nul > my_data.csv
type nul > my_message.txt
```

> CLARIFICATION: yes, `type` is part of the command :smiley_cat:

Remove/delete a file:

```sh
del index.html
```

Edit and save a file, using a command-line utility provided by your preferred text editor (just choose one of these, depending on which editor you're using):

```sh
code my_message.txt # VS Code text editor, may first require installation of shell commands from the settings
atom my_message.txt # Atom text editor, may first require installation of shell commands from the settings
```

Print file contents:

```sh
type my_message.txt
```

Move a file to target location:

```sh
move C:\Users\YOUR_USERNAME\Desktop\my_folder\my_message.txt C:\Users\YOUR_USERNAME\Desktop
```

> FYI: If you are into maximum efficiency, press "tab" to auto-complete file paths so you don't have to type the whole thing. :smiley_cat:

Copy a file:

```sh
xcopy C:\Users\YOUR_USERNAME\Desktop\my_message.txt C:\Users\YOUR_USERNAME\Desktop\my_folder
```

Copy contents of a file into the clipboard for pasting:

```sh
type C:\Users\YOUR_USERNAME\Desktop\my_folder\my_message.txt | clip
# ... then just paste as you normally would after copying some text
```

### Further Exploration

Optionally explore additional command-line interfaces, if you're curious.

#### Internet Computing

Trace the route traveled by a network request:

```sh
tracert google.com # stop after a few seconds if necessary by pressing: control + c
```

Time the duration of a network request:

```sh
ping google.com # stop after a few seconds if necessary by pressing: control + c
```

Download the [cURL](https://curl.haxx.se/download.html) utility if necessary, then request the contents of a webpage:

```sh
curl google.com
curl http://www.google.com
curl https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json
```

You may need to execute these commands from within the downloaded directory. See ["Installing cURL on Windows"](http://stackoverflow.com/questions/9507353/how-do-i-install-set-up-and-use-curl-on-a-windows) for more support.

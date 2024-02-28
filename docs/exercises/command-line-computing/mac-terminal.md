# "Command-line Computing" Exercise

## Command-line Application

Open the Terminal application (Mac) or the Git Bash application (Windows). 

### Git Bash (Windows OS)

> FYI: Windows users who are into maximum efficiency through keyboard shortcuts can get there quickly by pressing the "windows" button, then begin typing the word "git", then hit enter when you see "Git Bash" show up. 😺

### Terminal (Mac OS) 

> FYI: Mac users who are into maximum efficiency through keyboard shortcuts can get there quickly by pressing the "command + space" buttons to start a spotlight search, then begin typing the word "terminal", then hit enter when you see "Terminal" show up. :smiley_cat:
>
> ![a screenshot of the terminal app showing up as a result of a spotlight search](/img/exercises/command-line-computing/mac-shortcut.png)

![a screenshot of the terminal](/img/exercises/command-line-computing/mac-terminal.png)

> FYI: Mac users who are interested in customizing Terminal app color themes and keyboard shortcuts can reference the professor's [Terminal app configuration notes](mac-terminal-config.md). :smiley_cat:




## Instructions

After typing each of the commands below, press "enter" to execute it.

Optionally clear previous terminal output at any time by pressing "command + k", or by typing `clear` and pressing "enter".

### Current User

Display the current user's name:

```sh
whoami
```

### Present Working Directory

Display the current/present working directory:

```sh
pwd
```

### Listing Files in a Directory

List files in the current working directory:

```sh
ls

# alternatively, for a different display:
ls -al 
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
# triggers an error:
rm my_folder

# uses options called flags to recursively (-r) force (-f) removal
rm -rf my_folder 
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

Edit and save a file, using a command-line utility provided by your preferred text editor (like VS Code):

```sh
code my_message.txt 
```

> NOTE: Mac users may need to first configure the `code` command by following these [VS Code shell command setup instructions](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/devtools/vs-code.md#shell-commands)

Display file contents:

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
# Mac OS:
pbcopy < ~/Desktop/my_folder/my_message.txt

# Windows OS:
cat ~/Desktop/my_folder/my_message.txt | clip

# ... then just paste as you normally would after copying some text
```


### Further Exploration

There are many other utilities to use from the command-line. For example, you may optionally try some of the examples below.


#### Further Exploration (Windows or Mac)

To download videos from YouTube, try using the [`youtube-dl` command-line utility](/notes/clis/youtube-dl.md) (see the linked notes document for installation and usage instructions).

#### Further Exploration (Mac only)


Making your computer speak:

```sh
say "Hello, I am your computer. Let's be friends." # or something else polite and appropriate
```

##### Internet Computing

Tracing the route traveled by a network request:

```sh
traceroute google.com
# ... stop after a few seconds if necessary by pressing: control + c
```

Timing the duration of a network request:

```sh
ping google.com
# ... stop after a few seconds if necessary by pressing: control + c
```

Requesting the contents of a webpage:

```sh
curl google.com
curl http://www.google.com
curl https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json
```

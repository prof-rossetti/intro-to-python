

# Environment Variables

> See [Environment Variables](/notes/environment-variables.md)

## Setting Globally via the Command Line

Mac and Windows users can set environment variables from the command line. Windows users may need to use the `set` keyword (or `export`, if `set` doesn't work):

```sh
# Mac Terminal:
MY_SECRET_MESSAGE="SecretPassword123"

# Windows Command Prompt:
set MY_SECRET_MESSAGE="SecretPassword123"

# Mac Terminal or Windows Command Prompt:
export MY_SECRET_MESSAGE="SecretPassword123"
```


> NOTE: if you close your command prompt and re-open it, you may need to re-set the environment variable.


## Setting Globally via Hidden Config File

Mac users (and Windows Git Bash users) should be able to manage global environment variables using a hidden configuration file called either "~/.bash_profile" or "~/.zshrc", depending on your OS. Open the file with your text editor (e.g. `code ~/.bash_profile`), and place inside the following contents:

```sh
#
# this is the "~/.bash_profile" file
# ... or the "~/.zshrc" file (for newer Macs with the "Zsh" shell)
#

export MY_SECRET_MESSAGE="SecretPassword123"
export MY_OTHER_MESSAGE="SecretPassword456"
```

Then exit and re-open your Terminal for the changes to take effect.


## Getting

You will know you have successfully set an environment variable when you can access its value from the command-line:

```shell
# Mac Terminal:
echo $MY_SECRET_MESSAGE
#> SecretPassword123

# Windows Command Prompt:
echo %MY_SECRET_MESSAGE%
#> SecretPassword123
```

To access environment variables from within a Python program, use [the `os` module](/notes/python/modules/os.md#environment-variables).

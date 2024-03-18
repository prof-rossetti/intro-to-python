# The `dotenv` Package

The `dotenv` package allows a program to reference [Environment Variables](./../../environment-variables/README.md) from a special file called ".env" in the root directory of the given project, instead of passing them from the command-line.

This file-based approach makes environment variables much easier to manage, especially for Windows users.

Reference: https://github.com/theskumar/python-dotenv.

See also: [The `os` Module](./../modules/os.md#environment-variables) for reading environment variables.

## Installation

First install the package, if necessary:

```sh
pip install python-dotenv # note: NOT just "dotenv"
```

## Usage


To setup this example, create a new directory on your Desktop named "my-secure-project". Then navigate there from the command-line:

```sh
cd Desktop/my-secure-project/
```

Create three files in the "my-secure-project" directory named ".env", ".gitignore", and "my_script.py", respectively, and place inside the following contents:

```sh
# this is the "my-secure-project/.env" file...

SECRET_MESSAGE="Hello World"
```

```sh
# this is the "my-secure-project/.gitignore" file...

# ignore the contents of the ".env" file (prevent them from being exposed on GitHub):
.env
```

```py
# this is the "my-secure-project/my_script.py" file...

import os
from dotenv import load_dotenv

load_dotenv() #> invoking this function loads contents of the ".env" file into the script's environment...

# ... where they can be accessed / read via the os module as usual:
print(os.getenv("SECRET_MESSAGE"))
```

And run the script to see the output:

```sh
python my_script.py
#> "Hello World"
```

The lesson is that the `load_dotenv()` function will load environment variables from the ".env" file into the Python script's environment so they can be accessed via the `os` module.

Also, it's important to ensure there is a ".env" entry in your ".gitignore" file before making any commits. This prevents the ".env" file from being uploaded to GitHub. This is important on a practical level because ".env" files often contain sensitive information like secret passwords and API Keys, and preventing these credentials from being exposed on GitHub is an important security best practice (even if your remote repo is private).

> SECURITY NOTE: after pushing a repo to GitHub, you shouldn't be able to see the ".env" online. If you do see the ".env" in your remote repo on GitHub, follow these remediation steps:
>   1. Delete the ".env" file from your local repo, and make a commit.
>   2. Ensure you have a ".env" entry in your local ".gitignore" file, and make another commit if necessary. 
>   3. Finally, re-add the ".env" file to your local repo. Next time you push to GitHub, this file should no longer be in your remote repo.

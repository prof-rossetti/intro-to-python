# The `pip` Utility

Reference:

  + https://docs.python.org/3/installing/index.html#installing-index
  + https://packaging.python.org/tutorials/installing-packages

When you install Python, you also get Python's package manager, Pip. Use Pip to install and manage third-party Python packages.

Listing packages currently installed:

```sh
pip list #> should see all installed packages, as well as their package dependencies
```

Installing packages:

```sh
pip install pandas # where pandas is the name of a package you want to install
```

## Project-specific Package Management

You can specify and manage project-specific package dependencies by listing them in a special file called "requirements.txt" in the project's root directory.

To specify a project's dependencies, first create a new "requirements.txt" file in your repository's root directory, then revise the file to include the names of the packages your project requires. Write the name of each Python package dependency on a new line. For example:

    pytest
    requests
    pandas
    python-dotenv
    git+https://github.com/eskerda/pybikes.git # can install from GitHub source via HTTPS
    git+ssh://git@github.com/s2t2/game-utils-py.git # can install from GitHub source via SSH

Make sure to save the file. Then finally, use Pip to install package dependencies by specifying the requirements filepath:

```sh
pip install -r requirements.txt
```

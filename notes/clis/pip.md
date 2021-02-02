# The `pip` Utility

Reference:

  + https://docs.python.org/3/installing/index.html#installing-index
  + https://packaging.python.org/tutorials/installing-packages

Each programming language generally has its own way of installing third-party packages, and certain files to keep track of a project's package requirements. For Python, the package manager is called Pip, and is usually installed alongside Python (via Anaconda).
 
Pip will help us install third-party Python packages, like ones we might find shared on GitHub, or more officially on [PyPI](https://pypi.org/), the Python Package Index.

## Usage

### Listing Packages

Listing packages currently installed:

```sh
pip list #> should see all installed packages, as well as their package dependencies
```

### Installing Packages

We can install packages one at a time (not recommended):

```sh
pip install pandas # where pandas is the name of a package we want to install
```

#### Project-specific Package Management

We can also manage project-specific package dependencies by listing them all in a special file called "requirements.txt" in the project's root directory. This is the recommended approach that allows us to install all the packages at once, and also keeps an official record of their versions. It is possible for "breaking changes" from updated versions of underlying packages to introduce bugs into our apps, so it is helpful to keep track of which versions are being used. 

If we have an existing project, we can `pip freeze > requirements.txt` to create a new requirements file to reflect the existing environment. But more commonly, we'll create the requirements file first and build the environment around it.

First create a new "requirements.txt" file in your repository's root directory, then revise the file to include the names of the packages your project requires. Write the name of each Python package dependency on a new line. For example, any of the following:

    # this is the requirements.txt file!
    pytest
    requests
    pandas
    python-dotenv
    sendgrid==5.6.0 # can "lock" a specific version of the package
    git+https://github.com/eskerda/pybikes.git # can install from GitHub source via HTTPS
    git+ssh://git@github.com/s2t2/game-utils-py.git # can install from GitHub source via SSH

Make sure to save the file. Then finally, use Pip to install package dependencies by specifying the requirements filepath:

```sh
pip install -r requirements.txt
```


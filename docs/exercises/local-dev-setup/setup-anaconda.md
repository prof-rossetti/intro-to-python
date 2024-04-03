
## Anaconda, Python, and Pip

The goal is to have access to command-line tools for running Python programs and installing Python packages.

The Python programming language evolves over time as new features are added and new versions are released. For this course, we'll want to be running any Python version 3.7 or greater. By default, Mac computers have a super old version of Python (2.x) we don't want to mess with, and Windows computers don't have any version of Python installed. So we'll need to install Python separately.

Rather than install a single specific version of Python, and use that same version for all projects, sometimes different projects in a professional setting will require different minor versions of Python. So we'll use a tool called Anaconda to manage project-specific "virtual environments". Each virtual environment is like a separate work space with a different version of Python and combination of third-party Python packages installed inside.

Unless it is already installed, [install Anaconda](https://www.anaconda.com/download) for either Mac or Windows. You're encouraged to also review the professor's [Anaconda installation reference](./../../notes/clis/conda.md#installation) for more details, tips, and tricks.

If successful, you should be able to run the following commands:

```sh
# to see if conda is installed:
conda --version

# to check what environments exist (hopefully you see "base"):
conda info --envs

# to create and activate a new virtual environment
# ... for example one called "my-first-env"
# ... with a specified version of python, for example 3.8:
conda create -n my-first-env python=3.8
conda activate my-first-env

# to see which version of python and pip are installed in this environment:
python --version
pip --version

# to see which packages are installed in this environment:
pip list
```

> NOTE: when using `conda` to activate a virtual environment for the first time, when prompted to do so, Windows Git Bash users may need to run `conda init bash`, and Mac Zsh profile users may need to run `conda init zsh`. If you do, close your command-line application and open another window for the changes to take affect, then try again.

> NOTE: if you see "conda: command not found", it means there's something wrong with your installation. It's OK. Feel free to reach out to an instructor and ask for help. See also these [known troubleshooting remedies](https://github.com/prof-rossetti/intro-to-python/issues/13).

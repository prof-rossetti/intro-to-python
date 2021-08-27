# Local Development Environment Setup Guide (COSC 010)

> NOTE: this guide is for COSC 010 students!

This document helps you install and configure tools to develop and run Python applications on your local machine.

## GitHub

GitHub is a platform for sharing software projects, called "repositories". We will be saving copies of our Colab Notebooks (and maybe also some local Python files) to GitHub, to build an online portfolio.

Unless you already have one, take a moment to [create a GitHub account](https://github.com/). 

Afterwards, consider signing up for the [GitHub Student Developer Pack](https://education.github.com/pack), which provides some free resources.

> PRIVACY OPTIONS: Many students wish to associate their personal identities with their GitHub accounts, to display a portfolio of programming projects. However, if you're concerned about privacy, you have a few options. First, consider choosing a GitHub username which is different than your university-issued net identifier. Second, avoid uploading any personally-identifiable information to your GitHub profile. Third, consider submitting projects via private repositories.

If successful, when you view this page on GitHub, you should be able to click the buttons on the top-right of the page to "Star" the course repository, and also "Fork" it (i.e. create a copy under your own control).

## Command-line Application

The goal is to have access to a command-line application of choice, which we'll use for a variety of purposes. 

Mac users who don't already have a preferred command-line application are encouraged to use the built-in Terminal application (no need to download anything, although you may want to [customize](/exercises/command-line-computing/mac-terminal-config.md) the Terminal appearance as desired).

Windows users who don't already have a preferred command-line application are encouraged to install [Git Bash](https://git-scm.com/downloads), which will allow Windows users to write the same unix-style commands as Mac users.

Alternatively, students on Mac or Windows may be able to use an integrated terminal in their text editor or IDE, but it may require additional configuration. 

If successful, you should be able to use your command-line application to complete the ["Command-line Computing" Exercise](/exercises/command-line-computing/README.md), which will introduce you to useful commands (like these, for navigating your local filesystem):

```sh
cd ~/Desktop
pwd
ls -al
```

## Anaconda, Python, and Pip

The goal is to have access to tools for installing Python packages and running Python programs. 

The Python programming language evolves over time as new features are added and new versions are released. For this course, we'll want to be running any Python version 3.7 or greater. By default, Mac computers have a super old version of Python (2.x) we don't want to mess with, and Windows computers don't have any version of Python installed. So we'll need to install Python separately. 

Rather than install a single specific version of Python, and use that same version for all projects, sometimes different projects in a professional setting will require different minor versions of Python. So we'll use a tool called Anaconda to manage project-specific "virtual environments". Each virtual environment is like a separate work space with a different version of Python and combination of third-party Python pacakges installed inside.

Unless it is already installed, [install Anaconda](https://www.anaconda.com/download) for either Mac or Windows. You're encouraged to also review the professor's [Anaconda installation reference](/notes/clis/conda.md#installation) for more details, tips, and tricks.

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


## Text Editor / IDE

The goal is to have access to a text-editing application of choice, which we'll use to create and edit files of Python code (i.e. text files written in the Python Language and ending in the ".py" extension).

Unless you already have a text editor of choice, let's use the Spyder application which provides not only text editing capabilities, but also an integrated development environment (IDE) capable of running Python programs as well.

By installing Anaconda, you should also see the Spyder application has been installed.


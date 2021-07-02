# Local Development Environment Setup Guide

This document helps you install and configure tools to develop and run Python applications on your local machine.

## GitHub

We'll use GitHub to manage, share, and submit different versions of our software projects, called "repositories".

Unless you already have one, take a moment to [create a GitHub account](https://github.com/). 

Afterwards, consider signing up for the [GitHub Student Developer Pack](https://education.github.com/pack), which provides some free resources.

> PRIVACY OPTIONS: Many students wish to associate their personal identities with their GitHub accounts, to display a portfolio of programming projects. However, if you're concerned about privacy, you have a few options. First, consider choosing a GitHub username which is different than your university-issued net identifier. Second, avoid uploading any personally-identifiable information to your GitHub profile. Third, consider submitting projects via private repositories.

## Text Editor

The goal is to have access to a text-editing application of choice, which we'll use to create and edit files of Python code (i.e. text files written in the Python Language and ending in the ".py" extension).

Unless you already have a text editor of choice, install [VS Code](https://code.visualstudio.com/).

After installing VS Code, take some time to explore the settings and the "Command Palette". You're encouraged to review the professor's [VS Code configuration reference](/notes/devtools/vs-code.md#basic-configuration) for more details, tips, and tricks.

## Command-line Application

The goal is to have access to a command-line application of choice, which we'll use for a variety of purposes. 

Mac users who don't already have a preferred command-line application are encouraged to use the built-in Terminal application (no need to download anything, although you may want to [customize](/exercises/command-line-computing/mac-terminal-config.md) the Terminal appearance as desired).

Windows users who don't already have a preferred command-line application are encouraged to install [Git Bash](https://git-scm.com/downloads), which will allow Windows users to write the same unix-style commands as Mac users.

Alternatively, students on Mac or Windows may be able to use the integrated terminal in VS Code, but it may require additional configuration. 

If successful, you should be able to use your command-line application to complete the ["Command-line Computing" Exercise](/exercises/command-line-computing/README.md), which will introduce you to useful commands (like these, for navigating your local filesystem):

```sh
cd ~/Desktop
ls -al
```

## Anaconda, Python, and Pip

The goal is to be able to run Python programs from the command-line. 

The Python programming language evolves over time as new features are added and new versions are released. For this course, we'll want to be running a Python version greater than 3.7. By default, Mac computers have a super old version of Python (2.x) we don't want to mess with, and Windows computers don't have any version of Python installed. So we'll need to install Python somehow. 

Rather than install a single specific version of Python, and use that same version for all projects, sometimes different projects in a professional setting will require different minor versions of Python. So we'll use a tool called Anaconda to help us flexibly install different versions of Python in a project-specific way.

When we install Anaconda, we get to create project-specific "virtual environments", which are essentially separate work spaces on your computer, each with a specific version of Python installed inside. After "activating" a given virtual environment, we'll have access to the proper versions of the Python and Pip command-line tools. 

We'll use the Python command-line tool to run Python programs. Each Python program generally requires its own set of third-party "package" dependencies. Packages are essentially separate open source libraries of Python code we can use to do certain things, but they aren't included in the official Python Language, so we need to install them separately. We use the Pip tool to install these packages before we're able to run the Python program that requires them. When we use Pip to install a package, we are installing it from the centralized [Python Package Index (PyPI)](https://pypi.org/), where the package maintainer has already uploaded the source code for that package.

Wow, enough background already!

Unless it is already installed, install [Anaconda Version 3.8](https://www.anaconda.com/download) for either Mac or Windows. You're encouraged to also review the professor's [Anaconda installation reference](/notes/clis/conda.md#installation) for more details, tips, and tricks.

> IMPORTANT: make sure to check the "add to PATH" option during installation, on Windows, so Anaconda will integrate with the other local development tools such as Git Bash on Windows.

If successful, you should be able to run the following commands:

```sh
# to see if conda is installed:
conda --version

# to check what environments exist (hopefully you see "base"):
conda info --envs

# to create and activate a new virtual environment with the right version of python installed:
conda create -n my-first-env python=3.8
conda activate my-first-env

# to see if python is installed (after activating the virtual environment):
python --version
pip --version
```

> NOTE: when using `conda` to activate a virtual environment for the first time, when prompted to do so, Windows Git Bash users may need to run `conda init bash`, and Mac Zsh profile users may need to run `conda init zsh`. If you do, close your command-line application and open another window for the changes to take affect, then try again.

## Version Control Utilities

A "version control" tool will help us download projects from GitHub and upload projects to GitHub. We'll ultimately want to use the Git Command-line Utility (CLI) to do this. But many students think Git is harder to learn than Python, so beginners can feel free to get started with the GitHub Desktop software, which provides an easier to use graphical user interface (GUI).

### Git CLI

Windows users who have installed Git Bash (see "Command-line Application" section above) will have satisfied the Git installation requirement.

Mac users may find that a system version of Git is already installed, but we'll want to use a newer version. So all Mac users are encouraged to [install Homebrew](/notes/clis/brew.md), then [use Homebrew to install Git](/notes/clis/git.md#installation-on-mac). 

After installing Git, all students should generate SSH keys and configure their account credentials. You're encouraged to review the professor's [Git configuration reference](/notes/clis/git.md#configuration) for more details.

If successful, you should be able to run the following command:

```sh
git --version
```

### GitHub Desktop

Students who want to use GitHub Desktop should first install the Git CLI (see step above), then also install [GitHub Desktop software](https://desktop.github.com/) on Mac or Windows.

After installing, you will need to login with your GitHub account credentials. You're encouraged to review the professor's [GitHub Desktop configuration reference](/notes/devtools/github-desktop.md#configuration) for more details.

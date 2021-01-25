# Setting up your Local Development Environment

This document helps you install and configure the tools you'll need to develop Python applications on your local machine.

## GitHub

Unless you already have one, take a moment to [create a GitHub account](https://github.com/). We'll use this platform to manage, share, and submit different versions of our Python projects.

Afterwards, consider signing up for the [GitHub Student Developer Pack](https://education.github.com/pack), which provides some free resources.

> PRIVACY OPTIONS: Many students wish to associate their personal identities with their GitHub accounts, to display a portfolio of programming projects. However, if you're concerned about privacy, you have a few options. First, consider choosing a GitHub username which is different than your university-issued net identifier. Second, avoid uploading any personally-identifiable information to your GitHub profile. Third, sign up for the Student Developer Pack, which will allow you to submit projects via free private repositories.

## Text Editor

Unless you already have a text editor of choice, install [VS Code](https://code.visualstudio.com/).

After installing VS Code, take some time to [configure](/notes/devtools/vs-code.md#basic-configuration) it in helpful ways.

## Command-line Application

Mac users who don't already have a preferred command-line application are encouraged to use the built-in Terminal application (no need to download anything, although you may want to [customize](/exercises/command-line-computing/mac-terminal-config.md) the Terminal appearance as desired).

Windows users who don't already have a preferred command-line application are encouraged to install [Git Bash](https://git-scm.com/downloads), which will allow Windows users to write the same unix-style commands as Mac users.

> FYI: The ["Command-line Computing" Exercise](/exercises/command-line-computing/README.md) will introduce you to the most useful commands.

## Anaconda

Unless it is already installed, install [Anaconda Version 3.8](https://www.anaconda.com/download) for either Mac or Windows. See the professor's [Anaconda installation reference](/notes/clis/conda.md#installation) for more details.

> IMPORTANT: remember to check the "add to PATH" option during installation, especially on Windows, so Anaconda will integrate with the other local development tools such as Git Bash on Windows.

> NOTE: when using `conda` to activate a virtual environment for the first time, when prompted to do so, Windows Git Bash users may need to run `conda init bash`, and Mac Zsh profile users may need to run `conda init zsh`.

> NOTE: if experiencing issues recognizing `conda` commands on Mac OS Catalina, reference these [Catalina setup steps](https://github.com/prof-rossetti/intro-to-python/issues/13).

## Version Control Utilities

A "version control" tool will help us download projects from GitHub and upload projects to GitHub. We'll ultimately want to use the Git Command-line Utility (CLI) to do this. But many students think Git is harder to learn than Python, so beginners can feel free to get started with the GitHub Desktop software, which provides an easier to use graphical user interface (GUI).

### Git CLI

Windows users who have installed Git Bash (see "Command-line Application" section above) will have satisfied the Git installation requirement.

Mac users may find that Git is already installed, otherwise you are encouraged to install Git via Homebrew. See the professor's [Git installation reference](/notes/clis/git.md#installation) for more details.

After installing Git, students may need to configure their account credentials. See the professor's [Git configuration reference](/notes/clis/git.md#configuration) for more details.

### GitHub Desktop

Students who want to use GitHub Desktop should first install the Git CLI (see step above), then they can also install [GitHub Desktop software](https://desktop.github.com/) on Mac or Windows.

After installing, you will need to login with your GitHub account credentials. See the professor's [GitHub Desktop configuration reference](/notes/devtools/github-desktop.md#configuration) for more details.

# Unit 0: Onboarding

## Learning Objectives

Hello and welcome! In this unit, we'll prepare to start developing Python applications by installing all the necessary development tools.

## Development Tools Overview

Category | Recommended Tool | Purpose
--- | --- | ---
Text Editor | VS Code | For creating, reading, editing, and deleting files of Python code.
Command-line | Mac Terminal or Windows Git Bash | For interfacing with the computer in programmatic ways (i.e. to install or execute software).
Virtual Environment Manager | Anaconda (`conda`) | For installing different versions of the Python programming language.
Programming Language | Python (`python`) | For executing files of code written in the Python programming language.
Package Manager | Pip (`pip`)| For installing third-party packages written in the Python programming language.
Version Control | Git (`git`) and GitHub Desktop | For incrementally saving different versions of software files, and interfacing with GitHub, which is a place to share software files online.

## Development Tools Setup

### GitHub

Unless you already have one, please take a moment to [create a GitHub account](https://github.com/). We'll use this platform to manage, share, and submit different versions of our Python projects.

Afterwards, consider signing up for the [GitHub Student Developer Pack](https://education.github.com/pack), which provides some free resources.

> PRIVACY OPTIONS: Many students wish to associate their personal identities with their GitHub accounts, to display a portfolio of programming projects. However, if you're concerned about privacy, you have a few options. First, consider choosing a GitHub username which is different than your university-issued net identifier. Second, avoid uploading any personally-identifiable information to your GitHub profile. Third, sign up for the Student Developer Pack, which will allow you to submit projects via private repositories.

### Text Editor

Unless you already have a text editor of choice, please install [VS Code](https://code.visualstudio.com/). After doing so, make sure to install and enable the [Python language extension](/notes/devtools/vs-code.md#python-syntax-auto-completion), which provides Python code syntax-highlighting and auto-completion capabilities. Also take some time to [customize](/notes/devtools/vs-code.md#basic-configuration) the text editor's appearance and functionality, as desired.

### Command-line

Mac users who don't already have a preferred command-line application are encouraged to use the built-in Terminal application (no need to download anything, although you may want to [customize](/exercises/command-line-computing/mac-terminal-config.md) the Terminal appearance and functionality, as desired).

Windows users who don't already have a preferred command-line application are encouraged to install [Git Bash](https://git-scm.com/downloads), which will allow Windows users to write the same unix-style commands as Mac users.

> NOTE: Windows users who choose an alternative command-line application (such as the Command Prompt or Anaconda Prompt) are responsible for translating between unix-style commands and windows-style commands. The command-line computing exercise linked at the bottom of this document can help.

### Anaconda

Unless it is already installed, install [Anaconda Version 3.8](https://www.anaconda.com/download) for either Mac or Windows. See the professor's [Anaconda installation reference](/notes/clis/conda.md#installation) for more details.

> IMPORTANT: remember to check the "add to PATH" option during installation, especially on Windows, so Anaconda will integrate with the other local development tools such as Git Bash on Windows.

> NOTE: when using `conda` to activate a virtual environment for the first time, when prompted to do so, Windows Git Bash users may need to run `conda init bash` and Mac Zsh profile users may need to run `conda init zsh`.

> NOTE: if experiencing issues recognizing `conda` commands on Mac OS Catalina, reference these [Catalina setup steps](https://github.com/prof-rossetti/intro-to-python/issues/13).

### Version Control Utilities

We'll use the Git Command-line Utility and the GitHub Desktop software to upload our Python projects to the GitHub platform.

#### Git

Windows users who have installed Git Bash (see "Command-line Application" section above) will have satisfied the Git installation requirement.

Mac users may find that Git is already installed, otherwise you are encouraged to install Git via Homebrew. See the professor's [Git installation reference](/notes/clis/git.md#installation) for more details.

#### GitHub Desktop

After installing Git, Mac and Windows users should also install the [GitHub Desktop software](https://desktop.github.com/) and login with your GitHub account credentials. See the professor's [GitHub Desktop configuration reference](/notes/devtools/github-desktop.md#configuration) for more details.

## Preparation Exercise

Finally, to become more comfortable with command-line computing, complete this [Command-line Computing exercise](/exercises/command-line-computing).

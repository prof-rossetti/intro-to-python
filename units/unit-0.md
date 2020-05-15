# Unit 0: Onboarding

## Objectives

Welcome to this Introductory Python course! In this unit, we'll prepare to start working with Python applications by installing all the requisite development tools.

## Development Tools Overview

Category | Recommended Tool(s) | Purpose
--- | --- | ---
Text Editor | VS Code | For creating, reading, editing, and deleting files of Python code.
Command-line | Mac Terminal, Windows Git Bash | For interfacing with the computer in programmatic ways (i.e. installing and running software).
Virtual Environment Manager | Anaconda (`conda`) | For installing different versions of the Python programming language.
Programming Language Utility | Python (`python`) | For executing files of code written in the Python programming language.
Package Manager | Pip (`pip`)| For installing third-party packages written in the Python programming language.
Version Control Utility | Git (`git`) | For incrementally saving different versions of software files, and interfacing with GitHub, which is a place to share code repositories online.
Server Management Utility | Heroku (`heroku`) | For provisioning and managing remote servers on which to run software.

## Development Environment Setup

### GitHub

Unless you already have one, please take a moment to [create a GitHub account](https://github.com/). We'll use this platform to manage, share, and submit different versions of our Python projects.

Afterwards, consider signing up for the [GitHub Student Developer Pack](https://education.github.com/pack), which provides some free resources.

> PRIVACY OPTIONS: Many students wish to associate their personal identities with their GitHub accounts, to display a portfolio of programming projects. However, if you're concerned about privacy, you have a few options. First, consider choosing a GitHub username which is different than your university-issued net identifier. Second, avoid uploading any personally-identifiable information to your GitHub profile. Third, sign up for the Student Developer Pack, which will allow you to submit projects via private repositories.

### Text Editor

Unless you already have a text editor of choice, please install [VS Code](https://code.visualstudio.com/). After doing so, make sure to install and enable the [Python language extension](/notes/devtools/vs-code.md#python-syntax-auto-completion), which provides Python code syntax-highlighting and auto-completion capabilities. Also take some time to [customize](/notes/devtools/vs-code.md#basic-configuration) the text editor's appearance and functionality, as desired.

### Command-line Application

Mac users who don't already have a preferred command-line application are encouraged to use the built-in Terminal application (no need to download anything, although you may want to [customize](/exercises/command-line-computing/mac-terminal-config.md) the Terminal appearance and functionality, as desired). 

Windows users who don't already have a preferred command-line application are encouraged to install [Git Bash](https://git-scm.com/downloads), which will allow Windows users to write the same commands as Mac users. Windows users who would like to use an alternative command-line application such as the Command Prompt or Anaconda Prompt are responsible for translating between unix-style commands and windows-style commands.

Mac or Windows students who'd rather configure and use the built-in terminal inside the VS Code text editor may do so, although this can be tricky to configure. 

### Anaconda

Unless it is already installed, install [Anaconda Version 3.7](https://www.anaconda.com/download) for either Mac or Windows. 

> IMPORTANT: remember to check the "add to PATH" option during installation, especially on Windows, so Anaconda will integrate with the other local development tools such as Git Bash on Windows. See the professor's [Anaconda installation reference](/notes/clis/conda.md#installation) for more details.

### Git

GitHub Desktop software will require the Git command-line utility to be installed on our computers. So let's install Git now. See the professor's [Git installation reference](/notes/clis/git.md#installation) for more details.

This installation should also install a program called Git Bash, which Windows users will use as their default command-line computing application.

### GitHub Desktop

Unless you already have a Git client of choice, please install the [GitHub Desktop software](https://desktop.github.com/) and login with your GitHub account credentials. We'll use this software to upload our Python projects to the GitHub platform. See the professor's [GitHub Desktop configuration reference](/notes/devtools/github-desktop.md#configuration) for more details.

## Activities and Exercises

  + ["Command-line Computing" Exercise](/exercises/command-line-computing)

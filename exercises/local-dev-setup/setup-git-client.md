
## Version Control Utilities

A "version control" tool helps us upload and download projects to and from GitHub, and save different versions of our project code. 

Professionals usually use Git from the command line, but there is a learning curve involved. So beginners are encouraged to get started with GitHub Desktop first, which provides an easier to use graphical user interface (GUI).


### GitHub Desktop

Install [GitHub Desktop software](https://desktop.github.com/), for Mac or Windows.

After installing, you will need to login with your GitHub account credentials. See this [GitHub Desktop setup guide](https://docs.github.com/en/desktop/installing-and-authenticating-to-github-desktop/setting-up-github-desktop), and the professor's [GitHub Desktop configuration reference](/notes/devtools/github-desktop.md#configuration) for more details.

> NOTE: Using GitHub Desktop requires the Git command line utility to be installed on your computer (see below).

### Git CLI

Installing Git depends on your operating system:

  + Windows users who have [installed Git Bash](/exercises/local-dev-setup/setup-terminal.md) will have satisfied the Git installation requirement.
  + Mac users may find that a system version of Git is already installed, and that might be sufficient to satisfy the Git installation requirement. Any Mac users who encounter errors or who desire a newer version of Git can consider [installing Homebrew](/notes/clis/brew.md), and [using Homebrew to install Git](/notes/clis/git.md#installation-on-mac).


Verifing Git has been installed:

```sh
git --version
```


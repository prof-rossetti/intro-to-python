# Anaconda

Anaconda provides a command-line utility called `conda` for installing and managing different versions of the Python programming language and third-party packages.  

> Anaconda is a package manager, an environment manager, a Python/R data science distribution, and a collection of over 1,500+ open source packages. Anaconda is free and easy to install, and it offers free community support. - [Anaconda website](https://docs.anaconda.com/anaconda/)

## References

  + [Getting Started with Conda](https://conda.io/docs/user-guide/getting-started.html)
  + [Managing Conda Environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

## Detection

To check to see if Anaconda is already installed:

```sh
conda --version
#> conda 4.5.12

# Mac Terminal:
which conda
#> /anaconda3/bin/conda

# Windows Anaconda Prompt or Git Bash:
where conda
#> C:\Users\YOUR_USERNAME\Anaconda3\Library\bin\conda.bat
#> C:\Users\YOUR_USERNAME\Anaconda3\Scripts\conda.exe
```

### Detection on Mac

On a Mac, you can invoke the detection commands directly in the Terminal:

![](/img/notes/clis/conda/mac-terminal.png)

### Detection on Windows

On Windows, you can search for the "Anaconda Prompt" application to know whether or not you have Anaconda installed (although we will not ususally be using this application):

![](/img/notes/clis/conda/windows-detecting-anaconda-prompt.png)

After the Anaconda Prompt is installed, we can invoke `conda` commands from within it (although we will not usually be using this application):

![](/img/notes/clis/conda/windows-anaconda-prompt.png)

> NOTE: we don't want to use the Anaconda Prompt, because it is harder to integrate with other tools. Instead, we want to be running our `conda` commands in Git Bash instead (see below).

If Anaconda is installed the way we need it to be, we should ultimately be able to invoke `conda` commands from within the Git Bash console:

![](/img/notes/dev-tools/git-bash/git-bash-where-conda.png)

> NOTE: if Git Bash doesn't recognize `conda` commands ("conda command not found"), you might have to uninstall Anaconda and when re-installing it, make sure to check the "Add Anaconda to my PATH environment variable" option (see installation instructions below).

## Installation

If not yet installed, [download Anaconda Version 3.8](https://www.anaconda.com/download) for either Mac or Windows.

> NOTE: This might take a while, so prefer to do it over a strong WiFi connection. And feel free to ignore any email capture forms which may pop up afterwards.

![](/img/notes/clis/conda/downloading-anaconda-windows.png)

After the download has finished, run the installer program and accept all the default options, except for this important exception to "Add Anaconda to my PATH environment variable", which will allow other programs like Git Bash to recognize the Anaconda installation:

![](/img/notes/clis/conda/anaconda-install-add-to-path.png)


The installation will take a few minutes to complete.

> NOTE: After installing Anaconda on a Mac, you will need to restart your terminal for the changes to take effect.

After the installation is complete, try repeating the detection commands again, as described in the section above.

Once you are able to successfully detect your installation of Anaconda, you are ready to proceed!

## Usage

### The `conda` Utility

#### Listing Environments

View a list of existing virtual environments:

```sh
conda info --envs
```

#### Creating Environments

Create a new virtual environment, and name it something like "my-first-env":

```sh
# conda create -n my-first-env

# FYI: we'll always want to specify the Python version:
conda create -n my-first-env python=3.8
```

#### Activating Existing Environments


Enter into, or "activate", the virtual environment:

```sh
conda activate my-first-env
```

> NOTE: when using conda to activate a virtual environment for the first time, Windows Git Bash users may need to run `conda init bash`, and Mac Zsh profile users may need to run `conda init zsh`, when prompted to do so.

After activating the environment, you should be able to detect and use its installations of Python and Pip (see notes on [the `python` utility](python.md) and [the `pip` utility](pip.md)):

```sh
python --version
pip --version 
pip list
# etc.
```


#### Deactivating Environments

To deactivate the current environment:

```sh
conda deactivate
```

#### Removing Environments

It is possible to delete environments, although this might not be necessary unless trying to free up space on the computer:

```sh
conda env remove -n my-first-env
```

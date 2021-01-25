# Anaconda

Anaconda provides a command-line utility called `conda` for installing and managing different versions of the Python programming language and third-party packages.

> Anaconda is a package manager, an environment manager, a Python/R data science distribution, and a collection of over 1,500+ open source packages. Anaconda is free and easy to install, and it offers free community support. - [Anaconda website](https://docs.anaconda.com/anaconda/)

Resources:

  + https://conda.io/docs/_downloads/conda-cheatsheet.pdf
  + https://conda.io/docs/user-guide/getting-started.html
  + https://conda.io/docs/user-guide/tasks/manage-conda.html
  + https://conda.io/docs/user-guide/tasks/manage-environments.html
  + https://conda.io/docs/user-guide/tasks/manage-pkgs.html#id2
  + https://conda.io/docs/user-guide/tasks/view-command-line-help.html

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

On a Mac, you can invoke these commands directly in the Terminal.

![](/img/notes/clis/conda/mac-terminal.png)

### Detection on Windows

However, on Windows, you can alternatively search for the "Anaconda Prompt" application to know whether or not you have it installed.

![](/img/notes/clis/conda/windows-detecting-anaconda-prompt.png)

After the Anaconda Prompt is installed, you can invoke `conda` commands from within it:

![](/img/notes/clis/conda/windows-anaconda-prompt.png)

If Anaconda is installed the way we need it to be, we should also be able to invoke `conda` commands from within the Git Bash console:

![](/img/notes/dev-tools/git-bash/git-bash-where-conda.png)

If Git Bash doesn't recognize your `conda` commands, you might have to uninstall Anaconda and when re-installing it, make sure to check the "Add Anaconda to my PATH environment variable" option (see installation instructions below).

## Installation

If not yet installed, [download Anaconda Version 3.7](https://www.anaconda.com/download) for either Mac or Windows.

> NOTE: This might take a while, so prefer to do it over a strong WiFi connection. And feel free to ignore any email capture forms which may pop up afterwards.

![](/img/notes/clis/conda/downloading-anaconda-windows.png)

After the download has finished, run the installer program and accept all the default options, except for this important exception to "Add Anaconda to my PATH environment variable", which will allow other programs like Git Bash to recognize the Anaconda installation:

![](/img/notes/clis/conda/anaconda-install-add-to-path.png)


The installation will take a few minutes to complete.

> NOTE: After installing Anaconda on a Mac, you will need to restart your terminal for the changes to take effect.

After the installation is complete, try repeating the detection commands again, as described in the section above.

Once you are able to successfully detect your installation of Anaconda, you are ready to proceed!

> NOTE: On Windows, you may need to run the command `conda init bash` when prompted to do so, in order to activate a virtual environment for the first time.

## Usage

### The `conda` Utility

When activating Anaconda virtual environments and issuing project-specific `conda` commands, we generally want to do so within that project's directory. So let's take a moment to create a new project directory now, then navigate there from the command line:

```sh
cd path/to/my-first-project/ # where path/to/my-first-project/ is the actual path of your desired project directory
```

All subsequent commands assume you are running them from within the project's root directory.

#### Managing Virtual Environments

View a list of existing virtual environments:

```sh
conda env list
```

Create a new virtual environment, and name it something like "my-first-env":

```sh
conda create -n my-first-env

# FYI: you can specify a Python version for your new environment with...
# conda create -n my-first-env python=3.8

# FYI: you can delete any environment with...
# conda env remove -n my-first-env
```

Enter into, or "activate", the virtual environment:

```sh
conda activate my-first-env

# FYI: to deactivate...
# conda deactivate
```

Once activating the environment, you should be able to detect and use its installations of Python and Pip:

```sh
which python #> /anaconda3/envs/my-first-env/bin/python
python --version #> Python 3.6.7 :: Anaconda, Inc.

which pip #> /anaconda3/envs/my-first-env/bin/pip
pip --version #> pip 18.1 from /anaconda3/envs/my-first-env/lib/python3.6/site-packages/pip (python 3.6)
```

![](/img/notes/clis/conda/managing-envs.png)


For more information, see notes on [the `python` utility](python.md) and [the `pip` utility](pip.md).

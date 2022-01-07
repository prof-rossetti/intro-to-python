
# Troubleshooting Python Applications

> See the ["Run the App" Exercise](README.md) description.

Here are some common errors you may run into while trying to run Python apps locally.

## Bad Anaconda Installation

If you try to run a `conda` command, and you see an error like "conda: command not found", it means there's something wrong with your installation.

It's OK. Feel free to reach out to an instructor and ask for help. See also these [known troubleshooting remedies](https://github.com/prof-rossetti/intro-to-python/issues/13).

## Can't Install Packages / Forgot to Navigate to the Local Repo

If the `pip install -r requirements.txt` command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the "requirements.txt" file exists (see the initial `cd` step to navigate into the repository's root directory).

## Forgot to Install Packages

If you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip install -r requirements.txt` command from the repository's root directory to ensure that package has been installed into the virtual environment, before trying to run the app again.

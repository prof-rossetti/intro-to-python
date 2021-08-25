# "Run the App" Exercise

## Prerequisites

  1. Do the [Version Control Exercise](/exercises/hello-world/version-control.md).
  2. Read up about [Environment Variables](/notes/environment-variables.md), specifically setting via the ".env" file approach.

## Learning Objectives

In this exercise, we'll learn how to install, configure, and run an existing Python application. We'll focus on environment management, package management, and setting environment variables.

## Instructions

  1. Visit the Professor's ["My First Python App" repository](https://github.com/prof-rossetti/my-first-python-app), which contains a simple command-line application. We'll refer to the Professor's repository as the "upstream repository".
  2. Click "Fork" to copy the repo under your own control. We'll refer to your forked copy as the "remote fork", otherwise known as the "origin repository".
  3. Follow the instructions in the repository's "README.md" file to install, setup and run the Python code contained inside:
     1. Use your Git client to "clone" (download) the remote fork onto your local machine, perhaps onto the Desktop. We'll refer to this as the "local repository".
     2. Use the command-line to navigate into the local repository.
     3. Use the `conda` utility to create a new virtual environment with the specified version of Python, then activate it.
     4. Use the `pip` utility to install any required third-party packages specified in the repo's "requirements.txt" file.
     5. Use a ".env" file approach to set an environment variable to customize the user name.
     6. Use the `python` utility to run the Python file(s).

## Success Criteria

Once you have run the app, you will have succeeded. Repeat steps 3.5 and 3.6 (change the environment variable value and re-run the program) at least one more time for good measure.

## Further Exploration (Optional)

Are you ready to run a real app that actually does something? Try the professor's ["Daily Briefings" repository](https://github.com/prof-rossetti/daily-briefings-py), which contains a command-line application for fetching weather forecasts, and sending weather forecast emails. 

Just like before, we'll fork and clone the repo, then start to follow it's README instructions. Follow the Installation instructions, using a process like the one described above.

Your main goal is to then run the "Weather Service" Python script (does not require any Configuration steps - can skip that section for now). If successful, you should see weather forecast results in the terminal.

After that, your stretch goal is to follow the Configuration instructions (related to signing up for a Sendgrid account and configuring environment variables), then run the "Email Service" and "Daily Briefing" Python scripts. If successful, you should see weather forecast results sent to your email address.

Ignore the sections about Testing and Deploying. They're a little out of scope for us right now.

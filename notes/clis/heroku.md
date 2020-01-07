# Heroku, and the `heroku` Utility

> Prerequisite: [Remote Servers](/notes/hardware/servers.md)

> Heroku is a cloud platform that lets companies build, deliver, monitor and scale apps — we're the fastest way to go from idea to URL, bypassing all those infrastructure headaches. - [Heroku website](https://www.heroku.com/what)

Heroku provides developers with the ability to configure and manage remote servers. Each Heroku server has its own unique HTTP address. Users usually access the server by visiting its address in a web browser, whereas developers and administrators usually access the server from the command-line over what is usually an HTTPS or SSH connection.

Heroku servers can host applications written in popular programming languages like Python, Ruby, Node.js, and more.

In addition to using the online platform to interface with Heroku, we will use the [Heroku command-line utility (CLI)](https://devcenter.heroku.com/articles/heroku-cli).

References:

  + [Heroku CLI Reference](https://devcenter.heroku.com/categories/command-line)
  + [Heroku CLI Source Code](https://github.com/heroku/cli)
  + [Heroku CLI Installation Guide](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
  + [Heroku for "Pythonic apps and APIs"](https://www.heroku.com/python)
  + [Heroku Python Support](https://devcenter.heroku.com/articles/python-support)
  + [Heroku Getting Started with Python](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)

## Prerequisites

Before you can use the Heroku CLI, you'll need a Heroku account.

Take a moment to [register](https://signup.heroku.com/) for a new account unless you already have one.

After registering, make sure to confirm your account by clicking a confirmation link the confirmation email sent to you by Heroku.

> Security Alert: consider eventually enabling multi-factor authentication on your Heroku account to keep your account and your servers safe from intrusion. Don't worry about doing this now if you don't feel like it, but take a moment to do so when you have time.

> NOTE: In order to provision some services like databases and email, you may need to provide Heroku with billing information. You can expect to not be charged as long as you are using the free version of each of these services. Just be aware.


## Installation

Check to see if the Heroku CLI is already installed, and if so, what version:

```sh
# Mac Terminal
which heroku #> /usr/local/bin/heroku

# Windows Command Prompt
where heroku #> ...
```

```sh
heroku --version #> heroku/7.4.1 darwin-x64 node-v10.4.1
```

If it is not installed, follow the [official installation guide](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) for operating system-specific instructions. As usual, Mac users are able and encouraged to install via [Homebrew](/notes/clis/brew.md) (`brew tap heroku/brew && brew install heroku`). Windows users should install with all default preferences, including making sure "Add PATH to Heroku" is checked.

## Authentication

After installing the Heroku CLI, log-in to Heroku from the command-line using your account credentials:

```sh
heroku login # this will prompt you for a username and password
```




























## Usage

List applications:

```sh
heroku apps
```

> NOTE, for other commands below, you can specify which app to run the command against by providing the `-a` flag followed by the app name (e.g. `-a my-app-name`).

### Generation

Create a Heroku application server (from within the root directory of an existing project):

```sh
heroku create
# or optionally specify a name, like:
# heroku create my-app-name
```

Or create a new application via the Heroku online console, and note its name (e.g. "my-app-name"), and associate an existing repository with it (from within the root directory of an existing project):

```sh
heroku git:remote -a my-app-name
```

### Configuration

Get environment variables currently set on the server:

```sh
heroku config -a my-app-name
```

Set environment variables on the server:

```sh
heroku config:set MY_SECRET_MESSAGE="abc123" -a my-app-name
```

### Deploying

Deploy the application's source code to the application server:

```` sh
git push heroku master
# or if you need to deploy from a different branch:
# git push heroku mybranch:master
````

Visit the application in a browser and note its URL for future reference:

```` sh
heroku open -a my-app-name
````

Check your application's server logs:

```` sh
heroku logs -a my-app-name
````

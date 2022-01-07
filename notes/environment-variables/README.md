# Environment Variables

**Environment variables** allow developers to customize the environment in which an application is operating.

## Benefits

### Security

Sometimes applications need to reference secret passwords, tokens, and other values. This is especially the case when the app is authenticating to some other service on behalf of a given user.

But hard-coding these sensitive values into a program's source code would be irresponsible from a security standpoint, especially when sharing the source code online. You don't want your passwords on GitHub for everyone to see.

Environment variables provide a way of separating these secret values from a program's source code.

### Collaboration and Customization

Sometimes developers need to run an application in different environments. For example, two developers may want to use the same program to download their respective social media posts from an API.

But each developer has their own private API key which provides access to their own private social media posts. It would be ineffective for them to use the exact same source code, and inefficient to maintain two slightly different versions of the application's source code.

Environment variables allow developers to share the same source code while specifying different values at run-time.

### Testing and Delivery

Environment variables allow developers to specify customized environments in which to develop, test and deliver their application.

Environment variable customization allows an application to perform differently in a "test" environment than it would in a user-facing "production" environment. For example, developers can use the application to manipulate example data in a "test" environment without affecting real user data in the "production" environment.

## Usage

We can "set" environment variables, and later "get" their values, using a variety of strategies.

Environment variables can be set ["globally"](/accessing-globally.md), in which case they are accessible by any program running on that given computer. Or they can be set "locally", in which case they are only accessible by programs located in a specific directory.

The most common way to set environment variables is by passing them directly from the command-line. But when the number of environment variables grows, it becomes easier to store them all in a single ".env" file and use the "dotenv" approach.

### Setting Environment Variables via Command Line

To set a script-specific environment variable on either Mac or Windows, its possible to prefix the environment variable before invoking your Python script. For example:

```sh
MY_SECRET_MESSAGE="SecretPassword123" python path/to/my_script.py
```

To access environment variables from within a Python program, use [the `os` module](/notes/python/modules/os.md#environment-variables).

### Setting Environment Variables via "Dotenv" Approach

To set project-specific local environment variables on either Mac or Windows, consider using the "dotenv" approach.

In this approach, we create a special file named ".env" in the project's root directory, and place inside any number of environment variable declarations, each on their own line.

Example ".env" file contents:

```sh
#
# this is a special file called ".env" which is stored in your project's root directory
#

MY_VAR=5
MY_SECRET_MESSAGE="SecretPassword123"
MY_API_KEY="abc123"
```

To access these environment variables from a Python program, we first use [the `dotenv` package](/notes/python/packages/dotenv.md) to load them into the program's environment, then we can access them using [the `os` module](/notes/python/modules/os.md#environment-variables) as usual.

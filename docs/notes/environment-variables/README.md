# Environment Variables

**Environment variables** allow developers to customize the environment in which an application is operating, by passing certain values at runtime. This allows the program to behave differently, depending on what values have been specified.

Environment variables are like an indirect way of providing inputs to a program, without hard-coding them in the program, and without asking for a manual user input.

## Benefits

Environment variables provide benefits in terms of security and customization, and can help enable process automation.

### Security Benefits

Sometimes applications need to use secret passwords, tokens, and other credentials to interface with external services and APIs. This is especially the case when the app is authenticating to a third-party service on behalf of a given user. For example, consider an application that automatically logs in to a user's email inbox to check for unread messages.

Hard-coding secret credentials like email passwords into the program's source code would be irresponsible from a security standpoint, especially when sharing the source code online - we want to avoid publishing secret passwords to GitHub for people like hackers to see and exploit.

So to keep the secret credentials separate from the source code, we can pass them to the program as environment variables at runtime. This way, the program's code only contains a reference to these variables, but not their values.


### Collaboration Benefits


Environment variables allow multiple developers to share the same codebase, without keeping their own slightly different copies.

Consider the case of two developers using the same program to download their own respective social media posts. This requires them to specify their own respective credentials (most likely in the form of API keys).

If each developer hard-coded their own credentials into the application's source code, it would require them to keep two slightly different versions of the source code. This would lead to to increased maintenance costs, complexities, and inefficiencies.

Instead, by passing their own environment variables at runtime, multiple developers can share the same source code. This is a much more maintainable and efficient solution than keeping separate copies. And allows hundreds or thousands of developers to share the same source code.







## Usage

We can "set" environment variables, and later "get" their values, using a variety of strategies.

Environment variables can be set ["globally"](/accessing-globally.md), in which case they are accessible by any program running on that given computer. Or they can be set "locally", in which case they are only accessible by programs located in a specific directory.

The most common way to set environment variables is by passing them directly from the command-line. But when the number of environment variables grows, it becomes easier to store them all in a single ".env" file and use the "dotenv" approach.

### Setting Environment Variables via Command Line

To set a script-specific environment variable on either Mac or Windows, its possible to prefix the environment variable before invoking your Python script. For example:

```sh
MY_VAR=5 MY_SECRET_MESSAGE="SecretPassword123" python path/to/my_script.py
```

To access environment variables from within a Python program, use [the `os` module](./../python/modules/os.md#environment-variables).

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

To access these environment variables from a Python program, we first use [the `dotenv` package](./../python/packages/dotenv.md) to load them into the program's environment, then we can access them using [the `os` module](./../python/modules/os.md#environment-variables) as usual.

It is important for security reasons to ensure the ".env" file is ignored from version control, using the ".gitignore" file. We should not see the ".env" file on GitHub, but rather each developer will need to create their own local copy.

# "Freestyle" Project - Implementation (TECH 2335 Version)

> See: [The "Freestyle" Project](README.md)

## Learning Objectives

  1. Create a tool to address user needs and solve a business problem.
  2. Practice implementing software according to a plan.
  3. Practice investigating and leveraging third-party services and Python packages to speed development and enhance capabilities.

## Instructions

After defining the requirements and objectives of your proposed solution, and after investigating its technical feasibility, it's time to write (or continue writing) Python code to implement some or all of the application's desired functionality.

The implementation should adhere to the requirements below.

### Documentation Requirements

Your project repository should contain a "README.md" file. The README file should provide instructions to help someone else install, setup, run, and test your program. This includes:
  + instructions for creating and activating a virtual environment, most likely using Anaconda
  + instructions for installing package dependencies, most likely using Pip
  + instructions for obtaining and setting environment variables, as necessary

As you document for your application, strive to make it as easy as possible for someone else (or even your future self) to install it, use it, and understand what it is about.

Also, your codebase should be reasonably documented with comments as necessary, to help others (and your future self) understand the code.

### Dev Process Requirements

Iteratively develop your project using version control practices. Save new versions of your source code as you reach key milestones.

If working in a group, each group member should make significant contributions to the application's source code!

### Security Requirements

If your program requires sensitive information like secret passwords, API keys, or other credentials, those secret values should absolutely not be included in the source code or its revision history. Use environment variables in conjunction with a ".env" file and a ".gitignore" file to hide secret credentials from version control. If you need help, consult the [`dotenv` package notes](/notes/python/packages/dotenv.md).

### Quality Requirements

Scan your application's codebase for duplication of terms, and refactor (using custom functions as necessary) to simplify the code and make it easier to maintain.

Optionally integrate your GitHub repository with a service like [Code Climate](https://codeclimate.com/) to provide automated code quality checks.

### Licensing Requirements

Choose a software license, and include a corresponding file called "LICENSE" or "LICENSE.md" in the root directory of your repository. If you need help choosing a license, see the [software licensing notes](/notes/software/licensing.md).

## Submission Instructions

Submit the designated Google Form before the designated date, providing the URL to your GitHub repository, and any others (like a web application URL) as desired.

## Evaluation

Project implementations will be evaluated according to the requirements set forth above, as summarized by the rubric below:

Category | Requirement | Weight
--- | --- | ---
Uniqueness and Individuality | Exhibits creativity, and a unique set of functionality | 20%
User Experience | Provides a simple, pleasant, and intuitive experience for the user, with clear usage instructions, and free of idiosyncrasies or errors | 15%
Documentation | Contains a comprehensive and well-formatted README file | 20%
Licensing | Contains an appropriate LICENSE file | 5%
Security | Excludes sensitive information and credentials; protects user data as necessary | 15%
Quality | Simplified to remove or minimize code duplication | 5%
Dev Process | Submitted via Git repository which reflects an incremental revision history and contributions from all team members | 20%

This rubric is tentative, and may be subject to slight adjustments during the grading process.

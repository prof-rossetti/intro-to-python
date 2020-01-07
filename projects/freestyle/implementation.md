# "Freestyle" Project Implementation

> Prerequisites:
>   + [The "Freestyle" Project Proposal](/projects/freestyle/proposal.md)
>   + [The "Freestyle" Project Plan](/projects/freestyle/plan.md), ideally but not necessarily completed
>   + [Software Maintenance and Quality Control](/units/unit-8.md) (optional)
>   + ["Continuous Integration 1, 2, 3" Exercise](/exercises/ci-123/README.md) (optional)

## Learning Objectives

  1. Create a tool to address user needs and solve a business problem.
  2. Practice implementing software functionality as described in a planning and requirements document.
  3. Leverage built-in Python modules and third-party Python packages to speed development and enhance capabilities.
  4. Incorporate version control and quality control practices into your development process.

## Instructions

After [researching the technical feasibility](proposal.md) of your proposed solution and [defining project requirements and making a development plan](plan.md), it's time to write (or continue writing) Python code to implement some or all of the application's desired functionality.

In addition to addressing your system's written functionality requirements, the implementation should adhere to the requirements below.

### Documentation Requirements

Your project repository should contain a "README.md" file. The README file should provide instructions to help someone else install, setup, run, and test your program. This includes instructions for creating and activating a virtual environment, most likely using Anaconda. It also includes instructions for installing package dependencies, most likely using Pip. It also includes instructions for setting environment variables as necessary, using a "dotenv" approach.

As you document for your application, strive to make it as easy as possible for someone else (or even your future self) to install it, use it, and understand what it is about.

Also, your codebase should be reasonably organized and documented with comments as necessary, to help others (and your future self) understand the code.

### Licensing Requirements

[Choose a software license](/notes/software/licensing.md), and include a corresponding file called "LICENSE" or "LICENSE.md" in the root directory of your repository.

### Security Requirements

If your program requires sensitive information like secret passwords, API keys, or other credentials, those secret values should absolutely not be included in the source code or its revision history.

Use environment variables in conjunction with a ".env" file and a ".gitignore" file to read sensitive information from the software's operating environment while excluding them from the source code.

### Quality Requirements

#### Code Simplification

Scan your application's codebase for duplication of terms, and refactor (using custom functions as necessary) to remove that duplication.

#### Automated Tests

> FYI: this is optional, for extra credit

Implement automated tests using the Pytest package.

As you think about ways to test your application, consider asking yourself questions like the following:

  + As I was developing this application, what manual steps did I take to ensure it was functioning properly? Can I automate those manual processes?
  + Is it possible for the application to receive user inputs that are unexpected or invalid? How should the application handle various invalid inputs?
  + How should the application's component functions perform given various inputs, whether valid or invalid?
  + Are there any functions or sections of the code which aren't easy to read or understand? Is there a way to use examples to communicate what is supposed to happen?
  + If the application processes data from the Internet: Is there a way to test the application's functionality without making any additional network requests?
  + If the application processes data from a CSV file or database: Is there a way to test the application's functionality without affecting the development environment datastore?

#### Continuous Integration

> FYI: this is optional, for extra credit

Configure your GitHub repository to integrate with a continuous integration (CI) platform like Travis CI, such that automated tests are run on a CI server whenever new code is pushed to the remote GitHub repository.

### Dev Process Requirements

Iteratively develop your project using version control practices. Save new versions of your source code as you reach key milestones.

Optionally: Instead of committing your versions directly to the "master" branch, use [branch operations](/notes/clis/git.md#branch-operations) to develop logically-related updates on a separate branch, then push that branch to GitHub in order to create a Pull Request, where you can further review your proposed changes and allow automated tests to run and pass on the CI server before finally "merging" the code back into the master branch.

If working in a group, each group member must make significant contributions to the application's source code! Any group member not committing significant portions of the code may be subject to deductions.





## Submission Instructions

To submit:

  1. Push your local project repository to GitHub, so you can visit your remote project repository at a URL like `https://github.com/YOUR_USERNAME/YOUR_PROJECT`
  2. Fork the ["upstream" course repository](https://github.com/prof-rossetti/nyu-info-2335-201905) (or refresh your existing fork)
  3. Update the ["submissions.csv"](submissions.csv) file in your remote fork of the course repository to include an entry linking to your remote project repository URL
  4. Finally, submit a Pull Request for the changes in your remote fork of the course repository to be accepted back into the "upstream" course repository

### Group Project Submission

For groups with multiple users, your repository can be owned by one of the members, or a shared organization. And your entry in the "submissions.csv" file should resemble the following (including the quotes):

    github_username, repository_url
    "user1, user2, user3", https://github.com/USER_OR_ORG_NAME/REPO_NAME

## Evaluation

Implementations will be evaluated based on the criteria below:

Category | Requirement | Weight
--- | --- | ---
Satisfies Proposed Requirements | Addresses a problem discussed in the accompanying requirements document, in a manner generally consistent with the plan discussed in that document | 10%
Uniqueness and Individuality | Exhibits creativity, and a unique set of functionality | 10%
User Experience | Provides a simple, pleasant, and intuitive experience for the user, with clear usage instructions, and free of idiosyncrasies or errors | 15%
Documentation | Contains a comprehensive README file | 20%
Licensing | Contains an appropriate LICENSE file | 5%
Security | Excludes sensitive information and credentials | 12.5%
Quality | Simplified to remove or minimize code duplication | 7.5%
Dev Process | Submitted via Git repository which reflects an incremental revision history, branch operations, a Pull Request workflow, and contributions from all team members | 20%

Bonus / Optional Extra Credit:

Category | Requirement | Weight
--- | --- | ---
Quality | Contains relevant automated tests | 10% BONUS
Quality | Deployed to a continuous integration (CI) server | 5% BONUS


This rubric is tentative, and may be subject to slight adjustments during the grading process.

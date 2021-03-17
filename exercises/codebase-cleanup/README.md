# "Codebase Cleanup" Assignment

## Learning Objectives

  + Develop new features in a controlled manner, by adopting Git branch operations and a Pull Request workflow.
  + Practice collaborating with other developers and conducting Peer Reviews.
  + Simplify an existing codebase to decrease future maintenance costs, and reduce errors.
  + Write and execute automated tests to verify code is functioning as expected.
  + Incorporate automated checks (like running tests on a Continuous Integration server), to determine whether code updates are ready to be merged / adopted.

## Instructions

The [Codebase Cleanup Repo](https://github.com/prof-rossetti/codebase-cleanup-2021) contains some abbreviated example code related to some projects we have worked on. But there are few opportunities for us to improve the quality of this code.

First, fork the repo under your own control. Then integrate your forked repo with the [Code Climate](/notes/devtools/code-climate.md) platform, and the [Travis CI](/notes/devtools/travis-ci.md) platform.

Use a Pull Request workflow to complete each of the challenges below. Optionally invite a friend to collaborate on your repo, and perform a code review on at least one of your Pull Requests.

> NOTE: for Pull Requests, create them against your fork ("origin" repo), NOT the professor's "upstream" repo.

## Instructions

For Basic Requirements, do the "Game" and "Shopping" challenges. For further exploration, also do the "Robo" challenges.

### Game Improvements

User Feedback: "Sometimes it gets the winner wrong!"

Developer Maintenance Steps:

  1. Refactor duplicate code relating to the valid options ("rock", "paper", and "scissors").
  2. Notice Code Climate says the existing winner determination logic is "complex". Refactor the complex logic to use less computational steps and also make it easier to read. Also notice the existing logic produces some inaccurate outcomes, and update the logic to produce accurate outcomes.
  3. Test that the winner determination logic produces accurate outcomes. Move the logic into a stand-alone function called `determine_winner()` that can be invoked and tested in isolation, separate from any user inputs.

### Shopping Improvements

User Feedback: "The receipt file has the wrong total amount due!"

Developer Maintenance Steps:

  1. Refactor duplicate code relating to the price-formatting logic. Notice and fix any discrepancies in this logic.
  2. Refactor duplicate code relating to the receipt contents. Ensure the printed receipt has the same contents as the receipt file.
  3. Test the program's price-formatting logic produces desired results. Move the logic into a stand-alone function called `format_usd()` that can be invoked and tested in isolation, WITHOUT any user inputs.
  4. Test the program's ability to lookup matching products. Move the product lookup logic into a stand-alone function called `find_product()` that can be invoked and tested in isolation, WITHOUT any user inputs. Use the mock products CSV file data to perform this test.

### Robo Improvements (Further Exploration)

User Feedback: "The chart shows prices in reverse!"

Developer Maintenance Steps:

  1. Test the program's ability to request data for a given stock symbol, and that the resulting response data is structured in the expected format. HINT: since the response data will be dynamic, we can focus on some consistent parts of the response data, like ensuring certain keys like "Meta Data" and "Time Series (Daily)" exist, and checking the symbol we requested is contained in the "Meta Data".
  2. Test the program's ability to convert the response data into a more usable format (for example a list of dictionaries or Pandas DataFrame). Use one or more valid mock responses to perform this test, WITHOUT making any network requests.
  3. Test the program's chart displays prices in the proper order. HINT: we can just do a test about some aspects of the DataFrame that gets charted.
  4. Ensure any tests that make web requests are skipped from being run on the CI server.
  5. Refactor the `format_usd` function from the shopping script, moving it into the init file, and importing it from the init file into both the shopping and robo scripts.


> FYI: one philosophy when testing is to minimize the number of web requests that need to be made. That's one reason for using mock data. The other reason for mock data is for testing certain edge-cases.

## Evaluation

When you submit this project, you'll submit links to your repository on GitHub, Code Climate, and Travis CI. And evaluators will look at all these services when grading your project.

The project will be evaluated according to the instructions above, as summarized in the table below:

Category | Description | Weight
--- | --- | ---
Pull Request Workflow | At least one or two Pull Requests used during development. | 20%
Simplification | Code is reasonably well organized and simplified. | 20%
Documentation | At least a few functions are documented via "docstring" comments, as appropriate. | 20%
Automated Testing | Tests directly invoke functions from the source code to verify the program behaves as expected. | 30%
Continuous Integration | Tests have been run and passed on a CI server at least once, ideally as part of the Pull Request workflow. | 10%
Code Quality | The Code Climate service has been integrated into the Pull Request workflow to provide automated code quality checks. | 10%
Peer Reviews | A peer has provided an unofficial comment or official review as part of the Pull Request workflow | 0% (OPTIONAL)

> NOTE: for this project, evaluators will be reading your code and inspecting your repo across the various platforms (Github, Code Climate Travis CI), but not necessarily running or testing your application code directly.

# "Codebase Cleanup" Assignment

## Learning Objectives

  + Develop new features in a controlled manner, by adopting Git branch operations and a Pull Request workflow.
  + Practice collaborating with other developers and conducting Peer Reviews.
  + Simplify an existing codebase to decrease future maintenance costs, and reduce errors.
  + Write and execute automated tests to verify code is functioning as expected.
  + Incorporate automated checks (like running tests on a Continuous Integration server), to determine whether code updates are ready to be merged / adopted.

## Instructions

The [Codebase Cleanup Repo](https://github.com/prof-rossetti/codebase-cleanup-2021) contains some abbreviated example code related to some projects we have worked on. But there are few opportunities for us to improve the quality of this code.

First, fork the repo under your own control. Then integrate it with the Code Climate platform, and the Travis CI platform.

Use a Pull Request workflow to complete each of the challenges below. Optionally invite a friend to collaborate on your repo, and perform a code review on at least one of your Pull Requests.

For Basic Requirements, do the "Game" and "Shopping" challenges. For further exploration, do the "Robo" challenges.

## Game Improvements

  1. Refactor duplicate code relating to the valid options ("rock", "paper", and "scissors").
  2. Notice Code Climate says the existing winner determination logic is "complex". Refactor the complex logic to use less computational steps and also make it easier to read. Also notice this logic produces some inaccurate outcomes, and update the logic to produce accurate outcomes.
  3. Test that the winner determination logic produces accurate outcomes. Move the logic into a stand-alone function called `determine_winner()` that can be invoked and tested in isolation, separate from any user inputs.

## Shopping Improvements

  1. Refactor duplicate code relating to the price-formatting logic. Notice and fix any discrepancies in this logic.
  2. Refactor duplicate code relating to the receipt contents. Ensure the printed receipt has the same contents as the receipt file.
  3. Test the program's price-formatting logic produces desired results. Move the logic into a stand-alone function called `format_usd()` that can be invoked and tested in isolation.
  4. Test the program's ability to lookup matching products. Move the product lookup logic into a stand-alone function called `find_product()` that can be invoked and tested in isolation. Use the mock products CSV file data to perform this test.

## Robo Improvements (Further Exploration)

  1. Test the program's ability to request data for a given stock symbol, and that the resulting response data is structured in the expected format. HINT: since the response data will be dynamic, we can focus on some consistent parts of the response data, like checking the symbol we requested is contained in the "Meta Data" attribute. We could also test to ensure certain keys like "Meta Data" and "Time Series (Daily)" are keys in the response data.
  2. Test the program's ability to convert the response data into a more usable format (for example a list of dictionaries or Pandas DataFrame). Use one or more valid mock responses to perform this test.
  3. Test the program's chart displays prices in the proper order. HINT: we can just do a test about some aspects of the DataFrame that gets charted.
  4. Ensure any tests that make web requests are skipped from being run on the CI server.


## Evaluation

Each of the two projects will comprise half of the weight for each of the categories below:

Category | Description | Weight
--- | --- | ---
Pull Request Workflow | At least one or two Pull Requests used during development. | 20%
Simplification | Code is reasonably well organized and simplified. | 20%
Documentation | At least a few functions are documented via "docstring" comments, as appropriate. | 20%
Automated Testing | Tests directly invoke functions from the source code to verify the program behaves as expected. | 30%
Continuous Integration | Tests have been run and passed on a CI server at least once, ideally as part of the Pull Request workflow. | 10%
Code Quality | The Code Climate service has been integrated into the Pull Request workflow to provide automated code quality checks. | 10%
Peer Reviews | A peer has provided an unofficial comment or official review as part of the Pull Request workflow | 0% (OPTIONAL)

> NOTE: you'll be evaluated according to the rubric above, not any previous functionality requirements. Instructors will be reading your code and running your tests and inspecting your GitHub Pull Request history, but not necessarily running your application code directly.

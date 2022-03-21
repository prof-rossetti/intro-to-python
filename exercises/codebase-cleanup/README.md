# "Codebase Cleanup" Exercise

## Learning Objectives

  + Develop new features in a controlled manner, by adopting Git branch operations and a Pull Request workflow.
  + Practice collaborating with other developers and conducting Peer Reviews.
  + Simplify an existing codebase to decrease future maintenance costs, and reduce errors.
  + Write and execute automated tests to verify code is functioning as expected.
  + Incorporate automated checks (like running tests on a Continuous Integration server), to determine whether code updates are ready to be merged / adopted.

## Instructions


First, make a copy of the professor's ["codebase-cleanup-template" repo](https://github.com/prof-rossetti/codebase-cleanup-template), then continue to follow the "Repository Setup" instructions below.

After setting up the repo and updating your remote repo, use a Pull Request workflow to complete each of the "Challenges" below. Optionally invite a friend to collaborate on your repo, and perform a code review on at least one of your Pull Requests.

## Repository Setup

Create a new repo called something like "codebase-cleanup-2022". During this process, add a "README.md" file and a Python-flavored ".gitignore file.

Configure the repo to integrate with the "Python application" GitHub Action. This is for "Continuous Integration" purposes, which we will talk about later. This step should add a ".github/workflows/python-app.yml" file [like this one](starter/python-app.yml) to your repo.

Integrate your repo with the [Code Climate](/notes/devtools/code-climate.md) platform, which will provide automated quality and complexity assessments. Login to Code Climate (Quality Service) via your GitHub account. Visit the Code Climate dashboard, and click "Add a repository" and choose the repo you just created. Through the repo's settings on Code Climate, enable "Summary Comments" and/or "Inline Issue Comments". Optionally explore the python-related plugins, or add a predefined "" file [like this one](starter/.codeclimate.yml) to your repo.

Clone the repo to download it onto your computer. Navigate there from the command line, and open in a text editor of choice. For example:

```sh
cd ~/Desktop
git clone git@github.com:YOUR_USERNAME/codebase-cleanup-2022.git
cd codebase-cleanup-2022/
code .
```

As necessary, add an "app" directory with files: "game.py", "groceries.py", "crypto.py", "stocks.py", "crypto.py", "unemployment.py", and "email_me.py", respectively, with contents copied from [this starter code](starter/app).

Add an empty "requirements.txt" file to the repo's root directory, with contents [like this](starter/requirements.txt). When new application code requires installation of new packages, we will update the file to include the names of those required packages. For now, save the file, make a commit, and push the changes up to the remote repo.



## Challenges

### Game Improvements

File(s): "game.py"

User Feedback: "Sometimes it gets the winner wrong!"

Developer Maintenance Steps:

  1. Refactor duplicate code related to the valid options ("rock", "paper", and "scissors").
  2. Notice Code Climate says the existing winner determination logic is "complex". Refactor the complex logic to use less computational steps and also make it easier to read. Also notice the existing logic produces some inaccurate outcomes, and update the logic to produce accurate outcomes.
  3. Test that the winner determination logic produces accurate outcomes. The function should accept the user choice and the computer choice as input parameters, and should return the value of the winning choice. Move the logic into a stand-alone function called `determine_winner()` that can be invoked and tested in isolation, separate from any user inputs.
  4. Document the winner determination function with a docstring.

### Groceries Inventory Improvements

File(s): "groceries.py"

User Feedback: "The average price is wrong!"

Developer Maintenance Steps:

  1. Refactor duplicate code related to the CSV filepath compilation.
  2. Reduce complexity by minimizing the number of loops this script performs.
  3. Refactor duplicate code related to the price-formatting logic.
  4. Test the program's price-formatting logic produces desired results. Move the logic into a stand-alone function called something like `to_usd()` or `format_usd()` that can be invoked and tested in isolation, separate from any user inputs.
  5. Document the price formatting function with a docstring.

Optional, Advanced Testing Considerations:

  6. Test the program's ability to calculate the average product price. Move the average price calculation logic into a stand-alone function called something like `calculate_avg_price()` that can be invoked and tested in isolation. The function should accept any list or DataFrame of products as its input parameter, and should return the average price as a float(unformatted). Use the mock products CSV file data to perform this test.

### Unemployment Report Improvements

File(s): "unemployment.py", "stocks.py", "crypto.py"

User Feedback: "The unemployment chart is messed up!"

Developer Maintenance Steps:

  1. Refactor duplicate code related to the price-formatting logic (across all files in the repo, including the "groceries.py" file). Move the common formatter function to a separate file called something like "utils.py" or "decorators.py" or "formatters.py". Then import this shared function into all the files that need it. NOTE: you may need to add the infamous "init" file to the "app" directory, and you may need to use the infamous "main" conditional in any files being imported from.

Optional, Advanced Testing Considerations:

  1. Test the program's ability to request data for a given stock symbol, and that the resulting response data is structured in the expected format. HINT: since the response data will be dynamic, we can focus on some consistent parts of the response data, like ensuring certain keys like "Meta Data" and "Time Series (Daily)" exist, and checking the symbol we requested is contained in the "Meta Data". Optionally mock the response to use the example data.
  2. Test the program's ability to convert the response data into a more usable format (for example a list of dictionaries or Pandas DataFrame). Use one or more valid mock responses to perform this test, without making any network requests.
  3. Test the program's chart displays prices in the proper order. HINT: we can just do a test about some aspects of the DataFrame that gets charted.
  4. Ensure any tests that make web requests are skipped from being run on the CI server.


> FYI: our goal is to minimize the number of web requests that need to be made when testing. We can use mock data and/or pytest fixtures for this.



## Evaluation

The project will be evaluated according to the instructions above, as summarized in the table below:

Category | Description | Weight
--- | --- | ---
Pull Request Workflow | At least one or two Pull Requests used during development. | 20%
Simplification | Code is reasonably well organized and simplified. | 20%
Documentation | At least a few functions are documented via "docstring" comments, as appropriate. | 20%
Automated Testing | Tests directly invoke functions from the source code to verify the program behaves as expected. | 25%
Continuous Integration | Tests have been run and passed on a CI server at least once, ideally as part of the Pull Request workflow. | 7.5%
Code Quality | The Code Climate service has been integrated into the Pull Request workflow to provide automated code quality checks. | 7.5%
Peer Reviews | A peer has provided an unofficial comment or official review as part of the Pull Request workflow | 0% (OPTIONAL)

> NOTE: for this project, evaluators will be reading your code and inspecting your repo across the various platforms (Github, Code Climate, etc.), but not necessarily running or testing your application code directly.

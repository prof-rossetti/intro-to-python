# "Codebase Cleanup" Exercise

## Learning Objectives

  + Develop new features in a controlled manner, by adopting Git branch operations and a Pull Request workflow.
  + Practice collaborating with other developers and conducting Peer Reviews.
  + Simplify an existing codebase to decrease future maintenance costs, and reduce errors.
  + Write and execute automated tests to verify code is functioning as expected.
  + Incorporate automated checks (like running tests on a Continuous Integration server), to determine whether code updates are ready to be merged / adopted.

## Prerequisites
  
  + Read the [Unit 8](/units/unit-8.md) Notes
  + Sign up for the [Code Climate (Quality) service](https://codeclimate.com/quality/), and login with your GitHub account, and "install" Code Climate to access your GitHub repos.
  + Obtain a premium [AlphaVantage API key](https://www.alphavantage.co/) (from the professor).
  + Sign up for a [Sendgrid](https://sendgrid.com/) account, verify single sender address, and obtain a SendGrid API key.

## Instructions

First, make a copy of the professor's ["codebase-cleanup-template" repo](https://github.com/prof-rossetti/codebase-cleanup-template). 
 
Alternatively, if you'd like to start from scratch: create a new repo called something like "codebase-cleanup-2022", and during this process, add a "README.md" file and a Python-flavored ".gitignore" file.

## Repository Setup

Configure the GitHub repo to integrate with the "Python application" GitHub Action. This is for "Continuous Integration" purposes, which we will talk about later. This step should add a ".github/workflows/python-app.yml" file [like this one](starter/python-app.yml) to your repo.

Integrate your repo with the [Code Climate](/notes/devtools/code-climate.md) platform, which will provide automated quality and complexity assessments. Login to Code Climate (Quality Service) via your GitHub account. Visit the Code Climate dashboard, and click "Add a repository" and choose the repo you just created. Through the repo's settings on Code Climate, enable "Summary Comments" and/or "Inline Issue Comments". Optionally explore the python-related "Plugins", but prefer to add a predefined "codeclimate.yml" file [like this one](starter/.codeclimate.yml) to the root directory of the repo.

Clone the repo to download it onto your computer. Navigate there from the command line, and open in a text editor of choice. For example:

```sh
cd ~/Desktop
git clone git@github.com:YOUR_USERNAME/codebase-cleanup-2022.git
cd codebase-cleanup-2022/
code .
```

As necessary, if you were starting from scratch: ensure your repo contains an "app" directory with files: "game.py", "groceries.py", "crypto.py", "stocks.py", "crypto.py", "unemployment.py", and "email_me.py", respectively. You can copy the file contents from [this starter code](starter/app). As necessary, save the files, make a commit, and push the changes up to the remote repo (main branch).




## Challenges

Use a Pull Request workflow to complete the coding-based challenges below (i.e. "Game Improvements", "Groceries Inventory Improvements", and "Financial Services Improvements").

Optionally invite a friend to collaborate on your repo, and perform a code review on at least one of your Pull Requests.

### Repo Updates and Improvements

**"requirements.txt" file updates:**

As you run various Python files when working on the coding-based challenges below, you'll notice you might need to install packages to avoid "ModuleNotFound" errors. To facilitate package installations, ensure you're using a virtual environment, and that there is a "requirements.txt" file in the repo's root directory. When new application code requires installation of new packages, update the "requirements.txt" file to include the names of those required packages. If you have been starting from scratch: create an empty "requirements.txt" file, make a commit, and push the changes up to the remote repo (main branch).

**"README.md" file updates:**

By the end of the exercise, ensure your README file has all necessary instructions for how someone can:
  + Setup a virtual environment
  + Install all packages (in one step via the "requirements.txt" file)
  + Obtain any API Keys and configure Environment Variables using a ".env" file approach
  + Run all python files of interest
  + Run tests

### Game Improvements

File(s): "game.py"

User Feedback: "Sometimes it gets the winner wrong!"

Developer Maintenance Steps:

  1. Refactor duplicate code related to the valid options ("rock", "paper", and "scissors").
  2. Notice Code Climate says the existing winner determination logic is "complex". Refactor the complex logic to use less computational steps and also make it easier to read. Also notice the existing logic produces some inaccurate outcomes, and update the logic to produce accurate outcomes.
  3. Test that the winner determination logic produces accurate outcomes. Move the logic into a stand-alone function called `determine_winner()` that can be invoked and tested in isolation, separate from any user inputs. The winner determination function should accept the user choice and the computer choice as input parameters, and should return the value of the winning choice.
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

  6. Test the program's ability to calculate the average product price. Move the average price calculation logic into a stand-alone function called something like `calculate_avg_price()` that can be invoked and tested in isolation. The function should accept any list or DataFrame of products as its input parameter, and should return the average price as a float (unformatted). Use mock data or a mock CSV file to perform this test.


### Financial Services Improvements

File(s): "unemployment.py", "stocks.py", "crypto.py"

User Feedback: "The unemployment chart is messed up!"

Developer Maintenance Steps:

  1. Refactor duplicate code related to the price-formatting logic (across all files in the repo, including the "groceries.py" file). Move the common formatter function to a separate file called something like "utils.py" or "decorators.py" or "formatters.py". Then import this shared function into all the files that need it. NOTE: you may need to add the infamous "init" file to the "app" directory, and you may need to use the infamous "main" conditional in any files being imported from.
  2. Move any duplicate or related financial data fetching code into a separate module called something like "alphavantage_service.py". Include data fetching functions that can be tested in isolation, and imported into other files that need the data. HINT: it might end up looking something [like this](progress/app/alphavantage_service.py).

Optional, Advanced Testing Considerations:

  1. Fix the unemployment chart, and incorporate a test to ensure it is producing the proper result. HINT: consider testing aspects of the underlying DataFrame used to make the chart, like the dataypes of certain columns.
  2. In "stocks.py" and/or "crypto.py", test the program's ability to request data for a given stock or crypto symbol, and that the resulting response data is structured in the expected format. HINT: since the response data will be dynamic, we can focus on some consistent parts of the response data, like ensuring certain keys like "Meta Data" and "Time Series (Daily)" exist, and checking the symbol we requested is contained in the "Meta Data". Optionally can mock the response to return some example data.
  3. Write some tests that can be run without making any network requests (using mock data), and/or minimize the number of requests that get made (using pytest fixtures).

> HINT: here are some examples of working through some of these advanced testing considerations, in different ways, for different purposes:
>  + [testing the stocks report (2021, functional approach, with fixtures)](https://github.com/prof-rossetti/codebase-cleanup-2021/pull/5/files)
>  + [testing the stocks report (2021, object-oriented approach, with fixtures)](https://github.com/prof-rossetti/codebase-cleanup-2021/pull/6/files)
>  + [testing the unemployment report (2022, functional approach, end-to-end integration test)](progress/tests/unemployment_test_1.py)
>  + [testing the unemployment report (2022, functional approach, using mock data)](progress/tests/unemployment_test_2.py)


## Evaluation

The project will be evaluated according to the instructions above, as summarized in the table below:

Category | Description | Weight
--- | --- | ---
Pull Request Workflow | At least two or three Pull Requests used during development. | 10%
Continuous Integration | Tests have been run and passed on a CI server at least once, ideally as part of the Pull Request workflow (using GitHub Actions). | 10%
Code Quality | The Code Climate service has been integrated into the Pull Request workflow to provide automated code quality checks. | 10%
Peer Reviews (Optional) | A peer has provided an unofficial comment or official review as part of the Pull Request workflow. | 0%
Repo Improvements | The "README.md" file contains comprehensive setup and usage instructions (see guidance above). | 10%
Repo Improvements | The "requirements.txt" file facilitates package installations required to run any of the files. | 10%
Game Improvements | Simplify valid options list. | 5%
Game Improvements | Reduce complexity of winner determination logic. | 5%
Game Improvements | Refactor winner determination logic into a stand-alone function and test it to ensure it produces desired results. | 5%
Game Improvements | Document winner determination function using a docstring. | 5%
Groceries Improvements | Simplify CSV filepaths. | 5%
Groceries Improvements | Reduce complexity by using a single loop instead of two. | 5%
Groceries Improvements | Refactor USD-formatting logic into a stand-alone function, document it, and test it to ensure it produces desired results. | 10%
Financial Service Improvements | Refactor USD-formatting function into a helper "module" file, and import the function across whichever files need it. | 5%
Financial Service Improvements  | Refactor financial data-fetching code into a helper "module" file, and import the respective functions across whichever files need them. | 5%


> NOTE: Tests should directly invoke functions from the source code to verify the program behaves as expected.


> NOTE: for this project, evaluators will be reading your code and inspecting your repo across the various platforms (Github, Code Climate, etc.), but not necessarily running or testing your application code directly.

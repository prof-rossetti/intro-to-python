# "RPS Cleanup" Exercise

## Learning Objectives

  + Develop new features in a controlled manner, by adopting Git branch operations and a Pull Request workflow.
  + Practice collaborating with other developers and conducting Peer Reviews.
  + Simplify an existing codebase to decrease future maintenance costs, and reduce errors.
  + Write and execute automated tests to verify code is functioning as expected.
  + Incorporate automated checks (like running tests on a Continuous Integration server), to determine whether code updates are ready to be merged / adopted.

## Prerequisites

  + Read the [Unit 8](/units/unit-8.md) Notes
  + Sign up for the [Code Climate (Quality) service](https://codeclimate.com/quality/), and login with your GitHub account, and "install" Code Climate to access your GitHub repos.

## Prompt

User Feedback: "Sometimes it gets the winner wrong!"

Developer Maintenance Steps / Objectives:

  1. Refactor duplicate code related to the valid options ("rock", "paper", and "scissors").
  2. Notice Code Climate says the existing winner determination logic is "complex". Refactor the complex logic to use less computational steps and also make it easier to read. Also notice the existing logic produces some inaccurate outcomes, and update the logic to produce accurate outcomes.
  3. Test that the winner determination logic produces accurate outcomes. Move the logic into a stand-alone function called something like `determine_winner()` that can be invoked and tested in isolation, separate from any user inputs. The winner determination function should accept the user choice and the computer choice as input parameters, and should return either A) the value of the winning choice or B) a message saying who won.
  4. Document the winner determination function with a docstring.

### Repo Setup

Make a copy of the professor's ["rps-cleanup-template" repo](https://github.com/prof-rossetti/rps-cleanup-template-2022).

## Part 1 (Code Quality and Simplification)


### Code Climate Setup

Login to Code Climate, visit the dashboard, click "Add repository", then search for the repo you just created / copied, and click "Add".

Visit the repository's page in Code Climate. Under "Repo Settings" > "GitHub", configure code climate to: "enable summary comments" and/or "enable inline issue comments". Also "install PR status updates".

At this time you should be able to view some issues Code Climate has identified related to complexity. Before moving on we need to also configure Code Climate to check for duplication.

Return to your repository's homepage on GitHub. Use the online editor to "Add file" > "Create new file" called ".codeclimate.yml". Insert the following contents, then conclude the commit:


```
# this is the ".codeclimate.yml" file (in the root directory of your repo)
#
# see: https://docs.codeclimate.com/docs/duplication-concept
# ... https://docs.codeclimate.com/docs/default-analysis-configuration#sample-codeclimateyml
#
version: "2"
checks:
  #similar-code:
  #  enabled: true
  #  config:
  #    threshold:
  identical-code:
    enabled: true
    config:
      threshold: 2
```

This config file tells Code Climate to also check for duplicate code.

At this time when you view the issues Code Climate has identified, you should see issues related to "duplication".

Alright, you have successfully configured Code Climate!

### Fix Duplication

Clone / download the repo via your git client of choice (i.e. GitHub Desktop).

Checkout a new local branch called something like "simple".

Update your local "game.py" file to remove duplication / refactor using a shared variable. Save the file. Run the game to make sure it still works. Make a commit.

Push your local commit up to GitHub. Now there is a remote version of the "simple" branch.

Create a Pull Request from this branch.

Optionally invite a friend as a collaborator on your repo, via the GitHub repo settings. Optionally ask your friend to conduct a code review.

Observe PR comments / checks made by Code Climate, saying the duplication has been fixed!

When satisfied, merge the "simple" branch into the "main" branch. Now your repo homepage / "main" branch should be up to date.

### Refresh your Local Repo

After merging a PR remotely via the GitHub interface, we need to update our local repo's "main" branch.

From GitHub Desktop, checkout the "main" branch. Pull / fetch the code from origin (i.e. the remote repo).

Now your local repo's "main" branch is up to date.




## Part 2 (Automated Testing and Continuous Integration)


### Configure GitHub Actions

We're going to use GitHub Actions for continuous integration purposes. From the repo's "Actions" tab, add an action called "Python application". Conclude the commit to add a config file (".github/workflows/python-app.yml") to the remote repo.

From GitHub Desktop, pull the changes again to update your local repo to include this config file.

Observe there is a new failing check. It says our tests are failing. We haven't yet setup tests, so we'll do that next.

### Configuring Pytest

Use GitHub Desktop to checkout a new branch called something like "testing".

Using your text editor, update the "requirements.txt" file to un-comment the line related to `pytest`. Save the file.


Install the pytest package via `pip install -r requirements.txt`.

Run `pytest` from the command line to see there are no tests.


### Adding Tests



Let's add a new file to the repo called "game_test.py" and insert the following code inside:


```py
# this is the "game_test.py" file...

#
# if you want to setup your winner determination function to return a message about who won,
# use this test:
#

from game import winner

def test_winner():
    tie_message = "It's a tie!"
    win_message = "The user wins"
    lose_message = "The computer wins"

    assert winner(user_choice="rock", computer_choice="paper") == lose_message
    assert winner(user_choice="rock", computer_choice="rock") == tie_message
    assert winner(user_choice="rock", computer_choice="scissors") == win_message

    assert winner(user_choice="paper", computer_choice="paper") == tie_message
    assert winner(user_choice="paper", computer_choice="rock") == win_message
    assert winner(user_choice="paper", computer_choice="scissors") == lose_message

    assert winner(user_choice="scissors", computer_choice="paper") == win_message
    assert winner(user_choice="scissors", computer_choice="rock") == lose_message
    assert winner(user_choice="scissors", computer_choice="scissors") == tie_message

#
# if you want to setup your winner determination function to return the winning choice,
# use this test:
#

#from game import winning_choice
#
#def test_winning_choice():
#    assert winning_choice(user_choice="rock", computer_choice="paper") == "paper"
#    assert winning_choice(user_choice="rock", computer_choice="rock") == None
#    assert winning_choice(user_choice="rock", computer_choice="scissors") == "rock"
#
#    assert winning_choice(user_choice="paper", computer_choice="paper") == None
#    assert winning_choice(user_choice="paper", computer_choice="rock") == "paper"
#    assert winning_choice(user_choice="paper", computer_choice="scissors") == "scissors"
#
#    assert winning_choice(user_choice="scissors", computer_choice="paper") == "scissors"
#    assert winning_choice(user_choice="scissors", computer_choice="rock") == "rock"
#    assert winning_choice(user_choice="scissors", computer_choice="scissors") == None



```

This file contains two strategies we could use to test our gameplay logic. Choose the strategy that most closely matches your original approach. Default to using the first one for now, for demonstration purposes.

The test wants to import a function called ``winner` from the "game.py" file. Let's create that function now. In order for our test to import this function cleanly (and not run the rest of our game code), we need to nest everything else under the "main conditional". Your "game.py" file structure should look like this:


```py

from random import choice

valid_options = ["rock", "paper", "scissors"]


def winner(user_choice, computer_choice):
    return "OOPS - TODO"


if __name__ == "__main__":

    #
    # USER SELECTION
    #

    # ... (some code here)

    #
    # COMPUTER SELECTION
    #

    # ... (some code here)

    #
    # DETERMINATION OF WINNER
    #

    # ... (some code here)

```

Run tests again to see them fail.

Push your code up to GitHub (on the "testing" branch), and create a new Pull Request to see some updated checks, but notice our testing check is still failing.

### Passing Tests


Update the logic inside the `winner` function and re-run tests until the tests pass.

When you're doing this, you might notice some bugs in our initial logic that we didn't catch before.


After tests are passing locally, push your code up to GitHub and notice our checks are passing.



## Updating Game Code

Update the game code at the bottom of the main conditional to use the function we just tested and proved is working. Run the game locally to make sure it still works. Save the file and make a commit.

Push your code up to GitHub again and notice our checks are still passing.

When satisfied, merge the PR.

Alright, you're developing and testing like a pro!

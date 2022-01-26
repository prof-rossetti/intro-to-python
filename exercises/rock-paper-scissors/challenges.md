# "Rock, Paper, Scissors" Exercise

## Further Exploration Challenges

If you were able to implement the [basic requirements](README.md) with relative ease, or if you are interested in a challenge, consider expanding the scope to include one or more of the challenges below.

Category | Difficulty Level | Requirement | Weight
--- | --- | --- | ---
Customization | Beginner | Instructs and enables the user to configure their own player name - without revising the code, without asking for a user input, but rather by passing an environment variable. | 4-6% (BONUS)
Testing | Intermediate / Advanced | Includes automated tests to indicate if the `determine_winner` function is working properly. For full credit, tests should pass, and game code should be updated to invoke the  `determine_winner` function. | 8-12% (BONUS)

### Player Name Customization

Prerequisites:
  + [Environment Variables](/notes/environment-variables/README.md)
  + [The `os` Module](/notes/python/modules/os.md#Environment-Variables) -- focusing on getting environment variables


Right now the player's name is always "Player One" but it would be nice to allow the user to configure their own player name by passing an environment variable called `PLAYER_NAME`.

Update your "game.py" file to use [the `os` module](/notes/python/modules/os.md#Environment-Variables) to read this environment variable.

```py
# this is the "game.py" file...

import os

player_name = os.getenv("PLAYER_NAME", default="Player One")

# ...
```


Make sure to add corresponding instructions to the README file, to let the player know how to pass that environment variable to the script during runtime:


    PLAYER_NAME="Jon Snow" python game.py


### Automated Tests

Prerequisites:
  + [Python Modules and Imports](/notes/python/modules/README.md)
  + ["Modules and Imports" Exercise](/exercises/modules-and-imports/README.md)
  + [The `pytest` Package](/notes/python/packages/pytest.md)

By now you've probably been running the app manually to determine whether or not it is behaving as desired. But due to the randomness of the computer's selection, you might've had to run many iterations of the game before you are able to see how it functions under all possible scenarios.

As a best practice, let's learn how to automate those manual testing efforts, and use these automated tests to cover all possible edge-case scenarios.

Before we test some of the program's logic, we need to abstract that logic into one or more custom functions (e.g. the provided `determine_winner` function below). Encapsulating the logic inside a function helps us test that logic in isolation.


Update the organizational structure of your "game.py" file to generally resemble the provided code below:

```py
# this is the "game.py" file...

# ...

def determine_winner(choice_1, choice_2):
    """
    Determines the winning choice between two valid choices from selectable options: "rock", "paper", or "scissors".

    Returns the winning choice (e.g. "paper"), or None if there is a tie.

    Example: determine_winner("rock", "paper")
    """
    # todo: write some Python here to determine the winner
    return "TODO"


if __name__ == "__main__":

    print("WELCOME TO MY ROCK PAPER SCISSORS GAME!")

    # ...

```

You'll notice there is a `determine_winner` function definition in the global scope. And all other code that was originally in the file's global scope should now be nested under the infamous "main" conditional instead. This allows the test file to import the function without running the rest of that code. See the "Modules and Imports" Exercise for more details.

After making these organizational adjustments to your "game.py" file, add another file called "game_test.py", as necessary, and place inside contents like the following test scenarios:


```py
# this is the "game_test.py" file...

from game import determine_winner

def test_determination_of_the_winner():
    assert determine_winner("rock", "rock") == None # represents a tie
    assert determine_winner("rock", "paper") == "paper"
    assert determine_winner("rock", "scissors") == "rock"

    assert determine_winner("paper", "rock") == "paper"
    assert determine_winner("paper", "paper") == None # represents a tie
    assert determine_winner("paper", "scissors") == "scissors"

    assert determine_winner("scissors", "rock") == "rock"
    assert determine_winner("scissors", "paper") == "scissors"
    assert determine_winner("scissors", "scissors") == None # represents a tie

```

Once both of those files have been saved, we'll use the `pytest` package to run the test from the command-line:

```sh
pytest game_test.py
```

At first, you'll see the tests fail. It's because the provided `determine_winner` function doesn't yet do anything. Your job is to update the logic of the `determine_winner` function in the "game.py" file until the tests pass. Afterwards, also update your "game.py" file to use the completed `determine_winner` function.

Nice, you're testing like a Pro!

Finally, add these instructions into the repo's README file:

    ## Testing

    Run tests:

    ```sh
    pytest
    ```

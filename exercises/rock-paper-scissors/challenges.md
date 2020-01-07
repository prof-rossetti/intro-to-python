# "Rock, Paper, Scissors" Exercise

## Further Exploration Challenges

If you were able to implement the [basic requirements](README.md) with relative ease, or if you are interested in a challenge, consider expanding the scope to include one or more of the challenges below.

### UI / UX Improvements

> Prerequisites: [Interface Capabilities Exercise](/exercises/interface-capabilities.md)

Are there any issues with the basic command-line interface (CLI)? For example, does it elicit biased responses from the user due to the user's desire to type the easiest option (i.e. "rock")? Should the user enter numbers (e.g. "1", "2", or "3") or single-letters (e.g. "R", "P", "S") instead of entire words?

How could you modify the user interface to improve the user experience? Would a graphical user interface (GUI) lead to a better user experience? What if it featured a different selection mechanism like a dropdown, list-box, or three separate large buttons?

Sketch a mockup of your ideal interface on piece of paper or whiteboard, and then implement that desired interface! For implementation guidance, consult the professor's example apps which use different third-party packages to implement different kinds of GUI interfaces:

  + https://github.com/prof-rossetti/rock-paper-scissors-py
  + https://github.com/prof-rossetti/rock-paper-scissors-flask

### Automated Tests

> Prerequisites: [The `pytest` Package](/notes/python/packages/pytest.md)

So by now you've probably been running the app manually to determine whether or not it is behaving as desired. But due to the randomness of the computer's selection, you might've had to run many iterations of the game before you are able to see how it functions under all possible scenarios.

As a best practice, let's learn how to automate those manual testing efforts, and use these automated tests to cover all possible edge-case scenarios.

Before we test some of the program's logic, we need to abstract that logic into one or more custom functions (e.g. `determine_winner()`) which we can test in isolation. And we'll need to update the organizational structure of our game script to include the infamous `if __name__ == "__main__"` convention, to prevent the rest of the game's functionality from being executed when we attempt to import and test the `determine_winner()` function in isolation.

After making these organizational adjustments to your "game.py" file, add another file called "game_test.py" and place inside the following contents:

```py
# game_test.py

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

Then use the `pytest` package to run the test:

```sh
pytest game_test.py
```

If tests fail, update the logic of the `determine_winner()` function in the "game.py" file until the tests pass.

Nice, you're testing like a Pro!

# "Rock, Paper, Scissors" Exercise

## Further Exploration Challenges

If you were able to implement the [basic requirements](README.md) with relative ease, or if you are interested in a challenge, consider expanding the scope to include one or more of the challenges below.

Category | Difficulty Level | Requirement 
--- | --- | --- 
Customization | Beginner | Instructs and enables the user to configure their own player name - without revising the code, without asking for a user input, but rather by passing an environment variable. 

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



```py
# let's define a custom function called determine_outcome
# ... that accepts the user choice and computer choice as its parameter inputs
# ... and returns the outcome
# if it works properly, the tests below should all pass

def determine_outcome(u, c):
    # DETERMINE THE WINNER AND PRINT WHO WON

    return "TODO"
```

```py
# these tests invoke our function with certain combinations of parameter inputs
# ... and prove whether or not the function works as expected / returns the expected value

assert determine_outcome(u="rock", c="rock") == "TIE GAME"
assert determine_outcome(u="rock", c="paper") == "COMP WINS"
assert determine_outcome(u="rock", c="scissors") == "USER WINS"

assert determine_outcome(u="paper", c="rock") == "USER WINS"
assert determine_outcome(u="paper", c="paper") =="TIE GAME"
assert determine_outcome(u="paper", c="scissors") == "COMP WINS"

assert determine_outcome(u="scissors", c="rock") == "COMP WINS"
assert determine_outcome(u="scissors", c="paper") == "USER WINS"
assert determine_outcome(u="scissors", c="scissors") == "TIE GAME"

print("ALL TESTS PASS")
```

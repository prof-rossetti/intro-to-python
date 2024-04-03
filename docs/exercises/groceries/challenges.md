# Python Datatypes (a.k.a. "Groceries") Exercise

## Further Exploration Challenges

If you were able to implement the [basic requirements](README.md) with relative ease, or if you are interested in a challenge, consider expanding the scope to include one or more of the challenges below.

### Automated Tests

> Prerequisites: [The `pytest` Package](./../../notes/python/packages/pytest.md)

Before we test some of the program's logic, we need to abstract that logic into one or more custom functions (e.g. `to_usd()`) which we can test in isolation. And we'll need to update the organizational structure of our script to include the infamous `if __name__ == "__main__"` convention, to prevent the rest of the script's functionality from being executed when we attempt to import and test the `to_usd()` function in isolation.

After making these organizational adjustments to your "groceries.py" file, add another file called "groceries_test.py" and place inside the following contents:

```py
# groceries_test.py

from groceries import to_usd

def test_to_usd():
    # it should apply USD formatting:
    assert to_usd(4.50) == "$4.50"

    # it should display two decimal places:
    assert to_usd(4.5) == "$4.50"

    # it should round to two places:
    assert to_usd(4.55555) == "$4.56"

    # it should display thousands separators:
    assert to_usd(1234567890.5555555) == "$1,234,567,890.56"
```

Then use the `pytest` package to run the test:

```sh
pytest groceries_test.py
```

If tests fail, update the logic of the `to_usd()` function in the "groceries.py" file until the tests pass.

Nice, you're testing like a Pro!

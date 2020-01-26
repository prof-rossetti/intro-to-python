
# Testing the "Shopping Cart" Project

> Prerequisite: [The `pytest` Package](/notes/python/packages/pytest.md)

## Setup

From within the "shopping-env" virtual environment, install the `pytest` package:

```sh
pip install pytest # (first time only)
```

As you tackle the challenges below, you should be able to run tests from the root directory of your project repository:

```sh
pytest
```

## Automated Testing Challenges

### Testing Price Formatting

Refactor price-formatting logic into a function called something like `to_usd()`, and implement a corresponding test called something like `test_to_usd()`.

Test various scenarios to ensure the price formatting function displays a dollar sign, two decimal places, and a thousands separator.

### Testing Timestamp Formatting

Refactor timestamp-formatting logic into a function called something like `human_friendly_timestamp()`, and implement a corresponding test called something like `test_human_friendly_timestamp()`.

Test to ensure the function processes any given datetime object into a corresponding human-friendly string.

### Testing Product Lookups

Refactor product-finding logic into a function called something like `find_product()`, and implement a corresponding test called something like `test_find_product()`.

Test various scenarios to ensure the product lookup function finds and returns the proper product, even if the products are not sorted in order of their unique identifiers. What should happen when the function is passed a numeric identifier vs a string identifier? What should happen when there is no product matching the given identifier?

### Testing Tax and Total Calculations

Refactor subtotal and/or total price calculation logic into one or more function(s) called something like `calculate_total_price()`, and implement a corresponding test(s) called something like `test_calculate_total_price()`.

Test various scenarios to ensure the calculation function(s) produce the proper sum of prices, given a list of selected products and/or product identifiers.

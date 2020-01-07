# Python Datatypes (a.k.a. "Groceries") Exercise

## Further Exploration Challenges

If you were able to implement the [basic requirements](README.md) with relative ease, or if you are interested in a challenge, consider expanding the scope to include one or more of the challenges below.

### Departments

> Prerequisites: [Lists](/notes/python/datatypes/lists.md) and the ["List Comprehensions" Exercise](/exercises/list-comprehensions/README.md)

In addition to displaying the products in a human-friendly format, also display the departments in a human-friendly format. For each department, include the number of products associated with that department.

Example desired output:

    --------------
    THERE ARE 20 PRODUCTS:
    --------------
     + All-Seasons Salt ($4.99)
     + Chocolate Fudge Layer Cake ($18.50)
     + Chocolate Sandwich Cookies ($3.50)
     + Cut Russet Potatoes Steam N' Mash ($4.25)
     + Dry Nose Oil ($21.99)
     + Fresh Scent Dishwasher Cleaner ($4.99)
     + Gluten Free Quinoa Three Cheese & Mushroom Blend ($3.99)
     + Green Chile Anytime Sauce ($7.99)
     + Light Strawberry Blueberry Yogurt ($6.50)
     + Mint Chocolate Flavored Syrup ($4.50)
     + Overnight Diapers Size 6 ($25.50)
     + Peach Mango Juice ($1.99)
     + Pizza For One Suprema Frozen Pizza ($12.50)
     + Pomegranate Cranberry & Aloe Vera Enrich Drink ($4.25)
     + Pure Coconut Water With Orange ($3.50)
     + Rendered Duck Fat ($9.99)
     + Robust Golden Unsweetened Oolong Tea ($2.49)
     + Saline Nasal Mist ($16.00)
     + Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce ($6.99)
     + Sparkling Orange Juice & Prickly Pear Beverage ($2.99)
    --------------
    THERE ARE 10 DEPARTMENTS:
    --------------
     + Babies (1 product)
     + Beverages (5 products)
     + Dairy Eggs (1 product)
     + Dry Goods Pasta (1 product)
     + Frozen (4 products)
     + Household (1 product)
     + Meat Seafood (1 product)
     + Pantry (2 products)
     + Personal Care (2 products)
     + Snacks (2 products)

> HINT: use the `filter()` function or the filtering capabilities of a list comprehension to lookup all products associated with any given department, then use the `len()` function to count them

### Automated Tests

> Prerequisites: [The `pytest` Package](/notes/python/packages/pytest.md)

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

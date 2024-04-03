# "Groceries" Exercise

## Learning Objectives

  + Gain familiarity with the Python programming language, focusing on datatypes and looping.
  + Practice processing in-memory Python data structures into a desired information output.
  + Practice using a text editor to edit and save files of Python code.
  + Practice incorporating version control into your development process.
  + Practice importing and accessing functionality provided by Python modules.

## Instructions

Iteratively develop a Python program which will process a provided data structure into a desired human-friendly output. The program's functionality should adhere to the "Basic Requirements" below.

Before attempting to implement the basic requirements, take some time to configure your project repository according to the "Setup" instructions below. After doing so, you'll have a remote repo on GitHub.com and a local copy on your computer within which to develop.

When developing, as you reach key milestones, use the command-line or GitHub Desktop software to intermittently "commit", or save new versions of, your code. And remember to push / sync / upload your work back up to your remote project repository on GitHub.com at least once before you're done.

If you need help breaking the problem up into more manageable pieces, consult the "Guided Checkpoints" and/or the "Guided Screencast" (links below).

## Setup

### Repo Setup

Use the GitHub.com online interface to create a new remote project repository called something like "groceries-exercise". When prompted by the GitHub.com online interface, let's get in the habit of adding a "README.md" file and a Python-flavored ".gitignore" file (and also optionally a "LICENSE") during the repo creation process. After this process is complete, you should be able to view the repo on GitHub.com at an address like `https://github.com/YOUR_USERNAME/groceries-exercise`.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

```sh
cd ~/Desktop/groceries-exercise
```

Use your text editor or the command-line to create a file in that repo called "groceries.py", and then place the following contents inside:

```py
# groceries.py

#from pprint import pprint

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output
```

Make sure to save Python files like this whenever you're done editing them. After setting up a virtual environment, we will be ready to run this file.

### Environment Setup

Create and activate a new Anaconda virtual environment:

```sh
conda create -n groceries-env python=3.8 # (first time only)
conda activate groceries-env
```

From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

```sh
python groceries.py
```

If you see the provided "products" data structure, you're ready to move on to project development. This would be a great time to make any desired modifications to your project's "README.md" file (like adding instructions for how to setup and run the app like you've just done), and then make your first commit, with a message like "Setup the repo".

## Basic Requirements

### Printing Products

Inside the "groceries.py" script, write Python code which will transform the provided data structure into the following output:

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

> HINT: for formatting numbers as currency, feel free to use the `to_usd` function provided [here](./../../notes/python/datatypes/numbers.md#formatting-as-currency).

### Printing Departments

> Prerequisites: [Lists](./../../notes/python/datatypes/lists.md) and the ["List Comprehensions" Exercise](./../list-comprehensions/README.md)

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

## [Guided Checkpoints](checkpoints.md)

Feel free but not obligated to follow these guided "checkpoints", which provide one example strategy for breaking-up the requirements into smaller, more manageable pieces.

## [Guided Screencast](https://www.youtube.com/watch?v=Noy20XaMqho&feature=youtu.be)

For a more in-depth guided exercise walkthrough, follow the screencast, but keep in mind a few caveats:

  1. The screencast will instruct you to use the GitHub.com online interface to "commit", but you should be using GitHub Desktop instead.
  2. Some of the links reference a previous course repository, but you should be able to find related documents in this course repository as well.
  3. During the virtual environment creation step, make sure to specify the python version as 3.7 (was omitted in the video).
  4. For simplicity, when sorting with the `sorted()` function, it is reasonable to prefer the `operator.itemgetter()` approach over the custom function approach.

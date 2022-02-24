# The `getpass` Module

References:
  + https://docs.python.org/3/library/getpass.html

## Problem

When using the `input` function in Python to capture user inputs, we end up seeing the resulting value as the user types it (in this case "vanilla bean"):

```py
fav_flavor = input("Please input your favorite icecream flavor: ")

#> Please input your favorite icecream flavor: vanilla bean
```

But what if we want to ask for more sensitive inputs, like secret passwords or credentials? We need a way to prevent them from showing up in the program's output.

## Solution

We can hide a user-inputted value by using the `getpass` function instead of the `input` function. The `getpass` function will either hide the resulting value, or mask it using a key icon or series of asterisks:


```py
from getpass import getpass

my_password = getpass("Please input your secret password: ")
#> Please input your secret password: 🔑
```

This is espectially helpful in Google Colab, so you can share your notebook's output without exposing your secret credentials:


<img width="1240" alt="Screen Shot 2022-02-23 at 9 40 25 PM" src="https://user-images.githubusercontent.com/1328807/155450958-835fe78f-52b3-46f4-ad9f-89c29fb4fa6f.png">

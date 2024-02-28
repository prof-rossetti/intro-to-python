# "Web Requests" Exercise

> Prerequisite:
>   + [The `requests` Package](/notes/python/packages/requests.md)

## Learning Objectives

  + Practice using Python to request static data files located on the Internet, focusing on "GET" requests.
  + Increase exposure to JSON-formatted data, and practice processing it in Python.
  + Leverage built-in Python modules and third-party Python packages to speed development and enhance capabilities.
  + Prepare to issue requests to get data from web services (APIs).



## Setup

### Repo Setup

Use the GitHub.com online interface to create a new remote project repository called something like "web-requests-exercise". When prompted by the GitHub.com online interface, let's get in the habit of adding a "README.md" file and a Python-flavored ".gitignore" file (and also optionally a "LICENSE") during the repo creation process. After this process is complete, you should be able to view the repo on GitHub.com at an address like `https://github.com/YOUR_USERNAME/web-requests-exercise`.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

```sh
cd ~/Desktop/web-requests-exercise
```

Use your text editor or the command-line to create a file in that repo called "get_data.py", and then place the following contents inside:

```py
# get_data.py

print("REQUESTING SOME DATA FROM THE INTERNET...")
```

Make sure to save Python files like this whenever you're done editing them. After setting up a virtual environment, we will be ready to run this file.

### Environment Setup

Create and activate a new Anaconda virtual environment:

```sh
conda create -n requests-env python=3.8 # (first time only)
conda activate requests-env
```

From within the virtual environment, install the `requests` package:

```sh
pip install requests
```

From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

```sh
python get_data.py
```

If you see the provided message, you're ready to move on to project development. This would be a great time to make any desired modifications to your project's "README.md" file (like adding instructions for how to setup and run the app like you've just done), and then make your first commit, with a message like "Setup the repo".





## Challenges

Iteratively develop your Python script to tackle each of the following challenges.

> HINT: the response text for each of the following challenges will be formatted as JSON, so you can use [the `json` module](/notes/python/modules/json.md) to parse it. Also, depending on which URL we are making a request to, sometimes the JSON response will resemble a list and sometimes it will resemble a dictionary, so make sure to parse each accordingly.

### Requesting a Product

Write a Python program which issues a GET request for this [product.json data](https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json), then prints the product's "name".

> FYI: the response text will be a JSON object, like a Python dictionary

### Requesting Products

Write a Python program which issues a GET request for this [products.json data](https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json), then loop through each product and print its "name" and "id" attributes.

> FYI: the response text will be a JSON array of objects, like a Python list of dictionaries

### Requesting the Gradebook

Write a Python program which issues a GET request for this [gradebook.json data](https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json), then calculate and print the average, min, and max grades.

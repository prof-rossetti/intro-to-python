
# Checkpoint 3: Rendering HTML Pages

It's cool some of our routes are responding with JSON data, but some of them are just returning simple text. Let's take this opportunity to render HTML pages instead.

## Rendering HTML Templates

Flask will be looking for our HTML pages in a "templates" directory by default. So let's create a new subdirectory in the "web_app" folder called "templates", and place inside HTML files called "home.html", "about.html", and "hello.html", with the following contents inside, respectively:


Inside "web_app/templates/home.html":

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My App</title>
</head>
<body>

    <h1>Welcome Home</h1>

    <p>This is a paragraph.</p>

    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/hello">Hello</a></li>
        </ul>
    </nav>

    <footer>
        <hr>
        <p>My footer</p>
    </footer>

</body>
</html>

```

Inside "web_app/templates/about.html":


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My App</title>
</head>
<body>

    <h1>About Me</h1>

    <p>This is a paragraph.</p>

    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/hello">Hello</a></li>
        </ul>
    </nav>

    <footer>
        </hr>
        <p>My footer</p>
    </footer>

</body>
</html>

```


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My App</title>
</head>
<body>

    <h1>{{ message }}</h1>

    <p>This is a paragraph.</p>

    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/hello">Hello</a></li>
        </ul>
    </nav>

    <footer>
        </hr>
        <p>My footer</p>
    </footer>

</body>
</html>

```

Each page has a unique heading, and a shared navigation and footer. We'll refactor the duplicate /shared HTML code later, but for right now it's fine.

Let's now update the home routes to render these HTML pages:

```py
# web_app/routes/home_routes.py

from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("ABOUT...")
    return render_template("about.html")

@home_routes.route("/hello")
def hello_world():
    print("HELLO...", dict(request.args))
    # NOTE: `request.args` is dict-like, so below we're using the dictionary's `get()` method,
    # ... which will return None instead of throwing an error if key is not present
    # ... see also: https://www.w3schools.com/python/ref_dictionary_get.asp
    name = request.args.get("name") or "World"
    message = f"Hello, {name}!"
    return render_template("hello.html", message=message)

```

> NOTE: flask specifically is looking for our HTML files in the "templates" directory by default!

Restart the server and view the app in the browser and navigate between the three HTML pages. Cool!

Notice what's going on with passing a variable to the "hello" page, and how we are using the "Jinja" templating language to reference the variable using double curly braces. For more information about Jinja, see __________.

## Shared Layouts

TODO

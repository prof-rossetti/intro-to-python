
# Web App Checkpoint 3 - Rendering HTML Templates

> FYI: [Reference Code](https://github.com/s2t2/daily-briefings-py/pull/1/commits/bf4de599d22f96a2f67c2610f79b26485f48a6a0)

So far our app is just displaying some simple text when we visit each route. But we have the opportunity to display entire pages written in HTML.

Let's update the home routes to use the `render_template` function from Flask, and choose which files to render.

```py
# web_app/routes/home_routes.py

from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("VISITED THE HOME PAGE")
    #return "Welcome Home (TODO)"
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    #return "About Me (TODO)"
    return render_template("about.html")
```

Here we are referencing two HTML files, called "home.html" and "about.html". Flask wants to look in a specific directory called "templates" for these files. So let's create a new directory in the "web_app" directory called "templates" and insert the following files inside:

Inside "web_app/templates/home.html":

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My App</title>
</head>
<body>

    <h1>This is a heading</h1>

    <p>This is a paragraph text</p>

    <ul>
        <li>First list item</li>
        <li>Second list item</li>
        <li>Third list item</li>
    </ul>

</body>
</html>
```

Inside "web_app/templates/about.html":


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My App</title>
</head>
<body>

    <h1>About Me</h1>

    <p>todo write some stuff here</p>

</body>
</html>
```

Restart your server and view the app in the browser and see the complete HTML pages!

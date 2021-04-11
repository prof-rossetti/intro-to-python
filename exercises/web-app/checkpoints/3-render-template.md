
# Web App Checkpoint 3 - Responses

So far our app is just displaying some simple text when we visit each route. But we have the opportunity to provide more practical responses in JSON or HTML format.

## Responding with JSON

We've studied and used JSON APIs in the past, but now let's make our own!

Add a new file to the "routes" directory called "book_routes.py" and place the following contents inside:

```py
```

Visit "" and "" in the browser to see the JSON data responses.

OK, good to know.

## Rendering HTML Templates

Let's update the home routes to render HTML pages.

```py
# web_app/routes/home_routes.py

from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("VISITED THE HOME PAGE")
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    return render_template("about.html")
```

Here we are referencing two HTML files, called "home.html" and "about.html". Flask wants to look in a specific directory called "templates" for these files. So let's create a new directory in the "web_app" directory called "templates" and insert the following files inside:

Inside "web_app/templates/home.html":

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
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
    <title>My App</title>
</head>
<body>

    <h1>About Me</h1>

    <p>todo write some stuff here</p>

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

    <h1>About Me</h1>

    <p>todo write some stuff here</p>

</body>
</html>
```

> FYI: we can leverage the text editor's auto-completion capabilities to generate the starting structure of these HTML pages. When we create a file with a ".html" extension, if we start to write the word "html" in that file, we'll see the ability to generate an entire "html:5" document skeleton (which you see adapted in each of the pages above).

Restart your server and view the app in the browser and navigate between the three HTML pages.

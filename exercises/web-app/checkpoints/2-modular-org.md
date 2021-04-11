
# Checkpoint 2: Modular Organization

So far we've got a simple app with a few routes, but its already starting to get a bit cluttered, so to make this app easier to maintain as it grows, let's start adopting a more modular organizational structure.

We'll move the app into a new "web_app" directory, and we'll also move the routes into a new "web_app/routes" directory.

## Application Factory Pattern

First, let's implement the Flask ["application factory pattern"](https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/) where we define our application inside a function. Among other benefits, this can help us test our app's functionality later.

Create a new subdirectory in your repo called "web_app" with a file called "\_\_init_\_.py" and place the following contents inside:

```py
# web_app/__init__.py

from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes
#from web_app.routes.weather_routes import weather_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    #app.register_blueprint(weather_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
```

Remember that the "init" file is the entry-point into a local Python module.

Review the new "create_app" function and notice we are importing and referencing our routing functions from their own logically-related files.

> NOTE: in the future, whenever we add more routing files, we'll need to import and register them in this way for our app to recognize them!

## Route Blueprints

Let's now move the route definitions to their own logically-related files, just to be more organized.

We're using [Flask Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/) to store the route definitions in a way the app can recognize.

Inside the "web_app" directory, create a new subdirectory called "routes" with new files called "home_routes.py", "home_routes.py", and "home_routes.py", and place the following contents inside, respectively:

```py
# web_app/routes/home_routes.py

from flask import Blueprint, render_template, request

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    return "Welcome Home"

@home_routes.route("/about")
def about():
    print("ABOUT...")
    return "About Me"

@home_routes.route("/hello")
def hello_world():
    print("HELLO...", dict(request.args))
    # NOTE: `request.args` is dict-like, so below we're using the dictionary's `get()` method,
    # ... which will return None instead of throwing an error if key is not present
    # ... see also: https://www.w3schools.com/python/ref_dictionary_get.asp
    name = request.args.get("name") or "World"
    return f"Hello, {name}!"

```

```py
# web_app/routes/book_routes.py

from flask import Blueprint, jsonify

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/api/books")
@book_routes.route("/api/books.json")
def list_books():
    print("BOOKS...")
    books = [
        {"id": 1, "title": "Book 1", "year": 1957},
        {"id": 2, "title": "Book 2", "year": 1990},
        {"id": 3, "title": "Book 3", "year": 2031},
    ] # some dummy / placeholder data
    return jsonify(books)

@book_routes.route("/api/books/<int:book_id>")
@book_routes.route("/api/books/<int:book_id>.json")
def get_book(book_id):
    print("BOOK...", book_id)
    book = {"id": book_id, "title": f"Example Book", "year": 2000} # some dummy / placeholder data
    return jsonify(book)

```

## New Run Command

We can now delete the original "hello.py" file.

Since we moved the app into the "web_app" directory, we'll use this new command to run it moving forward:

```sh
# mac:
FLASK_APP=web_app flask run

# windows:
export FLASK_APP=web_app
flask run
```

Let's restart the web server using this new command, and visit the same URLs in the browser to see the app is working like it was before.

Great! With the modular codebase we'll be able to maintain and extend our app more easily in the future.

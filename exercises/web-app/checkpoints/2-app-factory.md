
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
from web_app.routes.weather_routes import weather_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(weather_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
```

Remember that the "init" file is the entry-point into a local Python module. When we run this "web_app" module in a moment, it will create a new instance of our app, and run it.

But first we have referenced some of our routes which we need to restore

## Route Blueprints

When we review the new application function, we see references to various "blueprints" which will contain our routes. Here we are moving the route definitions to separate files, and using [Flask Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/), just to be more organized.

So, inside the "web_app" directory, create a new subdirectory called "routes" with a file called "home_routes.py", "home_routes.py", and "home_routes.py", and place the following contents inside, respectively:

```py
# web_app/routes/home_routes.py

from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("VISITED THE HOME PAGE")
    return "Welcome Home (TODO)"


```

```py
# web_app/routes/book_routes.py

from flask import Blueprint

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/")
def index():
    print("VISITED THE HOME PAGE")
    return "Welcome Home (TODO)"


```

```py
# web_app/routes/weather_routes.py

from flask import Blueprint

weather_routes = Blueprint("weather_routes", __name__)

@weather_routes.route("/")
def index():
    print("VISITED THE HOME PAGE")
    return "Welcome Home (TODO)"


```

## New Run Command

Since we moved the app into the "web_app" directory, we'll use this new command to run it moving forward:

```sh
# mac:
FLASK_APP=web_app flask run

# windows:
export FLASK_APP=web_app
flask run
```

Let's (re-)start the web server using this new command, and then visit different URLs in the browser to see the app is working like it was before.

Great! With the modular codebase we'll be able to maintain and extend our app more easily.

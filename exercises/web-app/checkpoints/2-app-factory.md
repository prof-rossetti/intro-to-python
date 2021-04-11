
# Checkpoint 2: Modular Organization

So far we've got a simple app with a few routes, but to make this app easier to maintain as it grows, let's start adopting a more modular organizational structure.

## Application Factory

First, let's implement the Flask ["application factory pattern"](https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/) where we define our application inside a function. Among other benefits, this can help us test our app in isolation later.

Create a new directory called "web_app" with a file called "\_\_init_\_.py" and place the following contents inside:

```py
# web_app/__init__.py

from flask import Flask

from web_app.routes.home_routes import home_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
```

## Route Blueprints

Let's move the route definitions to separate files, using [Flask Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/), just to be more organized.

Inside the "web_app" directory, create a new subdirectory called "routes" with a file called "home_routes.py", "_____", and "", and place the following contents inside, respectively:

```py
# web_app/routes/home_routes.py

from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("VISITED THE HOME PAGE")
    return "Welcome Home (TODO)"

@home_routes.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    return "About Me (TODO)"
```

## New Run Command

With these routes in place and our application configured to recognize them, let's try running our app again. Since we moved the app into the "web_app" directory (the entry point of which is the init file), we'll use this command to run it moving forward:

```sh
# mac:
FLASK_APP=web_app flask run

# windows:
export FLASK_APP=web_app
flask run
```

Still working? Great.


# Web App Checkpoint 2 - Modular Organization

So far we've got a simple app with a few routes, but we need to use a more modular organizational structure for larger apps.

## Application Factory

Create a new directory called "web_app" with a file called "\_\_init_\_.py" and place inside the following contents:

```py
# web_app/__init__.py

#import os
#from dotenv import load_dotenv
from flask import Flask

from web_app.routes.home_routes import home_routes
#from web_app.routes.weather_routes import weather_routes

#load_dotenv()

#SECRET_KEY = os.getenv("SECRET_KEY", default="super secret")

def create_app():
    app = Flask(__name__)
    #app.config["SECRET_KEY"] = SECRET_KEY
    app.register_blueprint(home_routes)
    #app.register_blueprint(weather_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
```

Here we are implementing the Flask ["application factory pattern"](https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/) where we define our application inside a function.

Don't worry about the `SECRET_KEY` for now, we'll need this when we implement "flash messaging" later.

## Route Blueprints

Inside the "web_app" directory, create a new subdirectory called "routes" with a file called "home_routes" and place the following contents inside:

```py
# web_app/routes/home_routes.py

from flask import Blueprint #, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("VISITED THE HOME PAGE")
    #return render_template("dashboard.html")
    return "Welcome Home (TODO)"

@home_routes.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    return "About Me (TODO)"

@home_routes.route("/register")
def register():
    print("VISITED THE REGISTRATION PAGE")
    return "Sign Up for our Product! (TODO)"
```

We're also moving the route definitions to separate files, using [Flask Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/), just to be more organized.

With these routes in place and our application configured to recognize them, let's try running our app again. But since we moved the app into the "web_app" directory (the entry point of which is the init file), we'll now start to run our app like this:

```sh
# mac:
FLASK_APP=web_app flask run

# windows:
export FLASK_APP=web_app
flask run
```

Still working? Great.

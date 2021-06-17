

# Checkpoint 1: Setup

## Quick Start

After installing the Flask package, let's read the [Flask Quick Start Guide](https://flask.palletsprojects.com/en/1.1.x/quickstart/) and see what it wants us to do.

We find an example like the one below. Let's temporarily create a new file called "hello.py" in the root directory of the repo, and place the following contents inside:

```py
# hello.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"
```

> NOTE: We are using a [function decorator](https://www.python.org/dev/peps/pep-0318/) to specify the route (i.e. the path we visit in the browser).

> NOTE: Flask route function names like `hello_world()` must be unique.

Later when we move and re-organize our application we'll need to run it differently, but for now with the "hello.py" file we can run it from the root directory like this:

```sh
# Mac OS:
FLASK_APP=hello.py flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
export FLASK_APP=hello.py
flask run
```

This command starts a local web server on port 5000. Preview the app by visiting http://localhost:5000 in the browser. Nice, the web server is running and responding to our request.

> NOTE: whenever we modify the code we'll need to stop the web server via "ctrl+c", and start it again before previewing again.


> NOTE: some Windows OS students have reported that despite setting environment variables properly, that this command might not work. But when we re-organize the app in the next section, students have reported that has resolved their issue. So if this applies to you, feel free to skip to the next section below.


## Modular Organization

If we add dozens of additional routes, this single file approach will become harder to maintain. Also when we deploy the app to a Heroku server, the server will be looking for a different organizational structure.

So let's adopt a more modular organizational structure, whereby we'll move the app into a new directory and split the routing logic across multiple files.

### Application Factory Pattern

Let's implement the Flask ["application factory pattern"](https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/) where we define our application inside a function. Among other benefits, this can help us test the app later.

Create a new subdirectory in your repo called "web_app" with a file called "\_\_init_\_.py" and place the following contents inside:

```py
# web_app/__init__.py

from flask import Flask

from web_app.routes.home_routes import home_routes
#from web_app.routes.book_routes import book_routes
#from web_app.routes.weather_routes import weather_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    #app.register_blueprint(book_routes)
    #app.register_blueprint(weather_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
```

Review the new "create_app" function and notice we are importing and referencing the routing functions from their own logically-related files.

> NOTE: in the future, whenever we add more routing files, we'll need to import and register them in this way for our app to recognize them (we'll be un-commenting the blueprint imports soon)!

### Route Blueprints

Let's now move the route definitions to their own logically-related files, just to be more organized.

We're using [Flask Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/) to store the route definitions in a way the app can recognize.

Inside the "web_app" directory, create a new subdirectory called "routes" with new files called "home_routes.py", "book_routes.py", and place the following contents inside, respectively:

```py
# web_app/routes/home_routes.py

from flask import Blueprint, request #, render_template

home_routes = Blueprint("home_routes", __name__)

# GET /
# GET /home
@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    return "Welcome Home"
    #return render_template("home.html")

# GET /about
@home_routes.route("/about")
def about():
    print("ABOUT...")
    return "About Me"
    #return render_template("about.html")

```

### Running the Web App

Since we moved the Flask app into the "web_app" directory, We can now delete the original "hello.py" file, and we'll use this new command to run it moving forward:

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
export FLASK_APP=web_app
flask run
```

Remember, the "init" file is the entry-point into a local Python module, so when we run the app this way, Flask will run the "web_app" module's "init" file.

Let's restart the web server using this new command, then visit the following URLs in the browser:
  + http://localhost:5000
  + http://localhost:5000/home
  + http://localhost:5000/about

Review the code that handles these "index" and "about" routes. What do you notice?

Nice, our app is handling requests to different routes!

Great! With the modular codebase we'll be able to maintain and extend our app more easily in the future.

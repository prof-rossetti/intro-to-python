# The `flask` Package

The `flask` package provides a micro-framework for making web applications and APIs.

## References

  + [Website](https://flask.palletsprojects.com/)
  + [Docs](https://flask.palletsprojects.com/en/2.1.x/)
  + [Source](https://github.com/pallets/flask)
  + [Quick-start Guide](https://flask.palletsprojects.com/en/2.1.x/quickstart/)
  + [Tutorial](https://flask.palletsprojects.com/en/2.1.x/tutorial/)
  + [Jinja Templates](https://jinja.palletsprojects.com/en/2.11.x/)

## Installation

First install `flask`, if necessary:

```sh
pip install flask
```

## Usage

Follow the ["Web Application" Exercise](/exercises/web-app/README.md) for an introduction to making web applications with Flask.

### App Initialization

Example application factory function:

```py
# this is the "web_app/__init__.py" file...

from flask import Flask

from web_app.routes.home_routes import home_routes
#from web_app.routes.other_routes import other_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    #app.register_blueprint(other_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)

```

### Routes

Example routes:

```py
# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    return "Welcome Home"
    #return render_template("home.html")

@home_routes.route("/about")
def about():
    print("ABOUT...")
    return "About Me"
    #return render_template("about.html")

@home_routes.route("/hello")
def hello_world():
    print("HELLO...")

    # if the request contains url params, for example a request to "/hello?name=Harper"
    # the request object's args property will hold the values in a dictionary-like structure
    url_params = dict(request.args)
    print("URL PARAMS:", url_params) #> can be empty like {} or full of params like {"name":"Harper"}

    # get a specific key called "name" if available, otherwise use some specified default value
    # see also: https://www.w3schools.com/python/ref_dictionary_get.asp
    name = url_params.get("name") or "World"

    message = f"Hello, {name}!"
    return message
    #return render_template("hello.html", message=message)

```





## Testing Flask Applications

See: https://flask.palletsprojects.com/en/2.1.x/testing/

After you have implemented a web application, if you would like to test it, consider the following examples...


Testing a web application:

```py

import pytest

from web_app import create_app

@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    app.config.update({"TESTING": True})
    return app.test_client()

def test_home(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"<h1>Home</h1>" in response.data

def test_about(test_client):
    response = test_client.get("/about")
    assert response.status_code == 200
    assert b"<h1>About</h1>" in response.data

def test_products(test_client):
    response = test_client.get("/products")
    assert response.status_code == 200
    assert b"<h1>Products</h1>" in response.data
    
    assert b"Textbook" in response.data
    assert b"Cup of Tea" in response.data
    assert b"Strawberries" in response.data
```


Testing Flask APIs:

```py
import pytest

from api import create_app

@pytest.fixture
def api_client():
    app = create_app()
    return app.test_client()

def test_my_endpoint(api_client):
    response = api_client.get("/api/v1/my_endpoint")
    parsed_response = json.loads(response.data)
    assert response.status_code == 200
    assert isinstance(parsed_response, list)
    # etc.
```

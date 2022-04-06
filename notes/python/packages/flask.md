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

## Testing

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

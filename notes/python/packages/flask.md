# The `flask` Package

Reference:

  + [Website](https://flask.palletsprojects.com/)
  + [Docs](https://flask.palletsprojects.com/en/1.1.x/)
  + [Source](https://github.com/pallets/flask)
  + [Quick-start Guide](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
  + [Tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/)
  + [Jinja Templates](https://jinja.palletsprojects.com/en/2.11.x/)

The `flask` package provides a micro-framework for making applications with web interfaces (a.k.a "web applications").

Run a `flask` application "in development" using a web server on your local machine, and/or "in production" using a remote web server hosted by a provider like Heroku. If you run it in development, you should be able to use it by visiting `localhost:5000` in a browser, whereas if you run it in production, you should be able to use it by visiting the production server's URL.

## Installation

First install `flask`, if necessary:

```sh
pip install flask
```

## Usage

Follow the [Official Flask Tutorial](http://flask.pocoo.org/docs/1.0/tutorial/) or the ["Web Application" Exercise](/exercises/web-app/README.md) for an introduction to making web applications with Flask.

## Testing

See also:
  + [The `pytest` Package](/notes/python/packages/pytest.md#fixtures)
  + [Testing Flask Apps](https://flask.palletsprojects.com/en/1.1.x/testing/)

```py
import pytest

from api import create_app # (or whatever your app is called)

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

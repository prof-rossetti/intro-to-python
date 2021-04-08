# The `flask` Package

The `flask` package provides a micro-framework for making web applications and APIs.

## References

  + [Website](https://flask.palletsprojects.com/)
  + [Docs](https://flask.palletsprojects.com/en/1.1.x/)
  + [Source](https://github.com/pallets/flask)
  + [Quick-start Guide](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
  + [Tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/)
  + [Jinja Templates](https://jinja.palletsprojects.com/en/2.11.x/)

## Installation

First install `flask`, if necessary:

```sh
pip install flask
```

## Usage

Follow the ["Web Application" Exercise](/exercises/web-app/README.md) for an introduction to making web applications with Flask.

## Testing

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

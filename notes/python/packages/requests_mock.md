
# The `requests_mock` Package

References:
  + https://requests-mock.readthedocs.io/en/latest/
  + https://pypi.org/project/requests-mock/
  + https://github.com/jamielennox/requests-mock
 

Usage in the wild:
  + https://github.com/sammchardy/python-binance/blob/master/tests/test_api_request.py
  + https://github.com/sammchardy/python-binance/blob/d10de413172412fafe6a1ccd5c64e3ea31c449ee/tests/test_historical_klines.py

## Background

We can use the `requests_mock` package to prevent our code from making network requests, when we are running tests.

When we do this, we essentially prevent the request from being made, and specify some example data that we could pretend got returned.

As a note of caution: when we do this, we have to make sure the mock data we're specifying closely matches the real data that would be returned had we actually made the request.

## Benefits

When we request data from an API, it is reasonable and in many cases expected for it to change over time. For example when we fetch stock market data today and again tomorrow, the recent prices will be different / updated. This inhibits our ability to check for certain specific values when testing. So using mock data is a good solution.

Also, preventing network requests makes our test suite run faster. This means less time taken every time the tests are run (including on CI). This ends up turning into large productivity gains for the developer team. 


## Installation

```sh
pip install requests_mock
```

## Usage

For example, if we have this application code that makes a network request:

```py
# this is some application code (for example in a file called "app/gradebook_service.py") ...

import requests
import json

def fetch_data():
    request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/main/data/gradebook.json"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    return parsed_response
```

Here is how we could test it using mock data:

```py
# this is an example test file ...

import requests_mock

from app.gradebook_service import fetch_data

example_response_data = {
  "downloadDate": "2018-06-05",
  "professorId": 123,
  "students":[
    {"studentId": 1, "finalGrade": 76.7},
    {"studentId": 2, "finalGrade": 85.1},
    {"studentId": 3, "finalGrade": 50.3}
  ]
}

def test_fetch_data():

    # this is the real URL that would normally get requested
    request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/main/data/gradebook.json"

    with requests_mock.mock() as mocker:

        # override the request and return some specified mock data instead
        # do this BEFORE making the request
        mocker.get(request_url, json=example_response_data)

        # now we invoke and test the function in question
        # this would otherwise make the request, but won't since we mocked it above
        data = fetch_data()

        assert isinstance(data, dict)
        assert len(data["students"]) == 3
        assert data["students"][0] == {"studentId": 1, "finalGrade": 76.7}


        
```

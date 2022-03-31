# The `pytest` Package

Prerequisites:
  + [Python Modules and Imports](/notes/python/modules/README.md)
  + [Automated Testing](/notes/software/testing.md)


References:

  + https://github.com/pytest-dev/pytest/
  + https://docs.pytest.org/en/latest/
  + https://docs.pytest.org/en/latest/getting-started.html#our-first-test-run
  + https://docs.pytest.org/en/latest/goodpractices.html
  + https://docs.pytest.org/en/latest/usage.html#dropping-to-pdb-python-debugger-on-failures
  + http://python-guide-pt-br.readthedocs.io/en/latest/writing/tests/#py-test
  + https://docs.pytest.org/en/latest/capture.html

## Installation

If you are using Pip to manage software packages (recommended), install Pytest, as necessary:

```sh
pip install pytest
```

Otherwise, if you are using Pipenv, you will want to first navigate inside your repository's root directory before installing Pytest:

```sh
cd path/to/my-repo/
pipenv install pytest --dev # NOTE: the --dev flag denotes this package will be used in development only
```

## Configuration

It helps to add a file called "conftest.py" to the root directory of your repository. This helps pytest find the application code and facilitates proper imports.

Another use for the "conftest.py" file is to store some code that needs to be shared across multiple test files. If you do this, your test files could access the code using an import statement like this: `from conftest import my_thing`.

## Usage

The Pytest package is generally used as a command-line utility for running pre-defined files of "test" code. Follow the ["Testing 1,2,3" Exercise](/exercises/testing-123/README.md) to get acclimated with Pytest.


Example invocations:

```sh
# run all tests:
pytest

# suppress warnings:
pytest --disable-pytest-warnings

# see print statements:
pytest  -s

# run a specific test:
pytest test/my_test.py

# run a specific function in a specific test:
pytest test/my_test.py -k 'test_my_thing'
```

### Expecting Errors

The Pytest package can be imported to facilitate assertions that errors will be raised:

```py
# this is an example test file...

import pytest

def test_divide_by_zero():
    with pytest.raises(Exception) as e_info:
        # we expect this code will raise an error (division by zero)
        result = 2 / 0
```

### Fixtures

If there is a time-intensive or memory-intensive operation used by multiple tests, we can use a "fixture" to perform that operation just once. This is a big time saver.

We'll generally place the fixtures in the same file as the tests that need them, but if multiple test files need to share the same fixture, we'll move it to the "conftest.py" file:

```py
# this is the "conftest.py" file (if fixtures need to be shared across multiple test files), 
# ... otherwise we can put the fixtures in the same test file where they are being used 

import pytest

# prevents unnecessary or duplicative language model loading
# fixture only loaded when a specific test needs it
# module-level fixture only invoked once for all tests
@pytest.fixture(scope="module")
def nlp():
    import spacy
    print("LOADING THE LANGUAGE MODEL...")
    return spacy.load("en_core_web_md")

# prevents unnecessary or duplicative network requests
# fixture only loaded when a specific test needs it
# module-level fixture only invoked once for all tests
@pytest.fixture(scope="module")
def parsed_response():
    import requests
    import json
    print("MAKING A NETWORK REQUEST...")
    response = requests.get("https://www.example.com/api/")
    return json.loads(response.text)

```


```py

# this is an example test file...

# using fixtures in tests (just pass them like magic as a param to the test function that needs them):

def test_my_language_model(nlp):
    # do something with the nlp fixture
    # assert something

def test_my_calculations(parsed_response):
    # do something with the parsed_response fixture
    # assert something
```


### Skipping Tests on CI

If your tests make real life network requests, we'll want to prevent that from happening on the CI server. Partially because we'll also want to avoid needing to configure any secret credentials on the CI server. Also because it keeps our test suite fast. 

To skip any test function, mark it to be skipped conditionally, if the `CI` environment variable is true. This environment variable is set by default on some CI servers, or you could configure your CI server to run tests with `CI=true pytest` instead of just `pytest` (to pass the environment variable that signals tests are being run on CI):

```py
# this is an example test file...

import os
import pytest

from app.my_file import fetch_data # this is a function that makes a real network request

@pytest.mark.skipif(os.getenv("CI")=="true", reason="avoid issuing HTTP requests on the CI server") # skips this test on CI
def test_fetch_data():
    data = fetch_data() # make a network request
    assert isinstance(data, list) # for example

```

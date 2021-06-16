# The `pytest` Package

> Prerequisite: [Automated Testing](/notes/software/testing.md)

Reference:

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
import pytest

def test_divide_by_zero():
    with pytest.raises(Exception) as e_info:
        # we expect this code will raise an error (division by zero)
        result = 2 / 0
```

### Fixtures

The Pytest package can be imported to facilitate the construction of test fixtures (for example, to be placed in the "conftest.py" file):

```py
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

# using fixtures in tests (just pass them like magic as a param to the test function that needs them):

def test_my_language_model(nlp):
    # do something with the nlp fixture

def test_my_calculations(parsed_response):
    # do something with the parsed_response fixture
```

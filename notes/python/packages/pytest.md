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
pytest

pytest --disable-pytest-warnings # disables warnings

pytest  -s #> see print statements

pytest test/parser_test.py -k 'test_my_thing' # test a certain file / function
```

### Fixtures

However, in addition, the Pytest package can be imported to facilitate the construction of test fixtures:


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

def test_my_thing(nlp):
    doc = nlp(reconstructed_text)
    # etc
```

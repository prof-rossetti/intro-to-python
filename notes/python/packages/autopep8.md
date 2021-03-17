
# The `autopep8` Package

The `autopep8` package "automatically formats Python code to conform to the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide."

Take these PEP-8 style suggestions with a grain of salt - don't feel obligated to adopt suggestions you don't like.

## Reference

  + https://pypi.org/project/autopep8/
  + https://github.com/hhatto/autopep8
  + http://pep8online.com/ (ALTERNATIVE RESOURCE)

## Installation

```sh
pip install autopep8
```

## Usage

First, ensure your code has been committed, because the `--in-place` flag will actually modify your files.

Then conduct a style check for a given file:

```sh
autopep8 --in-place path/to/my_script.py
```

FYI: the `--aggressive` flag enforces a stricter set of style rules, and the `--recursive` flag says to check all files in all subdirectories. So here is an alternative command to check all files aggressively:

```sh
autopep8 --in-place --aggressive --recursive .
```

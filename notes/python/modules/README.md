# Python Modules

In Python, a "module" is a file of Python code that can be "imported" and used in other Python files.

## Built-in Modules

Many helpful built-in modules are provided along with the [Standard Library](https://docs.python.org/3/library/). Here are some built-in modules of interest:

  + [The `os` Module](os.md)
  + [The `math` Module](math.md)
  + [The `random` Module](random.md)
  + [The `statistics` Module](statistics.md)
  + [The `itertools` Module](itertools.md)
  + [The `datetime` Module](datetime.md)
  + [The `time` Module](time.md)
  + [The `webbrowser` Module](webbrowser.md)
  + [The `json` Module](json.md)
  + [The `csv` Module](csv.md) -- although you're recommended to use [the `pandas` package](/notes/python/packages/pandas.md) instead!!

A built-in "module" is like a third-party "package" in the sense that it provides some code for us to import and leverage. But unlike third-party packages which need to be installed separately (often via `pip`), modules don't need to be installed separately (just imported).

## Local Modules

In addition to built-in modules, developers can create their own local Python modules. Separating our Python code across multiple files helps with code organization and maintainability.

Any other python file can import code from the module file as long as the module file meets a few organizational conditions (such as nesting the code under the "main" conditional).

For more practice, complete the ["Modules and Imports" Exercise](/exercises/modules-and-imports/README.md).

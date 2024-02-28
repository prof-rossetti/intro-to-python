# File Management

Use Python to read and write file contents, as well as to create and delete files.

Reference:

 + https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
 + https://docs.python.org/3/glossary.html#term-file-object
 + https://docs.python.org/3/library/io.html#module-io
 + https://www.tutorialspoint.com/python/python_files_io.htm

See also: [the `csv` module](modules/csv.md) for reading and writing CSV files, and [the `os` module](modules/os.md) for command-line-style file operations and functionality to help specify file paths.

To setup these examples, create a new directory on your Desktop called "file-mgmt" and navigate there from your command line. Create two Python scripts in that directory called "write_message.py" and "read_message.py", and place inside contents from the following sections, respectively.

## Writing Files

Write some Python strings to a text file called "my_message.txt" by running this script:

```python
# file-mgmt/write_message.py

file_name = "my_message.txt" # a relative filepath

with open(file_name, "w") as file: # "w" means "open the file for writing"
    file.write("Hello World")
    file.write("\n")
    file.write("\n")
    file.write("...")
    file.write("\n")
    file.write("\n")
    file.write("Hello Again")
```

```sh
python write_message.py
#> Hello World
#>
#> ...
#>
#> Hello Again
```

Inspect the contents of the "my_message.txt" file to see the message.

## Reading Files

Process the "my_message.txt" file into a Python string by running this script:

```python
# file-mgmt/read_message.py

file_name = "my_message.txt" # a relative filepath

with open(file_name, "r") as file: # "r" means "open the file for reading"
    contents = file.read()
    print(contents)
```

```sh
python read_message.py
#> Hello World.
#>
#> ...
#>
#> Hello Again
```

Further, it's possible to split the file contents on line break characters (`\n`) to assemble a Python list of strings, each representing its own line. Try revising the script and running it again:

```python
# file-mgmt/read_message.py

file_name = "my_message.txt"

with open(file_name, "r") as file:
    contents = file.read()
    lines = contents.split("\n") # converts string to list
    print("THERE ARE", len(lines), "LINES IN THIS FILE")
    for line in lines:
        print("LINE:", line)
```

```sh
python read_message.py
#> THERE ARE 5 LINES IN THIS FILE
#> LINE: Hello World
#> LINE:
#> LINE: ...
#> LINE:
#> LINE: Hello Again
```

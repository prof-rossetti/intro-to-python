# The `csv` Module

Reference: https://docs.python.org/3/library/csv.html.

Use the `csv` module to process data stored in Comma Separated Values (CSV) format.

To setup these examples, create a new directory on your Desktop called "csv-mgmt" and navigate there from your command line. Create two Python scripts in that directory called "write_teams.py" and "read_teams.py", and place inside contents from the following sections, respectively.

## Writing CSV Files

Write some Python dictionaries to a CSV file called "teams.csv" by running this script:

```python
# csv-mgmt/write_teams.py

import csv

csv_file_path = "teams.csv" # a relative filepath

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=["city", "name"])
    writer.writeheader() # uses fieldnames set above
    writer.writerow({"city": "New York", "name": "Yankees"})
    writer.writerow({"city": "New York", "name": "Mets"})
    writer.writerow({"city": "Boston", "name": "Red Sox"})
    writer.writerow({"city": "New Haven", "name": "Ravens"})
```

```sh
python write_teams.py
#> city,name
#> New York,Yankees
#> New York,Mets
#> Boston,Red Sox
#> New Haven,Ravens
```

## Reading CSV Files

Process the "teams.csv" file into some Python dictionaries by running this script:

```python
# csv-mgmt/read_teams.py

import csv

csv_file_path = "teams.csv" # a relative filepath

with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file) # assuming your CSV has headers
    # reader = csv.reader(csv_file) # if your CSV doesn't have headers
    for row in reader:
        print(row["city"], row["name"])
```

```sh
python read_teams.py
#> New York Yankees
#> New York Mets
#> Boston Red Sox
#> New Haven Ravens
```

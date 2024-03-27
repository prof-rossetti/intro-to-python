# The `gspread` Package

The `gspread` package provides an interface to Google Sheet documents via the Google Sheets and Google Drive APIs.

## Reference

Google APIs:

  + https://github.com/googleapis/google-api-python-client
  + https://developers.google.com/api-client-library/python/
  + https://developers.google.com/sheets/api/guides/authorizing

The `gspread` Package:

  + https://github.com/burnash/gspread
  + https://gspread.readthedocs.io/en/latest
  + https://gspread.readthedocs.io/en/latest/api.html
  + https://gspread.readthedocs.io/en/latest/api.html#client
  + https://gspread.readthedocs.io/en/latest/api.html#gspread.models.Spreadsheet
  + https://gspread.readthedocs.io/en/latest/api.html#gspread.models.Worksheet


This document was originally adapted from an excellent [blog post](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html).

## Installation

Installing the package, as necessary:

```sh
pip install gspread

# pip install gspread --upgrade
```

> NOTE: the example code below has been tested against `gspread==5.7.2` however the latest version in colab at the moment is older (`gspread==3.4.2`) and if you want to use the numericize_ignore parameter, you'll need to upgrade

## Setup

Create your own Google Sheet. Note the document's unique identifier from its URL (i.e. the `DOCUMENT_ID`).

Add some data to one of the sheets, and note the sheet name (i.e. the `SHEET_NAME`).

> NOTE: if you are developing locally and using a service account to access the Google Sheets API, you'll need to modify the document's sharing settings to grant "edit" privileges to the "client email" address specified in the service account credentials file. Otherwise, in colab, this step should not be necessary.


## Usage

### Authorization

The way we access Google Sheets API differs, based on the development environment.

#### Credentials in Colab

If working in a Colab notebook, we can login through the browser to obtain credentials:

```py
from google.colab import auth

# asks you to login with your google account
auth.authenticate_user()
```

```py
from google.auth import default

# uses your google account credentials
credentials, _ = default()
print(type(credentials)) #> <class 'google.auth.compute_engine.credentials.Credentials'>
```

```py
import gspread

client = gspread.authorize(credentials)
print("CLIENT:", type(client)) #> <class 'gspread.client.Client'>
```

#### Service Account Credentials

Otherwise, if working locally, we'll need to first configure [Google API service account credentials](/notes/devtools/google-apis.md#service-account-credentials), then download the service account credentials JSON file into the root directory of the repo as "google-credentials.json". Then we'll point to the path where that credentials file is located:

```py
import os

# you may need to modify the filepath based on its location relative to your Python script (see the `os` module notes)
GOOGLE_CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "google-credentials.json")

client = gspread.service_account(filename=GOOGLE_CREDENTIALS_FILEPATH)
print("CLIENT:", type(client)) #> <class 'gspread.client.Client'>
```


### Accessing the Document

Reading data from Google Sheets:

```py
# access the document:
doc = client.open_by_key(DOCUMENT_ID)
print("DOC:", type(doc), doc.title) #> <class 'gspread.models.Spreadsheet'>

# access a sheet within the document:
sheet = doc.worksheet(SHEET_NAME)
print("SHEET:", type(sheet), sheet.title)#> <class 'gspread.models.Worksheet'>
```

### Reading Data

Fetch all data from a given sheet (will be returned as a list of dictionaries):

```py
rows = sheet.get_all_records()
print("ROWS:", type(rows)) #> <class 'list'>
```

```sh
# NOTE: if your spreadsheet has string values that start with zeros (like "06510"),
# ... you may need to utilize the `numericise_ignore` parameter to keep the leading zeros
# ... this parameter is only available in newer versions of the gspread package.
# ... to use it, pass a list of integers representing the column indices (starting at 1)

# rows = sheet.get_all_records(numericise_ignore=[1])
```

### Writing Data

Writing data to Google Sheets:

```py
print("-----------------")
print("NEW ROW...")

new_row = {
    "id": 999,
    "name": f"Product 999",
    "department": "snacks",
    "price": 4.99,
}

# the sheet's insert_row() method wants our data to be in this format (see docs):
new_values = list(new_row.values()) #> [999, 'Product 999', 'snacks', 4.99]

# the sheet's insert_row() method wants us to pass the row number where this will be inserted (see docs):
next_row_number = len(rows) + 2 # number of records, plus a header row, plus one

# actually insert the data:
response = sheet.insert_row(new_values, next_row_number)

# see if it worked ok:
print("RESPONSE:", type(response)) #> dict
print(response) #> {'spreadsheetId': '____', 'updatedRange': "'MySheet'!A9:D9", 'updatedRows': 1, 'updatedColumns': 4, 'updatedCells': 4}
```

You can use `sheet.insert_row()` to insert one row at a time, or `sheet.insert_rows()` to insert multiple rows at a time (see the docs).

## Additional Examples

For more advanced usage, see the Professor's [Google Sheets App](https://github.com/prof-rossetti/flask-sheets-template-2023/blob/main/app/spreadsheet_service.py), as well as the examples below.

### Find or Create Sheet

Here is a function to find or create a given sheet:

```py
from gspread.exceptions import WorksheetNotFound

def find_or_create_sheet(sheet_name, doc=doc):
    """Access a sheet within the document, or create if not exists."""
    try:
        sheet = doc.worksheet(sheet_name)
    except WorksheetNotFound:
        print("CREATING NEW SHEET...")
        sheet = doc.add_worksheet(title=sheet_name, rows="10", cols="10")

    return sheet


sheet_name = "daily_prices_msft"
sheet = find_or_create_sheet(sheet_name)
print("SHEET:", type(sheet), sheet.title) #> <class 'gspread.models.Worksheet'>
```


### Writing DataFrames to Sheet

Here is an example function for overwriting sheet contents, using a pandas DataFrame:

```py
def write_data_to_sheet(df, sheet):
    """Write dataframe contents to a given sheet.
        Params df: a pandas DataFrame object.
    """
    header_row = df.columns.tolist()
    rows = df.values.tolist()
    assert len(header_row) == len(rows[0]) # same number of columns in all rows
    all_rows = [header_row] + rows

    sheet.clear()
    sheet.update(all_rows)


write_data_to_sheet(df, sheet)
```

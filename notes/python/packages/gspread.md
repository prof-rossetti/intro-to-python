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
  + https://gspread.readthedocs.io/en/latest/oauth2.html
  + https://gspread.readthedocs.io/en/latest/api.html

This document was originally adapted from an excellent [blog post](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html).

## Installation

First install the package (and a dependent auth-related package) using Pip, if necessary:

```sh
pip install gspread oauth2client
```

> NOTE: the example code below has been tested against `gspread==3.6.0`  and `oauth2client==4.1.3`

## Setup

### Downloading API Credentials

Visit the [Google Developer Console](https://console.developers.google.com/cloud-resource-manager). Create a new project, or select an existing one. Click on your project, then from the project page, search for the "Google Sheets API" and enable it. Also search for the "Google Drive API" and enable it.

From either API page, or from the [API Credentials](https://console.developers.google.com/apis/credentials) page, follow a process to create and download credentials to use the APIs:
  1. Click "Create Credentials" for a "Service Account". Follow the prompt to create a new service account named something like "spreadsheet-service", and add a role of "Editor".
  2. Click on the newly created service account from the "Service Accounts" section, and click "Add Key" to create a new "JSON" credentials file for that service account. Download the resulting .json file (this might happen automatically).
  3. Move a copy of the credentials file into your project repository, typically into the root directory or perhaps a directory called "auth", and note its filepath. For the example below, we'll refer to a file called "google-credentials.json" in an "auth" directory (i.e. "auth/google-credentials.json").

Finally, before committing, add the credentials filepath to your repository's ".gitignore" file to ensure it does not get tracked in version control or uploaded to GitHub:

```sh
# the .gitignore file

# ignore environment variables in the ".env" file:
.env

# ignore the google api credentials file at the following location:
auth/google-credentials.json
```

### Configuring Spreadsheet Document

Use this [example Google Sheet](https://docs.google.com/spreadsheets/d/1_hisQ9kNjmc-cafIasMue6IQG-ql_6TcqFGpVNOkUSE/edit#gid=0), or create your own. Note the document's unique identifier (e.g. `1_hisQ9kNjmc-cafIasMue6IQG-ql_6TcqFGpVNOkUSE`) from its URL, and store the identifier in an environment variable called `GOOGLE_SHEET_ID`.

If you create your own, make sure it contains a sheet called "Products-2021" with column headers `id`, `name`, `department`, `price`, and `availability_date`. If you choose a different sheet name, customize it via an environment variable called `SHEET_NAME`. Finally, modify the document's sharing settings to grant "edit" privileges to the "client email" address specified in the credentials file.

## Usage

### Authorization

To interface with the Google Sheets API, we'll first use our credentials to authorize an API client object, which provides certain capabilities:

```py
import os
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

DOCUMENT_ID = os.getenv("GOOGLE_SHEET_ID", default="OOPS")
SHEET_NAME = os.getenv("SHEET_NAME", default="Products-2021")

#
# AUTHORIZATION
#
# see: https://gspread.readthedocs.io/en/latest/api.html#gspread.authorize
# ... and FYI there is also a newer, more high level way to do this (see the docs)

# an OS-agnostic (Windows-safe) way to reference the "auth/google-credentials.json" filepath:
CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "google-credentials.json")

AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
print("CREDS:", type(credentials)) #> <class 'oauth2client.service_account.ServiceAccountCredentials'>

client = gspread.authorize(credentials)
print("CLIENT:", type(client)) #> <class 'gspread.client.Client'>
```

Reading sheet values:

```py

#
# READ SHEET VALUES
#
# see: https://gspread.readthedocs.io/en/latest/api.html#client
# ...  https://gspread.readthedocs.io/en/latest/api.html#gspread.models.Spreadsheet
# ...  https://gspread.readthedocs.io/en/latest/api.html#gspread.models.Worksheet

print("-----------------")
print("READING DOCUMENT...")

# access the document:
doc = client.open_by_key(DOCUMENT_ID)
print("DOC:", type(doc), doc.title) #> <class 'gspread.models.Spreadsheet'>

# access a sheet within the document:
sheet = doc.worksheet(SHEET_NAME)
print("SHEET:", type(sheet), sheet.title)#> <class 'gspread.models.Worksheet'>

# fetch all data from that sheet:
rows = sheet.get_all_records()
print("ROWS:", type(rows)) #> <class 'list'>

# loop through and print each row, one at a time:
for row in rows:
    print(row) #> <class 'dict'>
```

Writing to Google Sheets:

```py
#
# WRITE VALUES TO SHEET
#
# see: https://gspread.readthedocs.io/en/latest/api.html#gspread.models.Worksheet.insert_row

print("-----------------")
print("NEW ROW...")

auto_incremented_id = len(rows) + 1 # TODO: should change this to be one greater than the current maximum id value
new_row = {
    "id": auto_incremented_id,
    "name": f"Product {auto_incremented_id} (created from my python app)",
    "department": "snacks",
    "price": 4.99,
    "availability_date": "2021-02-17"
}
print(new_row)

print("-----------------")
print("WRITING VALUES TO DOCUMENT...")

# the sheet's insert_row() method wants our data to be in this format (see docs):
new_values = list(new_row.values()) #> [13, 'Product 13', 'snacks', 4.99, '2019-01-01']

# the sheet's insert_row() method wants us to pass the row number where this will be inserted (see docs):
next_row_number = len(rows) + 2 # number of records, plus a header row, plus one

# actually insert the data:
response = sheet.insert_row(new_values, next_row_number)

# see if it worked ok:
print("RESPONSE:", type(response)) #> dict
print(response) #> {'spreadsheetId': '____', 'updatedRange': "'Products-2021'!A9:E9", 'updatedRows': 1, 'updatedColumns': 5, 'updatedCells': 5}

```



## Service Account Credentials

Visit the [Google Developer Console](https://console.developers.google.com/cloud-resource-manager). Create a new project, or select an existing one. Click on your project, then from the project page, search for the "Google Sheets API" (or whatever API you need) and enable it.

From the [API Credentials](https://console.developers.google.com/apis/credentials) page, follow a process to create and download credentials to use the APIs:

  1. Click "Create Credentials" for a "Service Account". Follow the prompt to create a new service account named something like "spreadsheet-service", and add a role of "Editor".
  2. Click on the newly created service account from the "Service Accounts" section, and click "Add Key" to create a new "JSON" credentials file for that service account. Download the resulting .json file (this might happen automatically).
  3. Move a copy of the credentials file into your project repository, typically into the root directory, and name it "google-credentials.json".

Before you make a commit, remember to add the credentials filepath to the repository's ".gitignore" file, to ensure the secret credentials file is excluded from version control (to prevent it from being exposed on GitHub):

```sh
# the .gitignore file

# ignore environment variables in the ".env" file:
.env

# ignore the google api credentials file at the following location:
google-credentials.json

# ... etc.
```

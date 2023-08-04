# "Web App" Exercise (Financial Data Dashboards Version)

## Prerequisites

 + Local Development Exercise (Financial Version) -- converting a prototype notebook to a repository
 + [Codebase Cleanup Exercise (Financial Version)](/exercises/codebase-cleanup-2023/README.md)
 + Web Service Exercise (Financial Version) -- sending emails not necessary, but you'll want to have at least deployed the code to the server

## Learning Objectives

  + Create a basic web application in Python, using modular architecture.
  + Write routing logic to handle GET and POST requests, and respond by rendering HTML pages or returning JSON data.
  + Gain exposure to HTML templates, and using HTML forms to submit form data.
  + Run a web application in "development" using a local web server, and deploy to a user-facing "production" environment (i.e. a Heroku server).

## References

  + [The `flask` Package](/notes/python/packages/flask.md)
  + [HTTP Requests and Responses](/notes/info-systems/networks.md#HyperText-Transfer-Protocol)
  + [Basic HTML - W3Schools](https://www.w3schools.com/html/html_basic.asp)
  + [HTML Lists - W3Schools](https://www.w3schools.com/html/html_lists.asp)
  + [HTML Forms - W3Schools](https://www.w3schools.com/html/html_forms.asp)
  + [HTML Forms - Mozilla](https://developer.mozilla.org/en-US/docs/Learn/Forms)
  + [Sending and Retrieving Form Data - Mozilla](https://developer.mozilla.org/en-US/docs/Learn/Forms/Sending_and_retrieving_form_data)

## Prompt

So, you've created a command-line application. Now let's build a web application interface into your application's functionality!


## Instructions

### Setup

To use the Flask package, let's first add `flask` to the repo's "requirements.txt" file, then re-install packages:

```sh
pip install -r requirements.txt
```

### Guided Checkpoints

Now follow these sequential "checkpoints" to develop the Flask application from scratch, using an iterative process:

  1. [Checkpoint 1](checkpoint-1/) - Basic Routing, Rendering HTML pages
  2. [Checkpoint 2](checkpoint-2/) - Shared Layouts
  3. [Checkpoint 3](checkpoint-3/) - Twitter Bootstrap Layout
  4. [Checkpoint 4](checkpoint-4/) - Interactive Dashboards
  5. [Checkpoint 5](checkpoint-5/) - Automated Testing for Web Apps

For further reference, here is a [completed version history](https://github.com/s2t2/unemployment-2023-testing-prep/pull/1/commits) which implements these checkpoints. 

**Further Exploration**

For your reference, here are some Flask app templates which implement Google Login and fetch data from with datastores (Firebase and Google Sheets, respectively). Feel free to copy the templates and build on top of them for your final project, as desired:

  + [flask-firebase-template-2022](https://github.com/prof-rossetti/flask-firebase-template-2022)
  + [flask-sheets-starter-2023](https://github.com/prof-rossetti/flask-sheets-starter-2023) 
  + [flask-sheets-template-2023](https://github.com/prof-rossetti/flask-sheets-template-2023) 

### Running the Web App

FYI: we'll be running the application using the following Flask command (not a Python command):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or try a ".env" file approach
export FLASK_APP=web_app
flask run
```

To restart the server, press "ctrl+c" to stop it, and then re-run using the command above.

### Deploying to Production

See the [Deployment Checkpoint](deployment/). Add a copy of the provided "DEPLOYING.md" file to the root directory of your repo.

Update your "requirements.txt" file to include the `gunicorn` package, which will be used to run the app in production.

Save all files and make a commit and push the files to GitHub.

Finally, follow the instructions in the "DEPLOYING.md" guide to configure a Render server to host your app. Afterwards, you should be able to view your app in the browser and share the URL with friends and family.

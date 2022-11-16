# "Web App" Exercise (Financial Data Dashboards Version)

## Prerequisites

 + ["Web Service" Exercise](/exercises/web-service/README.md)

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
  3. [Checkpoint 3](checkpint-3/) - Twitter Bootstrap Layout
  4. [Checkpoint 4](checkpint-4/) - Interactive Dashboards
  5. [Checkpoint 5](checkpint-5/) - Automated Testing for Web Apps

Further exploration:

 + Google Login - see this [template repo](https://github.com/prof-rossetti/flask-firebase-template-2022) and feel free to build on top of it for your projects!!!

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

### Deploying to Production

> See also the [Deployment Checkpoint](deployment/!

Reference:
  + [Getting Started w/ Python - Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)
  + [Deploying Python Apps w/ Gunicorn - Heroku](https://devcenter.heroku.com/articles/python-gunicorn)

After completing all the checkpoints and demonstrating the ability to successfully run the web app locally, let's re-deploy the source code:

```sh
git push heroku main
```

Heroku says "no web process specified". They want us to create a specific file called the "Procfile" in the repo's root directory to instruct the Heroku server which command to invoke in order to run the web app:

```sh
# this is the Procfile (a Heroku config file)

web: gunicorn "web_app:create_app()"
```

Since we're instructing the server to use the "gunicorn" package (Heroku's preferred tool) to run the web app on production, we'll also need to add `gunicorn` to the "requirements.txt" file so it will be installed on the server during the deployment process.

After saving the "Procfile" and "requirements.txt" files, make a commit before re-attempting to re-deploy:

```sh
git push heroku main
```

View the server logs and troubleshoot as necessary:

```sh
heroku logs --tail
```

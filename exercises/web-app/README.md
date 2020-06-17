# "Web App" Exercise

> Prerequisites:
>   + [Software Products and Services](/units/unit-9.md)
>   + [The `flask` Package](/notes/python/packages/flask.md)
>   + [Web Service Exercise](/exercises/web-service/README.md), especially the deployment process

> FYI: this web application involves some basic HTML code. To gain familiarity with HTML and the Twitter Bootstrap front-end framework, see these resources:
>   + https://www.w3schools.com/html/html_basic.asp
>   + https://www.w3schools.com/html/html_forms.asp
>   + https://www.w3schools.com/html/html_tables.asp
>   + https://getbootstrap.com/docs/4.0/components/navbar/
>   + https://getbootstrap.com/docs/4.0/components/alerts/

## Learning Objectives

  + Practice leveraging third-party APIs and Python packages.
  + Practice security and privacy best practices by using a "dotenv" approach in conjunction with a ".gitignore" file.
  + Gain high-level exposure to basic HTML.
  + Learn how to use the Flask package to create a basic web application in Python.
  + Learn how to "deploy" a Python web application to a user-facing "production" environment, namely an application server hosted by Heroku, and configure the server to host the application publicly over the Internet.

## Instructions

So, you've [deployed a background web service](/exercises/web-service/README.md) to send you an email every day. But what if you wanted your information on-demand at the click of a button, without waiting for the next daily email? And what if you wanted to allow other people to register for your service? Let's build a web application interface into your application's functionality!

![](../../img/exercises/web-app/weather-form.png)

Follow along in class as the professor guides you through the process of building a web application from scratch.

### Solution

If you'd like to work ahead or asynchronously, you can reference this [Draft Pull Request in the Daily Briefings Repo](https://github.com/prof-rossetti/daily-briefings-py/pull/4) which includes a [step-by-step commit history](https://github.com/prof-rossetti/daily-briefings-py/pull/4/commits) and [comprehensive file diffs](https://github.com/prof-rossetti/daily-briefings-py/pull/4/files).

Or follow these written "checkpoints" sequentially:

  1. [Basic App](checkpoints/1-basic-app.md)
  2. [Application Factory](checkpoints/2-app-factory.md)
  3. [Rendering HTML Templates](checkpoints/3-render-template.md)
  4. [Shared HTML Layouts](checkpoints/4-shared-layout.md)
  5. [Bootstrap Layouts](checkpoints/5-bootstrap-layout.md)
  6. [Web Forms](checkpoints/6-forms.md), POST Requests, and Flash Messaging
  7. [Integrating Weather Functionality](checkpoints/7-integration.md)

### Setup

To use the Flask package, you'll need to add `Flask` to the "requirements.txt" file and re-install packages:

```sh
pip install -r requirements.txt
```

### Running Locally

Depending on the way a Flask app is organized, the run command will differ, but based on the provided organizational structure (with the `create_app()` function in the "web_app/\_\_init__.py" file), the following command should run web application locally so you can view it in a browser at localhost:5000:

```sh
# Mac:
FLASK_APP=web_app flask run

# Windows:
export FLASK_APP=web_app # first time, to set the env var
flask run # subsequent times
```

### Deploying to Production

> FYI: [Reference Code](https://github.com/s2t2/daily-briefings-py/pull/1/commits/efa9daf3c28bf083bce262526947155f6140ac58)

After demonstrating the ability to successfully run the web app locally, repeat the process that you followed when [deploying a web service](/exercises/web-service/deploying.md) to upload the source code onto a remote server:

```sh
git push heroku master
```

There are no scripts to be scheduled, so skip that part. Instead, you'll need to create a special file called the "Procfile" in the repo's root directory to instruct the Heroku server which command to invoke in order to run the app:

```sh
web: gunicorn "web_app:create_app()"
```

> NOTE: since we're instructing the server to use the "gunicorn" package (Heroku's preferred tool) to run the web app on production, we'll also need to add `gunicorn` to the "requirements.txt" file so it will be installed on the server during the deployment process.

Save the "Procfile" and "requirements.txt" files, and make a commit before re-attempting to deploy your app to the server.

```sh
git push heroku master
```

View the server logs and troubleshoot as necessary until you're able to see the weather forecast in the browser. Nice!

```sh
heroku logs --tail
```



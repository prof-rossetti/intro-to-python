# "Web App" Exercise

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
  + [Web Forms - W3Schools](https://www.w3schools.com/html/html_forms.asp)
  + [Web Forms - Mozilla](https://developer.mozilla.org/en-US/docs/Learn/Forms)
  + [Sending and Retrieving Form Data - Mozilla](https://developer.mozilla.org/en-US/docs/Learn/Forms/Sending_and_retrieving_form_data)

## Prompt

So, you've [deployed a background web service](/exercises/web-service/README.md) to send you an email every day. But what if you wanted the information on-demand at the click of a button, without waiting for the next daily email? And what if you wanted to allow other people to register for your service? Let's build a web application interface into your application's functionality!

![](../../img/exercises/web-app/weather-form.png)

## Instructions

### Setup

To use the Flask package, let's first add `Flask` to the Daily Briefing repo's "requirements.txt" file, then re-install packages:

```sh
pip install -r requirements.txt
```

### Guided Checkpoints

Now follow these sequential "checkpoints" for a guided walk-through of how to create a Flask application:

  1. [Routing (and Handling GET Requests)](checkpoints/1-routing.md)
  2. [Modular Organization](checkpoints/2-modular-org.md)
  3. [Rendering HTML Pages](checkpoints/3-render-template.md)
  4. [Web Forms (and Handling POST Requests)](checkpoints/4-web-forms.md)
  5. [Twitter Bootstrap Styling (and Flash Messaging)](checkpoints/5-bootstrap-layout.md)

### Deploying to Production

After completing all the checkpoints and demonstrating the ability to successfully run the web app locally, repeat the process we followed when [deploying the web service](/exercises/web-service/deploying.md) to upload an updated copy of the source code onto the server:

```sh
git push heroku main
```

There are no scripts to be scheduled, so skip that part. Instead, you'll need to create a special file called the "Procfile" in the repo's root directory to instruct the Heroku server which command to invoke in order to run the app:

```sh
web: gunicorn "web_app:create_app()"
```

> NOTE: since we're instructing the server to use the "gunicorn" package (Heroku's preferred tool) to run the web app on production, we'll also need to add `gunicorn` to the "requirements.txt" file so it will be installed on the server during the deployment process.

Save the "Procfile" and "requirements.txt" files, and make a commit before re-attempting to deploy your app to the server.

```sh
git push heroku main
```

View the server logs and troubleshoot as necessary until you're able to see the weather forecast in the browser. Nice!

```sh
heroku logs --tail
```

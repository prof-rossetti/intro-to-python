# "Web App" Exercise

> Prerequisites:
>   + [Software Products and Services](/units/unit-9.md)
>   + [The Open Weather API](https://home.openweathermap.org/api_keys) (sign up and obtain an API Key)
>   + [The `flask` Package](/notes/python/packages/flask.md)
>   + [Heroku](/notes/clis/heroku.md) (sign up for a account and install the Heroku CLI)
>   + [Web Service Exercise](/exercises/web-service/README.md), especially the deployment process

## Learning Objectives

  + Practice leveraging third-party APIs and Python packages.
  + Practice security and privacy best practices by using a "dotenv" approach in conjunction with a ".gitignore" file.
  + Learn how to "deploy" a Python web application to a user-facing "production" environment, namely an application server hosted by Heroku, and configure the server to host the application publicly over the Internet.

## Instructions

### Setup

Fork this Weather Web App repo (LINK TBA!!!) under your own control and then clone / download it onto your local computer.

Follow the README instructions to setup a virtual environment, install package dependencies, and configure environment variables.

### Running Locally

Continue following the README instructions to run web application locally and view it in a browser at localhost:5000.

### Deploying to Production

After demonstrating the ability to successfully run the web app locally, repeat the process that you followed when [deploying a web service](/exercises/web-service/deploying.md) to upload the source code onto a remote server and configure environment variables, etc.

There are no scripts to be scheduled, so skip that part. Instead, you'll need to create a special file called the "Procfile" in the repo's root directory to instruct the Heroku server which command to invoke in order to run the app:

```sh
web: gunicorn "web_app:create_app()"
```

> NOTE: since we're instructing the server to use the `gunicorn` package (Heroku's preferred tool) to run the web app on production, we'll also need to add that package to the "requirements.txt" file so it will be installed on the server during the deployment process.

Save the "Procfile" and "requirements.txt" files, and make a commit before re-attempting to deploy your app to the server.

View the server logs and troubleshoot as necessary until you're able to see the weather forecast in the browser. Nice!

## Evaluation

If you'd like to submit this exercise for evaluation, submit links to both your GitHub repo and your production app via the designated form.

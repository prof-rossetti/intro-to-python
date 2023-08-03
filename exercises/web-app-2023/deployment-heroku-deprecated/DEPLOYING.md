
# Deploying to Heroku (DEPRECATED)

> NOTE: heroku removed their free tier server, so we will use Render instead. Consult the [updated "deployment" checkpoint](../deployment/) for instructions.


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

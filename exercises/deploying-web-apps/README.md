# "Deploy a Web App to Production" Exercise

> Prerequisites:
>   + [Software Products and Services](/units/unit-9.md)
>   + [Heroku](/notes/clis/heroku.md) (sign up for a account, install the Heroku CLI, and login via the command line)
>   + ["Deploying Background Services" Exercise](/exercises/deploying-services/README.md) (FYI, contains more details about the deployment process)

## Learning Objectives

Learn how to "deploy" a Python web application to a "production" environment, namely an application server hosted by Heroku.

## Instructions

Fork this [Starter Web Application repo](https://github.com/prof-rossetti/web-app-starter-flask) under your own control and then clone / download it onto your local computer.

Follow the installation and usage instructions to demonstrate your ability to run the app locally in your browser at http://localhost:5000/.

Follow the deployment instructions to push your app to a server hosted by Heroku, then demonstrate your ability to visit the app on the Internet at its public address!

<hr>

## Further Exploration Challenges

### Deploying a Web App With a Google Sheets Datastore

Fork this [Starter Web Application w/ Google Sheets Datastore repo](https://github.com/prof-rossetti/web-app-starter-flask-sheets) under your own control and then clone / download it onto your local computer. Follow the installation and usage instructions to demonstrate your ability to run the app locally in your browser at http://localhost:5000/.

Follow the deployment instructions to push your app to a server hosted by Heroku, then demonstrate your ability to visit the app on the Internet at its public address!

### Configuring a Deploying a Web App from Scratch

So far both of the repositories referenced above already contain configuration files which allow them to be hosted on a Heroku server. This [Rock-Paper-Scissors Web App](https://github.com/prof-rossetti/rock-paper-scissors-flask) runs locally, but has not yet been deployed to a public-facing Heroku server. See if you can configure it to be deployed, and then deploy it.

Fork the repo under your own control and then clone / download it onto your local computer. Follow the installation and usage instructions to demonstrate your ability to run the app locally in your browser at http://localhost:5000/.

Figure out how to push your app to a server hosted by Heroku, then demonstrate your ability to visit the app on the Internet at its public address!

> HINT: you'll need to add a special file called the "Procfile" to instruct the Heroku server which function to invoke in order to run the app (see examples in those other repos). Example "Procfile":
>
>     web: gunicorn "web_app:create_app()"
>
> NOTE: Since you're instructing the server to use the `gunicorn` package (Heroku's preferred tool) to run the web app, you'll also need to add that package to the "requirements.txt" file so it will be installed on the server during the deployment process.

# "Web Service" (a.k.a. "Daily Briefings") Exercise

Write a Python application to send yourself an email containing information of interest, like an up-to-date hourly weather forecast. Then deploy the application to a remote server and schedule the server to send you the email at the same time every morning.

> Prerequisites:
>   + [Software Products and Services](/units/unit-9.md)
>   + [The Open Weather API](https://home.openweathermap.org/api_keys) (sign up and obtain an API Key)
>   + [The `requests` Package](/notes/python/packages/requests.md), revisited
>   + [The SendGrid API](https://app.sendgrid.com/settings/api_keys), revisited (sign up and obtain an API Key)
>   + [The `sendgrid` Package](/notes/python/packages/sendgrid.md), revisited
>   + [Heroku](/notes/clis/heroku.md) (sign up for a account and install the Heroku CLI)

This exercise is inspired by a [project](https://github.com/mgallea/daily-email) by former student @mgallea.

## Learning Objectives

  + Practice leveraging third-party APIs and Python packages.
  + Practice security and privacy best practices by using a "dotenv" approach in conjunction with a ".gitignore" file.
  + Gain high-level exposure to basic HTML.
  + Learn how to "deploy" a Python script to a user-facing "production" environment, namely an application server hosted by Heroku, and schedule the server to execute the script at regular intervals.

## Instructions

### Setup

Fork this [Daily Briefings repo](https://github.com/prof-rossetti/daily-briefings-py) under your own control and then clone / download it onto your local computer.

Follow the README instructions to setup the virtual environment, install package dependencies, and configure environment variables.

### Running Locally

Continue following the README instructions to run each of the Python scripts locally and see them produce their desired results. Check your email inbox to verify you are receiving the emails.

> FYI: the email content is being formatted as HTML. For any students who are not familiar with HTML, see this [Quick HTML Reference](https://www.w3schools.com/html/html_basic.asp)!

### Deploying to Production

After demonstrating the ability to successfully run the app locally, follow these [Deployment Instructions](deploying.md) to upload the source code onto a remote server and configure the server to send you an email at scheduled (e.g. daily) intervals.


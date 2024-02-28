# "Web Service" Exercise

## Learning Objectives

  + Deploy a Python script to a user-facing "production" environment (i.e. a remote application server hosted by Heroku).
  + Schedule a remote server to execute a specified Python application at specified intervals (i.e. once per day)
  + Gain exposure to basic HTML.

## Instructions

### Setup

Make a copy of the professor's [Daily Briefings repo template](https://github.com/prof-rossetti/daily-briefings-py), then clone / download your copy onto your local computer.

Follow the README instructions to setup the virtual environment, install package dependencies, and configure environment variables.

### Running Locally

Continue following the README instructions to run each of the Python scripts locally and see them produce their desired results. Check your email inbox to verify you are receiving the emails.

> FYI: the email is getting sent via SendGrid. For more info, see these notes about the [the `sendgrid` package](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/sendgrid.md).

> FYI: the email content is being formatted as HTML. For any students who are not familiar with HTML, see these reference documents about [Basic HTML](https://www.w3schools.com/html/html_basic.asp) and [HTML Lists](https://www.w3schools.com/html/html_lists.asp)!

### Deploying to Production

After demonstrating the ability to successfully run the app locally, follow the app's [Deployment Instructions](https://github.com/prof-rossetti/daily-briefings-py/blob/main/DEPLOYING.md) to upload the source code onto a remote server and configure the server to send you an email at scheduled (e.g. daily) intervals.

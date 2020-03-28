# "Web Service" (a.k.a. "Morning Briefings") Exercise

> Prerequisites:
>   + [Software Products and Services](/units/unit-9.md)
>   + [The `requests` Package](/notes/python/packages/requests.md), revisited
>   + [The `sendgrid` Package](/notes/python/packages/sendgrid.md), including the setup instructions
>   + [Heroku](/notes/clis/heroku.md) (sign up for a account, install the Heroku CLI, and login via the command line)

## Learning Objectives

  + Practice leveraging third-party APIs and Python packages.
  + Practice security and privacy best practices by using a "dotenv" approach in conjunction with a ".gitignore" file.
  + Learn how to "deploy" a Python script to a user-facing "production" environment, namely an application server hosted by Heroku, and schedule the server to execute the script at regular intervals.

## Instructions

### Setup

Create a new repo on GitHub called something like "morning-briefings". Clone it onto your local computer (for example to your Desktop) and navigate there from the command-line:

```sh
cd ~/Desktop/morning-briefings/
```

Create an "app" directory with three files inside called "stocks_service.py", "weather_service, and "email_service.py", respectively, and place the following contents inside:

```py
# app/stocks_service.py

# TODO
```

```py
# app/weather_service.py

# TODO
```

```py
# app/email_service.py

# TODO
```

Create another file in the "app" directory called "daily_briefing.py", and place the following contents inside:

```py
# app/daily_briefing.py

# TODO
```

Create a "requirements.txt" file in the root directory, and place inside the following contents:

```sh
# requirements.txt
python-dotenv
requests
```

Create a ".env" file in the root directory and place configuration variables and secret credentials inside:

```sh
# .env

MY_ZIP_CODE="_______"
MY_FAVORITE_STOCKS="MSFT,TSLA,GOOG,WORK"
MY_EMAIL_ADDRESS="________"

WEATHER_API_KEY="_____"
SENDGRID_API_KEY="________"
```

Create a ".gitignore" file in the root directory and place the following contents inside:

```sh
# .gitignore

# ignore hidden files (Mac OS only):
.DS_Store

# ignore secret credentials in the ".env" file:
.env
```

Make sure to save all the files, then make a commit with a message like "Setup repo".

### Running Locally

Create and activate a new Anaconda virtual environment, perhaps named "briefings-env":

```sh
conda create -n briefings-env python=3.7
conda activate briefings-env
```

Then, from within the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

From within the virtual environment, ensure you can run each of the files and see them produce their desired results of: printing the latest closing prices, printing today's weather forecast, and sending an example email, respectively.

```sh
python app/stocks_service.py
#> THE LATEST CLOSING PRICE IS ...
```

```sh
python app/weather_service.py
#> TODAY'S WEATHER FORECAST IS ...
```

```sh
python app/email_service.py
#> SENDING EMAIL TO ...
```

> NOTE: the Sendgrid emails might first start showing up in spam, until you designate them as coming from a trusted source

Also demonstrate your ability to send the daily briefing email:

```sh
python app/daily_briefing.py
```

### Deploying to Production

After getting the app running locally, follow these [Deployment Instructions](deploying.md) to deploy it to a remote server and schedule it to run at regular (e.g. daily) intervals.

## Evaluation

Category | Description | Weight
--- | --- | ---
A | lorum | 20%
B | ipsum | 20%

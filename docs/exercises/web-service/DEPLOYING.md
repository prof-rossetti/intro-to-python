# Deploying to Heroku

> NOTE: this is to be used specifically in conjunction with the [Web Service exercise](README.md).

## Prerequisites

If you haven't yet done so, [sign up for a Heroku account](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/heroku.md#prerequisites) and [install the Heroku CLI](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/heroku.md#installation), and make sure you can login and list your applications.

```sh
heroku login # just a one-time thing when you use heroku for the first time

heroku apps # at this time, results might be empty-ish
```

> NOTE: some students have reported that when running `heroku login` in Git Bash, it hangs after successfully logging them in. If this is the case for you, close that Git Bash window and when you open a new one you should be all set.

## Server Setup

> IMPORTANT: run the following commands from the root directory of your repository!

Use the online [Heroku Dashboard](https://dashboard.heroku.com/) or the command-line (instructions below) to [create a new application server](https://dashboard.heroku.com/new-app), specifying a unique name (e.g. "notification-app-123", but yours will need to be different):

```sh
heroku create notification-app-123 # choose your own unique name!
```

Verify the app has been created:

```sh
heroku apps
```

Also verify this step has associated the local repo with a remote address called "heroku":

```sh
git remote -v
```

## Server Configuration

Before we copy the source code to the remote server, we need to configure the server's environment in a similar way we configured our local environment.

Instead of using a ".env" file, we will directly configure the server's environment variables by either clicking "Reveal Config Vars" from the "Settings" tab in your application's Heroku dashboard, or from the command line (instructions below):

![a screenshot of setting env vars via the app's online dashboard](https://user-images.githubusercontent.com/1328807/54229588-f249e880-44da-11e9-920a-b11d4c210a99.png)

```sh
# or, alternatively...

# get environment variables:
heroku config # at this time, results might be empty-ish

# set environment variables:
heroku config:set APP_ENV="production"

heroku config:set SENDGRID_API_KEY="_________"
heroku config:set SENDER_EMAIL_ADDRESS="someone@gmail.com"

heroku config:set COUNTRY_CODE="US"
heroku config:set ZIP_CODE="20057"
heroku config:set USER_NAME="Jon Snow"
```

At this point, you should be able to verify the production environment has been configured with the proper environment variable values:

```sh
heroku config
```

## Deploying

After this configuration process is complete, you are finally ready to "deploy" the application's source code to the Heroku server:

```sh
git push heroku main
```

> NOTE: any time you update your source code, you can repeat this deployment command to upload your new code onto the server

## Running the Script in Production

Once you've deployed the source code to the Heroku server, login to the server to see the files there, and take an opportunity to test your ability to run the script that now lives on the server:

```sh
heroku run bash # login to the server
# ... whoami # see that you are not on your local computer anymore
# ... ls -al # optionally see the files, nice!
# ... python -m app.daily_briefing # see the output, nice!
# ... exit # logout

# or alternatively, run it from your computer, in "detached" mode:
heroku run "python -m app.daily_briefing"
```

## Scheduling the Script

Finally, provision and configure the server's "Heroku Scheduler" resource to run the notification script at specified intervals, for example once per day.

From the "Resources" tab in your application's Heroku dashboard, search for an add-on called "Heroku Scheduler" and provision the server with a free plan.

![a screenshot of searching for the resource](https://user-images.githubusercontent.com/1328807/54228813-59ff3400-44d9-11e9-803e-21fbd8f6c52f.png)

![a screenshot of provisioning the resource](https://user-images.githubusercontent.com/1328807/54228820-5e2b5180-44d9-11e9-9901-13c538a73ac4.png)

> NOTE: if doing this for the first time, Heroku may ask you to provide billing info. Feel free to provide it, as the services we are using to complete this exercise are all free, and your card should not be charged!

Finally, click on the provisioned "Heroku Scheduler" resource from the "Resources" tab, then click to "Add a new Job". When adding the job, choose to execute the designated python command (`python -m app.daily_briefing`) at a scheduled interval (e.g. every 10 minutes), and finally click to "Save" the job:

![a screenshot of the job configuration menu](https://user-images.githubusercontent.com/1328807/54229044-da259980-44d9-11e9-91d8-51773499cbfb.png)


## It's Alive!

Congratulations, you have just deployed a software service!

Monitor your inbox over the specified time period and witness your notification service in action!

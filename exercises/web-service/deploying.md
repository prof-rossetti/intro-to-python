# Deploying a Background Web Service to Heroku

## Prerequisites

If you haven't yet done so, [install the Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install), and make sure you can login and list your applications.

```sh
heroku login

heroku apps:list # at this time, results might be empty-ish
```

## Server Setup

Use the online [Heroku Dashboard](https://dashboard.heroku.com/) or the command-line (instructions below) to [create a new application server](https://dashboard.heroku.com/new-app), specifying a unique name (e.g. "notification-app-123", but yours will need to be different):

![a screenshot of a Heroku web form asking the user to choose a new application name](https://user-images.githubusercontent.com/1328807/54228060-b7928100-44d7-11e9-969e-817eb219f1c9.png)

```sh
# or, alternatively:
heroku apps:create notification-app-123
```

Verify the app has been created:

```sh
heroku apps:list
```

If you created the application server from the command-line within your project repository, this process might have already automatically associated the repository with that server's remote address. Check to see whether you see a remote address called "heroku":

```sh
git remote -v
```

If you don't already see the remote address called "heroku", manually create this association now:

```sh
heroku git:remote -a notification-app-123
```

At this point, you should be able to verify the repository is configured with a remote address called "heroku":

```sh
git remote -v
```

## Server Configuration

Before we copy the script to the remote server, we need to configure the server's environment in a similar way we configured our local environment. But instead of using a ".env" file, we will directly configure the server's environment variables by either clicking "Reveal Config Vars" from the "Settings" tab in your application's Heroku dashboard, or from the command line (instructions below):

![a screenshot of setting env vars via the app's online dashboard](https://user-images.githubusercontent.com/1328807/54229588-f249e880-44da-11e9-920a-b11d4c210a99.png)

```sh
# or, alternatively...

# get environment variables:
heroku config -a notification-app-123 # at this time, results might be empty-ish

# set environment variables:
heroku config:set SENDGRID_API_KEY="abc123" -a notification-app-123
heroku config:set MY_EMAIL_ADDRESS="someone@gmail.com" -a notification-app-123
# etc...
```

At this point, you should be able to verify the production environment has been configured with the proper environment variable values:

```sh
heroku config -a notification-app-123
```

## Deploying

After this configuration process is complete, you are finally ready to "deploy" the application's source code to the Heroku server:

```sh
git push heroku master
```

## Running the Script

Once you've deployed the source code to the Heroku server, login to the server to see the files there, and take an opportunity to test your ability to run the script that now lives on the server:

```sh
heroku run bash -a notification-app-123 # login to the server
ls -al # optionally see the files, nice!
python app/send_email.py # see the output, nice!
exit # logout

# or alternatively, without the login and logout steps:
heroku run "python app/send_email.py" -a notification-app-123
```

## Scheduling the Script

Finally, provision and configure the server's "Heroku Scheduler" resource to run the notification script at specified intervals, for example once per day.

From the "Resources" tab in your application's Heroku dashboard, search for an add-on called "Heroku Scheduler" and provision the server with a free plan.

![a screenshot of searching for the resource](https://user-images.githubusercontent.com/1328807/54228813-59ff3400-44d9-11e9-803e-21fbd8f6c52f.png)

![a screenshot of provisioning the resource](https://user-images.githubusercontent.com/1328807/54228820-5e2b5180-44d9-11e9-9901-13c538a73ac4.png)


Finally, click on the provisioned "Heroku Scheduler" resource from the "Resources" tab, then click to "Add a new Job". When adding the job, choose to execute the "app/send_email.py" script at a scheduled interval (e.g. every 10 minutes), and finally click to "Save" the job:

![a screenshot of ](https://user-images.githubusercontent.com/1328807/54229044-da259980-44d9-11e9-91d8-51773499cbfb.png)


## It's Alive!

Congratulations, you have just deployed a software service!

Monitor your inbox over the specified time period and witness your notification service in action!

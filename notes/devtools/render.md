
# Deploying to Render

Follow this guide if you would like to deploy / host your web application on a free server provided by the Render platform.

References:
  + https://render.com/docs/deploy-flask

## Prerequisites

This guide assumes you have a flask web application defined in the "web_app" directory of your repo, specifically in the directory's "\__init\__.py" file, within a function called `create_app`.

Before deploying, take a moment to add `gunicorn` to the repository's "requirements.txt" file. Save the file, make a commit, and push your code up to GitHub.

## Render Setup

Login to [Render](https://dashboard.render.com) and visit the dashboard.

Create a New "Web Service". 

Specify the URL of your repository (under the Public Git Repository tab).

Specify start command referencing the "web_app" directory:

```
gunicorn "web_app:create_app()"
```

Choose instance type of "free".

Under the "Advanced" options, set any environment variables that your app requires, as necessary.

Finally, click "Deploy web service". This will trigger a build. Since we are using the free server option, it might take a few moments for the deployment to complete. 

## Render Deploys

Whenever you push new code to the designated branch in your GitHub repository, it will trigger a new deployment to update your hosted site.

You can also trigger builds manually.

After a deployment build has finished, you should be able to view the updated app at the URL provided in the top left (i.e. `https://YOUR_APP.onrender.com/`).

Note that since we are using a free server, it may take a few moments to show up in the browser when you first visit the URL.

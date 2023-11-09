# GitHub Actions

We can use GitHub actions for continuous integration purposes, to run our automated tests and other automated checks.


## Configuration / Setup

We'll need to setup our repository with a config file at location ".github/workflows/python-app.yml".

From your repo's "Actions" tab, add an action called "Python application". Conclude the commit to add a config file (".github/workflows/python-app.yml") to the remote repo.

Pull the changes to update your local repo to include this config file as well, before proceeding.

For further customization of the config file, see these [examples](examples). 

If your app uses environment variables, you'll need to add them as repository secrets and update your build file to reference the secrets (see ["app with secrets" example](examples/app_with_secrets.yml)), with pertenent section copied below:

```yml
    - name: Test with pytest
      env:
        # set environment variables to use during testing
        # ... using the repository secret values set securely via repo settings
        MY_API_KEY: ${{ secrets.MY_API_KEY }}
        MY_API_SECRET: ${{ secrets.MY_API_SECRET }}
      run: |
        pytest
```

## Badge

After you have setup GitHub Actions for CI, consider adding a [workflow status badge](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge) to your README as well.

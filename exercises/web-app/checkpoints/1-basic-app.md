
# Web App Checkpoint 1 - Basic App

After installing the Flask package, let's read the [Flask Quick Start Guide](https://flask.palletsprojects.com/en/1.1.x/quickstart/) and see what it wants us to do.

We find an example like this, so let's try it out:

```py
# hello.py (root dir of repo)

from flask import Flask

app = Flask(__name__)

# route: a URL path to visit
# route function names should be unique hello_world() vs about()

@app.route("/")
def hello_world():
    print("VISITED THE HELLO PAGE")
    return "Hello, World!"
```

We'll run the file like this:

```sh
# mac:
FLASK_APP=hello.py flask run

# windows:
export FLASK_APP=hello.py
flask run
```

> NOTE: on Windows, if `export` doesn't work for you, try `set`

This command starts a local web server. Visit localhost:5000 in the browser to see the app in action!

Try adding another route:

```py
# hello.py (root dir of repo)

# ...

@app.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    return "About me!"
```

Any time you modify the code you'll need to restart the web server via "ctrl+c". And restart it again.

View "localhost:5000" and "localhost:5000/about" in the browser.

Nice, you've got the routing down.

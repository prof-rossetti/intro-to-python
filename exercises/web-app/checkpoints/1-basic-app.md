
# Web App Step 1 - Routing

After installing the Flask package, let's read the [Flask Quick Start Guide](https://flask.palletsprojects.com/en/1.1.x/quickstart/) and see what it wants us to do.

We find an example like the one below. Let's temporarily create a new file called "hello.py" in the root directory of the repo, and place the following contents inside:

```py
# hello.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("VISITED THE HOME PAGE")
    return "Hello, World!"

@app.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    return "About me!"
```

> NOTE: Flask route function names must be unique.

Later when we move and re-organize our application we'll need to run it differently, but for now with the "hello.py" file we can run it from the root directory like this:

```sh
# Mac OS:
FLASK_APP=hello.py flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
export FLASK_APP=hello.py
flask run
```

This command starts a local web server on port 5000. Preview the app in the browser by visiting "localhost:5000" and then "localhost:5000/about".

> NOTE: whenever we modify the code we'll need to stop the web server via "ctrl+c", and start it again before previewing again.

Nice, you've got the routing down.

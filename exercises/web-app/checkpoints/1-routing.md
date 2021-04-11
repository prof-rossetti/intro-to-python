
# Checkpoint 1: Routing

## Quick Start

After installing the Flask package, let's read the [Flask Quick Start Guide](https://flask.palletsprojects.com/en/1.1.x/quickstart/) and see what it wants us to do.

We find an example like the one below. Let's temporarily create a new file called "hello.py" in the root directory of the repo, and place the following contents inside:

```py
# hello.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"
```

> NOTE: We are using a [function decorator](https://www.python.org/dev/peps/pep-0318/) to specify the route (i.e. the path we visit in the browser).

> NOTE: Flask route function names like `hello_world()` must be unique.

Later when we move and re-organize our application we'll need to run it differently, but for now with the "hello.py" file we can run it from the root directory like this:

```sh
# Mac OS:
FLASK_APP=hello.py flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
export FLASK_APP=hello.py
flask run
```

This command starts a local web server on port 5000. Preview the app by visiting "localhost:5000" in the browser. Nice, the web server is running and responding to our request.

> NOTE: whenever we modify the code we'll need to stop the web server via "ctrl+c", and start it again before previewing again.

## More Routes

Let's add more routes.


```py
# hello.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    print("HOME...")
    return "Welcome Home"

@app.route("/about")
def about():
    print("ABOUT...")
    return "About Me"

@app.route("/hello")
@app.route("/hello.json")
def hello_world():
    print("HELLO...", dict(request.args))
    name = request.args.get("name") or "World"
    message = f"Hello, {name}!"

    if ".json" in request.url:
        return jsonify({"message": message})
    else:
        return message

@app.route("/api/books.json")
def list_books():
    print("BOOKS...")
    books = [
        {"title": "Book 1", "year": 1957},
        {"title": "Book 2", "year": 1990},
        {"title": "Book 3", "year": 2031},
    ]
    return jsonify(books)

```

After restarting the server, visit "localhost:5000", "localhost:5000/about", and "localhost:5000/hello" in the browser. Nice, the server is handling requests to different routes!

### Handling URL Parameters

Next visit "localhost:5000/hello?name=Vijay" in the browser. By doing so, we are now passing a URL parameter called "name" to the server along with our request.

Notice how our "hello" route is using the `request` object from Flask, specifically looking at its `args` property (i.e. `request.args`) to get the URL params. NOTE: This will be a dictionary-like object. FYI: here we're using the dictionary's  `get()` method (i.e. `request.args.get()` to safely access a dictionary key and avoid an error if the key is not present, and we're using `or` to provide a default back-up value.

Visit the same route, but specify a different name in the URL parameters, to see the response content dynamically change. Nice, we are detecting URL parameters!

> FYI: We can use `%20` to escape space characters in our request's URL params. Visit a route like "localhost:5000/hello?name=Jon%20Snow" to test this out.

### Responding with JSON

Finally, visit "localhost:5000/hello.json" and "localhost:5000/api/books.json" in the browser.

Notice how we are using the `jsonify` method from Flask to convert a Python list or dictionary to JSON data.

Wow we just made our own JSON API. Nice.

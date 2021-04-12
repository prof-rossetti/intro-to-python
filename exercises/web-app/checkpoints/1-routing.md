
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

This command starts a local web server on port 5000. Preview the app by visiting http://localhost:5000 in the browser. Nice, the web server is running and responding to our request.

> NOTE: whenever we modify the code we'll need to stop the web server via "ctrl+c", and start it again before previewing again.

## More Routes

Let's add more routes.


```py
# hello.py

from flask import Flask, request, jsonify

app = Flask(__name__)

#
# HOME ROUTES
#

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
def hello_world():
    print("HELLO...", dict(request.args))
    # NOTE: `request.args` is dict-like, so below we're using the dictionary's `get()` method,
    # ... which will return None instead of throwing an error if key is not present
    # ... see also: https://www.w3schools.com/python/ref_dictionary_get.asp
    name = request.args.get("name") or "World"
    return f"Hello, {name}!"

#
# BOOK ROUTES
#

@app.route("/api/books")
@app.route("/api/books.json")
def list_books():
    print("BOOKS...")
    books = [
        {"id": 1, "title": "Book 1", "year": 1957},
        {"id": 2, "title": "Book 2", "year": 1990},
        {"id": 3, "title": "Book 3", "year": 2031},
    ] # some dummy / placeholder data
    return jsonify(books)

@app.route("/api/books/<int:book_id>")
@app.route("/api/books/<int:book_id>.json")
def get_book(book_id):
    print("BOOK...", book_id)
    book = {"id": book_id, "title": f"Example Book", "year": 2000} # some dummy / placeholder data
    return jsonify(book)
```

After restarting the server, visit the following URLs in the browser:
  + http://localhost:5000
  + http://localhost:5000/home
  + http://localhost:5000/about


Review the code that handles these "index" and "about" routes. What do you notice?

Nice, our app is handling requests to different routes!

### Handling URL Parameters

Visit the following URLs in the browser, and notice we are now passing a URL parameter called "name" along with our requests:

  + http://localhost:5000/hello
  + http://localhost:5000/hello?name=Jim
  + http://localhost:5000/hello?name=Jane
  + http://localhost:5000/hello?name=Jon%20Snow

> FYI: the `%20` character acts as a space character in the URL params

Review the code that handles the "hello" route. Notice the "hello" route referencing the `request` object from Flask, specifically looking at its `args` property (i.e. `request.args`), a dictionary-like object, to access the URL params.

Nice, our app is dynamically handling different URL parameters!

### Responding with JSON

Finally, visit the following urls in the browser:
  + http://localhost:5000/api/books.json
  + http://localhost:5000/api/books/100.json
  + http://localhost:5000/api/books/oops.json

Review the code that handles these "book" routes. Notice how we are using the `jsonify` method from Flask to convert a Python list or dictionary to a JSON response.

Wow, we've just made our own JSON API (although with limited functionality so far).

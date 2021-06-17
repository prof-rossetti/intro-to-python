
# Checkpoint 2: Routing

## New Routes

First, update the "home_routes.py" file to define another route there:

```py
# web_app/routes/home_routes.py

# ...

@home_routes.route("/hello")
def hello_world():
    print("HELLO...", dict(request.args))
    # NOTE: `request.args` is dict-like, so below we're using the dictionary's `get()` method,
    # ... which will return None instead of throwing an error if key is not present
    # ... see also: https://www.w3schools.com/python/ref_dictionary_get.asp
    name = request.args.get("name") or "World"
    message = f"Hello, {name}!"
    return message
    #return render_template("hello.html", message=message)

```

Next, inside the "routes" directory, create new files called "book_routes.py" and "weather_routes.py", and place the following contents inside, respectively:

```py
# web_app/routes/book_routes.py

from flask import Blueprint, jsonify

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/api/books")
@book_routes.route("/api/books.json")
def list_books():
    print("BOOKS...")
    books = [
        {"id": 1, "title": "Book 1", "year": 1957},
        {"id": 2, "title": "Book 2", "year": 1990},
        {"id": 3, "title": "Book 3", "year": 2031},
    ] # some dummy / placeholder data
    return jsonify(books)

@book_routes.route("/api/books/<int:book_id>")
@book_routes.route("/api/books/<int:book_id>.json")
def get_book(book_id):
    print("BOOK...", book_id)
    book = {"id": book_id, "title": f"Example Book", "year": 2000} # some dummy / placeholder data
    return jsonify(book)

```

```py
# web_app/routes/weather_routes.py

from flask import Blueprint, request, jsonify

from app.weather_service import get_hourly_forecasts

weather_routes = Blueprint("weather_routes", __name__)

@weather_routes.route("/weather/forecast.json")
def weather_forecast_api():
    print("WEATHER FORECAST (API)...")
    print("URL PARAMS:", dict(request.args))

    country_code = request.args.get("country_code") or "US"
    zip_code = request.args.get("zip_code") or "20057"

    results = get_hourly_forecasts(country_code=country_code, zip_code=zip_code)
    if results:
        return jsonify(results)
    else:
        return jsonify({"message":"Invalid Geography. Please try again."}), 404

```


Finally, to let our app know about these new routes, let's un-comment the related "import" and "register" lines from the web app's "\_\_init_\_.py" file.

### Handling URL Parameters

Restart the server, and visit the following URLs in the browser. Notice we are now passing an optional URL parameter called "name" along with our requests:

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
  + http://localhost:5000/api/books/OOPS.json
  + http://localhost:5000/weather/forecast.json
  + http://localhost:5000/weather/forecast.json?country_code=US&zip_code=10012
  + http://localhost:5000/weather/forecast.json?country_code=US&zip_code=OOPS

Review the code that handles these "book" routes. Notice how we are using the `jsonify` method from Flask to convert a Python list or dictionary to a JSON response.

Wow, we've just made our own JSON API!

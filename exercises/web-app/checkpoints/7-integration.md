# Web App Checkpoint 7 - Integrating Weather Functionality

> FYI: [Reference Code](https://github.com/s2t2/daily-briefings-py/pull/1/commits/26299ec21548b3d9465b78e11f8ff5e4e17a77b8)

Alright, we've demonstrated our ability to send and receive data via a web form. Now let's apply that approach to integrating our weather functionality.

Let's create a web form with a text input element to allow the user to specify their given zip code. In the templates directory, add a new HTML file called "weather_form.html" and place inside the following contents:

```html
{% extends "bootstrap_layout.html" %}
{% set active_page = "weather_form" %}

{% block content %}

    <h2>Weather Form</h2>

    <p>Request an hourly forecast for your zip code...</p>

    <form action="/weather/forecast" method="POST">

        <label>Zip Code:</label>
        <input type="text" name="zip_code" placeholder="20057" value="20057">
        <br>

        <button>Submit</button>
    </form>

{% endblock %}
```

Here we're saying when the user submits the form, we'll send their zip code via POST request to a new route called "/weather/forecast", so let's set up our weather routes now:

```py
# web_app/routes/weather_routes.py

from flask import Blueprint, render_template, request

from app.weather_service import get_hourly_forecasts

weather_routes = Blueprint("weather_routes", __name__)

@weather_routes.route("/weather/form")
def weather_form():
    print("VISITED THE WEATHER FORM...")
    return render_template("weather_form.html")

@weather_routes.route("/weather/forecast", methods=["GET", "POST"])
def weather_forecast():
    print("GENERATING A WEATHER FORECAST...")

    if request.method == "POST":
        print("FORM DATA:", dict(request.form)) #> {'zip_code': '20057'}
        zip_code = request.form["zip_code"]
    elif request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        zip_code = request.args["zip_code"] #> {'zip_code': '20057'}

    results = get_hourly_forecasts(zip_code)
    print(results.keys())
    return render_template("weather_forecast.html", zip_code=zip_code, results=results)
```

After we get a weather forecast for the given zip code, we'll send the results to a new page called "weather_forecast", so let's create that page now in the templates directory, and place inside the following contents:

```html
{% extends "bootstrap_layout.html" %}

{% block content %}

    <h2>Weather Forecast for {{ results["city_name"].title() }}</h2>

    <p>Zip Code: {{ zip_code }}</p>

    <!-- TODO: consider using a table instead of a list -->
    <!-- https://www.w3schools.com/html/html_tables.asp -->
    <!-- https://getbootstrap.com/docs/4.0/content/tables/ -->
    <ul>
    {% for hourly in results["hourly_forecasts"] %}
        <li>{{ hourly["timestamp"] }} | {{ hourly["temp"] }} | {{ hourly["conditions"].upper() }}</li>
    {% endfor %}
    </ul>

{% endblock %}
```

Here, we are using the Jinja templating language to display any Python variables that are wrapped inside double curly braces (e.g. `{{ zip_code }}`). Fun, right?

Restart the server and visit "localhost:5000/weather/form" to test the newly-integrated weather forecasting functionality.

At this time, if you haven't told your app about these new routes, we'll get 404 errors, so let's finally configure the app to recognize the weather routes. In the "web_app/\_\_init\_\_.py" file, add the following lines:

```py
# web_app/__init__.py

# ...

from web_app.routes.weather_routes import weather_routes

# ...

# def create_app():
    # ...
    app.register_blueprint(weather_routes)
    # ...

# ...
```

Alright, now when you restart the server, you should be able to view the new pages as desired. Nice!

## Further Exploration (Optional)

You'll notice we can also view "localhost:5000/weather/forecast?zip_code=20057" directly, customizing the zip code via URL params as desired. You'll probably set up most of your routes to handle either GET requests or POST requests, but we configured the `weather_forecast` route to conditionally handle either, primarily as an example to show you how you could handle URL params.

Think of how this URL parameter approach relates to some other APIs that we've used earlier in the semester. Let's set up some example API routes now:

```py
# web_app/routes/api_routes.py

from flask import Blueprint, request, jsonify

api_routes = Blueprint("api_routes", __name__)

@api_routes.route("/api/hello.json")
def hello():
    return jsonify({"message": "Hello World"}) # can jsonify a dictionary

@api_routes.route("/api/users.json")
def users():
    return jsonify([1,2,3]) # can jsonify a list

@api_routes.route("/api/forecast.json")
def forecast():
    print("URL PARAMS:", dict(request.args))
    zip_code = request.args["zip_code"] #> {'zip_code': '20057'}
    results = get_hourly_forecasts(zip_code)
    return jsonify(results)
```

Register these new routes, restart your server, and view the API routes directly from the browser to see the JSON responses. Customize the zip code via URL params. You've created your own API. Nice!

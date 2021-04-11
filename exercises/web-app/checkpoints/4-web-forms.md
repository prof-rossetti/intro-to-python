# Checkpoint 4: Submitting Data from Web Forms

Let's create a web form with a text input element to allow the user to specify their given zip code. In the templates directory, add a new HTML file called "weather_form.html" and place inside the following contents:

```html
{% extends "layout.html" %}

{% block content %}

    <h2>Weather Form</h2>

    <p>Request an hourly forecast for your zip code...</p>

    <form action="/weather/forecast" method="POST">

        <label>Country Code:</label>
        <input type="text" name="country_code" placeholder="US" value="US">
        <br>

        <label>Zip Code:</label>
        <input type="text" name="zip_code" placeholder="20057" value="20057">
        <br>

        <button>Submit</button>
    </form>

{% endblock %}
```

Here we're saying when the user submits the form, we'll send their form inputs via POST request to a route called "/weather/forecast". So let's create some weather routes to handle the POST request. Create a new file in the "routes" directory called "weather_routes.py", and place inside the following contents:

```py
# web_app/routes/weather_routes.py

# web_app/routes/weather_routes.py

from flask import Blueprint, request, jsonify, render_template, flash, redirect

from app.weather_service import get_hourly_forecasts

weather_routes = Blueprint("weather_routes", __name__)

@weather_routes.route("/weather/form")
def weather_form():
    print("WEATHER FORM...")
    return render_template("weather_form.html")

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
        return jsonify({"message":"Invalid Geograpy. Please try again."})

@weather_routes.route("/weather/forecast", methods=["GET", "POST"])
def weather_forecast():
    print("WEATHER FORECAST...")

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    country_code = request_data.get("country_code") or "US"
    zip_code = request_data.get("zip_code") or "20057"

    results = get_hourly_forecasts(country_code=country_code, zip_code=zip_code)
    if results:
        flash(f"Weather Forecast Generated Successfully!", "success")
        return render_template("weather_forecast.html", country_code=country_code, zip_code=zip_code, results=results)
    else:
        flash(f"Geography Error. Please try again!", "danger")
        return redirect("/weather/form")

```

Also uncomment the corresponding lines in the init file to import and register these routes.

Based on this routing logic, after we get a weather forecast for the given zip code, we'll send the results to a new page called "weather_forecast.html", so let's create that page now in the "templates" directory, and place inside the following contents:

```html
{% extends "layout.html" %}

{% block content %}

    <h2>Weather Forecast for {{ results["city_name"] }}</h2>

    <p>Zip Code: {{ zip_code }}</p>

    <!-- TODO: consider using a table instead of a list -->
    <!-- TODO: consider adding images using the provided icon urls -->
    <ul>
    {% for hourly in results["hourly_forecasts"] %}
        <li>{{ hourly["timestamp"] }} | {{ hourly["temp"] }} | {{ hourly["conditions"].upper() }}</li>
    {% endfor %}
    </ul>

{% endblock %}
```

Here, we are using the Jinja template language to loop through our forecasts and display each.

Restart the server and visit the following routes to test the newly-integrated weather forecasting functionality:
  + http://localhost:5000/weather/forecast
  + http://localhost:5000/weather/forecast?country_code=US&zip_code=10012
  + http://localhost:5000/weather/forecast?country_code=US&zip_code=OOPS
  + http://localhost:5000/weather/forecast.json
  + http://localhost:5000/weather/forecast.json?country_code=US&zip_code=10012
  + http://localhost:5000/weather/forecast.json?country_code=US&zip_code=OOPS

Also visit http://localhost:5000/weather/form and submit the form to test the app's ability to handle POST requests.

Nice! We now have both a web interface and a JSON API interface into our app's weather functionality.

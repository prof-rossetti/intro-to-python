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

Here we're saying when the user submits the form, we'll send their form inputs via POST request to a route called "/weather/forecast". So let's update our weather routes accordingly:

```py
# web_app/routes/weather_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash

from app.weather_service import get_hourly_forecasts

weather_routes = Blueprint("weather_routes", __name__)

@weather_routes.route("/weather/form")
def weather_form():
    print("WEATHER FORM...")
    return render_template("weather_form.html")

@weather_routes.route("/weather/forecast", methods=["POST"])
def weather_forecast():
    print("WEATHER FORECAST...")

    request_data = dict(request.form)
    print("FORM DATA:", request_data)

    country_code = request_data.get("country_code") or "US"
    zip_code = request_data.get("zip_code") or "20057"

    results = get_hourly_forecasts(country_code=country_code, zip_code=zip_code)
    if results:
        #flash("Weather Forecast Generated Successfully!", "success")
        return render_template("weather_forecast.html",
            country_code=country_code,
            zip_code=zip_code,
            results=results
        )
    else:
        #flash("Geography Error. Please try again!", "danger")
        return redirect("/weather/form")

#
# API ROUTES
#

@weather_routes.route("/api/weather/forecast.json")
def weather_forecast_api():
    print("WEATHER FORECAST (API)...")

    url_params = dict(request.args)
    print("URL PARAMS:", url_params)

    country_code = url_params.get("country_code") or "US"
    zip_code = url_params.get("zip_code") or "20057"

    results = get_hourly_forecasts(country_code=country_code, zip_code=zip_code)
    if results:
        return jsonify(results)
    else:
        return jsonify({"message":"Invalid Geography. Please try again."}), 404

```

Based on this routing logic, after we get a weather forecast for the given zip code, we'll send the results to a new page called "weather_forecast.html", so let's create that page now in the "templates" directory, and place inside the following contents:

```html
{% extends "layout.html" %}

{% block content %}

    <h2>Weather Forecast for {{ results["city_name"] }}</h2>

    <p>Zip Code: {{ zip_code }}</p>

    <!-- TODO: consider using a table instead of a list -->
    <!-- TODO: consider adding images using the provided icon urls -->
    <ul>
    {% for forecast in results["hourly_forecasts"] %}
        <li>{{ forecast["timestamp"] }} | {{ forecast["temp"] }} | {{ forecast["conditions"].upper() }}</li>
    {% endfor %}
    </ul>

{% endblock %}
```

Here, we are using the Jinja template language to loop through our forecasts and display each.

Before visiting our app again in the browser, let's add a navigation link pointing to our weather form page. In the "web_app/templates/layout.html" file, add the following HTML code to the site navigation section, inside the `nav` element, below the other existing links:

```html
<li><a href="/weather/form">Weather Form</a></li>
```

Restart the server and visit http://localhost:5000/weather/form and submit the form to test the app's ability to handle POST requests.

Also know that we can request the forecast in JSON format, supplying URL params to our API route as desired:
  + http://localhost:5000/api/weather/forecast.json
  + http://localhost:5000/api/weather/forecast.json?country_code=US&zip_code=10012
  + http://localhost:5000/api/weather/forecast.json?country_code=US&zip_code=OOPS

Nice! We now have a web interface into our app's weather functionality.

Before moving on, make a commit with a message like "Handle Form Data".

# Checkpoint 5: Bootstrap Layout

Right now we have consistent navigation and footer, but our site could use some style upgrades. Let's leverage the capabilities of the [Twitter Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) front-end framework.

## Bootstrap Navbar

Let's create a new shared layout in the "templates" directory called "bootstrap_layout.html" and place inside contents from this [Bootstrap 5 HTML layout](/exercises/web-app/bootstrap_5_layout.html).

There's a lot going on in this file. But we still have the same "content" block which will allow the individual pages to specify their own content.

Instead of inheriting our templates from the "layout.html" file, let's modify them to inherit from the new bootstrap layout.


Updated "web_app/templates/home.html":

```html
{% extends "bootstrap_layout.html" %}
{% set active_page = "home" %}

{% block content %}

    <h1>Welcome Home</h1>

    <p>This is a paragraph on the "home" page.</p>

{% endblock %}
```

Updated "web_app/templates/about.html":

```html
{% extends "bootstrap_layout.html" %}
{% set active_page = "about" %}

{% block content %}

    <h1>About Me</h1>

    <p>This is a paragraph on the "about" page.</p>

{% endblock %}
```

Updated "web_app/templates/hello.html":

```html
{% extends "bootstrap_layout.html" %}
{% set active_page = "hello" %}

{% block content %}

    <h1>{{ message }}</h1>

    <p>This is a paragraph on the "hello" page.</p>

{% endblock %}
```

Updated "web_app/templates/weather_form.html":

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

Restart the server and view the app in the browser to see the new styles with a blue responsive navbar at the top!

Before moving on, make a commit with a message like "Bootstrap Layout".

## Flash Messaging

Reference:
  + [Flask Flash Messages](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/)
  + [Flask Secret Key Encryption](https://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key)
  + [Flask Sessions](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions)

Since Twitter Bootstrap provides [dismissible alert messages](https://getbootstrap.com/docs/5.0/components/alerts/), let's take advantage of Flask's `flash` messaging capabilities to display them.

Uncomment the lines related to "flash" in the weather routes file. Notice we're sending a flash with `flash("Weather Forecast Generated Successfully!", "success")`, where the first parameter is the flash message and the second represents the Bootstrap contextual color class (e.g. "success", "danger", "primary", etc.). Notice in the bootstrap layout how we are invoking `get_flashed_messages()` to display them at the top of the page.

Because Flask's flash messages use sessions, as a one-time setup, we'll need to update the web app's init file to configure the Flask app's secret key. This secret key facilitates the encryption of information stored in the session, and is more relevant when we have user data to protect.

```py
# web_app/__init__.py

import os
from dotenv import load_dotenv
from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes
from web_app.routes.weather_routes import weather_routes

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", default="super secret") # set this to something else on production!!!

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(weather_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
```


Restart the server and submit the weather form with valid and invalid inputs to see the flash message at the top of the forecast page!

Before moving on, make a commit with a message like "Flash Messaging".

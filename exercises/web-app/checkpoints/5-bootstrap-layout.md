# Web App Checkpoint 5 - Twitter Bootstrap Layout

Right now we have consistent navigation and footer, but our site could use some style upgrades. Let's leverage the capabilities of the [Twitter Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) front-end framework.

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

# Web App Checkpoint 4 - Shared Layouts

> FYI: [Reference Code](https://github.com/s2t2/daily-briefings-py/pull/1/commits/3449ff1040dbdc6acae3650779098b314bac6ae1)

Right now each template is a complete HTML file. If we wanted to implement common navigation and footer across each of the files, we'd have to copy and paste the same header and footer into all the files. This is not ideal from a maintainability perspective.

Luckily we have the ability to define the shared aspects of each page, like the header and footer, and inherit them from a common "layout".

Let's change our "home.html" and "about.html" to the following:

```html
{% extends "layout.html" %}

{% block content %}

    <h1>This is a heading</h1>

    <p>This is a paragraph text</p>

    <ul>
        <li>First list item</li>
        <li>Second list item</li>
        <li>Third list item</li>
    </ul>

{% endblock %}
```

```html
{% extends "layout.html" %}

{% block content %}

    <h1>About Me</h1>

    <p>todo write some stuff here</p>

{% endblock %}
```

You see we are referencing a shared template called "layout.html". Let's create that now.

Inside "web_app/templates/layout.html":

```html
<!doctype html>
<html>
  <head>
    <title>My Starter Web App | Learning how to use the Flask Python package</title>
  </head>

  <body>

    <!-- SITE NAVIGATION -->
    <div class="container">
      <div id="nav">
        <h1><a href="/">My Web App</a></h1>
        <ul>
            <li><a href="/about">About</a></li>
            <li><a href="/register">Sign Up</a></li>
        </ul>
      </div>
      <hr>

      <!-- PAGE CONTENTS -->
      <div id="content">
        {% block content %}
        {% endblock %}
      </div>

      <!-- FOOTER -->
      <div id="footer">
        <hr>
        &copy; Copyright 2020 [Your Name Here] |
        <a href="https://github.com/prof-rossetti/daily-briefings-py">source</a>
      </div>
    </div>

  </body>
</html>
```

The important part of this layout is the "content" block. It allows us to insert custom content into that section from each of our individual templates (i.e. "home.html" and "about.html").

Restart your server and view your app in the browser and use the links to navigate between pages. Witness the consistent header and footer. Nice!

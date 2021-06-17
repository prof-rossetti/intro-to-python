
# Checkpoint 3: Rendering HTML Pages

A web application is more fun with navigable HTML pages, so let's add take this opportunity to add some.

## Rendering HTML Templates

Reference:
  + [Jinja Templates](https://jinja.palletsprojects.com/en/2.11.x/)

Let's update the "home_routes.py" file, commenting out the existing `return` statements, and un-commenting the ` return render_template()` statements instead, referencing HTML template files like "home.html", "about.html", and "hello.html".

Flask will be looking for these HTML pages in a "templates" directory by default. So let's create a new subdirectory in the "web_app" folder called "templates", with new HTML files called "home.html", "about.html", and "hello.html", with the following contents inside, respectively.


Inside "web_app/templates/home.html":

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My App</title>
</head>
<body>

    <h1>Welcome Home</h1>

    <p>This is a paragraph on the "home" page.</p>

    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/hello">Hello</a></li>
        </ul>
    </nav>

    <footer>
        <p>My footer</p>
    </footer>

</body>
</html>

```

Inside "web_app/templates/about.html":


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My App</title>
</head>
<body>

    <h1>About Me</h1>

    <p>This is a paragraph on the "about" page.</p>

    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/hello">Hello</a></li>
        </ul>
    </nav>

    <footer>
        <p>My footer</p>
    </footer>

</body>
</html>

```

Inside "web_app/templates/hello.html":

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My App</title>
</head>
<body>

    <h1>{{ message }}</h1>

    <p>This is a paragraph on the "hello" page.</p>

    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/hello">Hello</a></li>
        </ul>
    </nav>

    <footer>
        <p>My footer</p>
    </footer>

</body>
</html>

```

Notice each HTML page has a unique heading, and a shared navigation and footer. We'll refactor the duplicate / shared HTML code later, but for right now it's fine.

Notice we're passing a variable called `message` from the router to the "hello" page, and using the "Jinja" template language to reference it (i.e. `{{ message }}`).

Restart the server and view the app in the browser and navigate between the three HTML pages. Use URL params to customize the name on the "hello" page. Cool!


Before moving on, make a commit with a message like "Render HTML pages".

## Shared Layouts

Right now each template is a complete HTML file. If we wanted to continue to implement common navigation and footer across each of the files, we'd have to copy and paste the same header and footer into all the files. This is not ideal from a maintainability perspective.

Luckily we have the ability to define the shared aspects of each page, like the header and footer, and inherit them from a common "layout".

Let's create a new file in the "templates" directory called "layout.html", and place inside the following contents:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>My Web App</title>
</head>
<body>

  <!-- SITE NAVIGATION -->
  <div class="container">
    <nav>
      <h1><a href="/">My Web App</a></h1>
      <ul>
          <li><a href="/about">About</a></li>
          <li><a href="/hello">Hello</a></li>
      </ul>
    </nav>
    <hr>

    <!-- PAGE CONTENTS -->
    <div id="content">
      {% block content %}
      {% endblock %}
    </div>

    <!-- FOOTER -->
    <footer>
      <hr>
      &copy; Copyright 2021 [Your Name Here] |
      <a href="https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/web-app/README.md">Source</a>
    </footer>
  </div>

</body>
</html>
```

> NOTE: feel free to update the footer to include your Name and a Source Code link to your own repo.


Notice the block called "content" (i.e. `{% block content %}`), which is a placeholder for the respective page contents.

Let's update the "home.html", "about.html", and "hello.html" templates to leverage this shared layout, using the following contents, respectively:

Inside "web_app/templates/home.html":

```html
{% extends "layout.html" %}

{% block content %}

    <h1>Welcome Home</h1>

    <p>This is a paragraph on the "home" page.</p>

{% endblock %}
```

Inside "web_app/templates/about.html":


```html
{% extends "layout.html" %}

{% block content %}

    <h1>About Me</h1>

    <p>This is a paragraph on the "about" page.</p>

{% endblock %}
```

Inside "web_app/templates/hello.html":


```html
{% extends "layout.html" %}

{% block content %}

    <h1>{{ message }}</h1>

    <p>This is a paragraph on the "hello" page.</p>

{% endblock %}
```


Notice each of these templates is inheriting from the "layout.html" template, and specifying some unique page contents to overwrite the "content" block.



Restart your server and view your app in the browser and use the HTML links to navigate between pages. Observe the consistent header and footer. Nice!

Before moving on, make a commit with a message like "Shared Layouts".

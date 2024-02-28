# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    return "Welcome Home"
    #return render_template("home.html")

@home_routes.route("/about")
def about():
    print("ABOUT...")
    return "About Me"
    #return render_template("about.html")

@home_routes.route("/hello")
def hello_world():
    print("HELLO...")

    # if the request contains url params, for example a request to "/hello?name=Harper"
    # the request object's args property will hold the values in a dictionary-like structure
    url_params = dict(request.args)
    print("URL PARAMS:", url_params) #> can be empty like {} or full of params like {"name":"Harper"}

    # get a specific key called "name" if available, otherwise use some specified default value
    # see also: https://www.w3schools.com/python/ref_dictionary_get.asp
    name = url_params.get("name") or "World"

    message = f"Hello, {name}!"
    return message
    #return render_template("hello.html", message=message)


# this is the "web_app/routes/unemployment_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.unemployment import fetch_unemployment_data, format_pct

unemployment_routes = Blueprint("unemployment_routes", __name__)


@unemployment_routes.route("/unemployment/dashboard")
def unemployment_dashboard():
    print("UNEMPLOYMENT DASHBOARD...")

    try:
        data = fetch_unemployment_data()
        latest = data[0]
        latest_rate_pct = format_pct(float(latest["value"]))
        latest_date = latest["date"]

        #flash("Fetched Latest Unemployment Data!", "success")
        return render_template("unemployment_dashboard.html",
            latest_rate_pct=latest_rate_pct,
            latest_date=latest_date,
            data=data
        )
    except Exception as err:
        print('OOPS', err)

        #flash("Unemployment Data Error. Please try again!", "danger")
        return redirect("/")

#
# API ROUTES
#

@unemployment_routes.route("/api/unemployment.json")
def unemployment_api():
    print("UNEMPLOYMENT DATA (API)...")

    try:
        data = fetch_unemployment_data()
        return data
    except Exception as err:
        print('OOPS', err)
        return {"message":"Unemployment Data Error. Please try again."}, 404

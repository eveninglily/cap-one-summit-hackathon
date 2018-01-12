#!/usr/bin/env python3

from flask import *
import data_processing

import secret


app = Flask(__name__, static_url_path="")
customer_id = "5a563d3b5eaa612c093b0ba2"


@app.route("/map")
def map():
    purchase_history = data_processing.get_sorted_filtered_purchases(customer_id)
    return render_template("map.html", mapsKey=secret.MAPS_KEY, purchase_history=purchase_history)

@app.route("/")
def index():
    return render_template("index.html", isLoginPage=True)

@app.route("/profile")
def profile():
    first_name = request.args.get("firstname")
    last_name = request.args.get("lastname")
    if not first_name or not last_name:
        return render_template("index.html", isLoginPage=True)
    return render_template("profile.html", firstname=first_name, lastname=last_name)

if __name__ == "__main__":
    import sys
    app.run(host="0.0.0.0", port=int(sys.argv[1]) if len(sys.argv) > 1 else 8080, threaded=True)

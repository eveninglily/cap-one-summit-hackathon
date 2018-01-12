#!/usr/bin/env python3

from flask import *
import data_processing
import secret
import suggest
import classify
from constants import PREFS


app = Flask(__name__, static_url_path="")
customer_id = "5a563d165eaa612c093b0ac4"


@app.template_filter()
def format_money(m):
    if m is None:
        return "Error"
    return "${:,.2f}".format(m)

@app.route("/map")
def map():
    print("hello?")
    purchase_history = data_processing.get_sorted_filtered_purchases(customer_id)
    print(purchase_history)
    return render_template("map.html", mapsKey=secret.MAPS_KEY, purchase_history=purchase_history)

@app.route("/")
def index():
    return render_template("index.html", isLoginPage=True)

@app.route("/profile")
def profile():
    first_name = request.args.get("firstname")
    last_name = request.args.get("lastname")
    if not first_name or not last_name:
        return render_template("profile.html", firstname="", lastname="")
    return render_template("profile.html", firstname=first_name, lastname=last_name)

@app.route("/alexa")
def alexa():
    habit, score = data_processing.get_alexa_data(customer_id)
    category = ""
    if habit == "shopping":
        category = "clothing_store"
    elif habit == "food":
        category = "meal_takeaway"
    else:
        category = "bar"

    s = suggest.suggest_alternative(38.878337, -77.100703, category, PREFS)

    return jsonify({'place': s[0], 'score': score, 'habit': habit})

@app.route("/suggest")
def suggest_api():
    category = request.args.get('category')
    lng = request.args.get('pos[lng]')
    lat = request.args.get('pos[lat]')
    return jsonify(suggest.suggest_alternative(lat, lng, category, PREFS))

@app.route('/totals')
def get_totals():
    return jsonify(classify.parse_data(data_processing.strip_data(customer_id)))

@app.route('/transactions')
def get_transactions():
    return jsonify(data_processing.get_sorted_filtered_purchases(customer_id))

if __name__ == "__main__":
    import sys
    app.run(host="0.0.0.0", port=int(sys.argv[1]) if len(sys.argv) > 1 else 8080, threaded=True)

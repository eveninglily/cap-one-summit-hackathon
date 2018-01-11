#!/usr/bin/env python3

from flask import *


app = Flask(__name__, static_url_path="")


@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/login")
def login():
    return render_template("login.html", isIndex=True)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    import sys
    app.run(host="0.0.0.0", port=int(sys.argv[1]) if len(sys.argv) > 1 else 8080, threaded=True)

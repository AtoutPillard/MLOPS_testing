
"""
ANIME RATING PREDICTION API
"""

# Importation
import os
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask.json import jsonify

import pandas as pd

import controller as ctrl

from prometheus_flask_exporter import PrometheusMetrics

# Code
app = Flask(__name__)

metrics = PrometheusMetrics(app)

request_counter = metrics.counter(
    'anime_req_counter', 'Request count by endpoints',
    labels={'endpoint': lambda: request.endpoint, 'path': lambda: request.path, 'method':lambda:request.method}
)

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/", methods=["POST"])
@request_counter
def predict():
    """
    Return the anime rating prediction based on its information input
    """

    if request.form.get('key') is None and not request.is_json:
            return jsonify({'error': 'Missing or invalid data in request'}), 500
    rate = ctrl.predict_rating(request)

    return jsonify({"rating": rate})

@app.route("/metrics")
def metrics():
    return metrics.generate_latest()

if __name__ == '__main__':
    app.run()
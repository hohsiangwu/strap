import logging

from flask import jsonify

from {{ app_name }} import app

logger = logging.getLogger(__name__)


@app.route('/')
def index():
    return jsonify(tagline='you know, for {{ app_name }}',
                   status_code=200)

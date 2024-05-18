#!/usr/bin/python3
"""
Flask app that runs on 0.0.0.0
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    home hbnb!
    """
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

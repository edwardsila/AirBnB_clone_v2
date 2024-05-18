#!/usr/bin/python3
"""
displays hbnb ..location
"""
from flask import Flask

app = flask(__name__)

@app.route('/', strict_slashes=False)
def home():
   """
   displays hbnb
   """
   return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    returns hbnb
    """
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

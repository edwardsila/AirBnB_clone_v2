#!/usr/bin/python3
"""
displays hbnb ..location
"""
from flask import Flask

app = Flask(__name__)


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


@app.route('/c/<text>')
def c_with_params(text):
    """ Return c text """
    text_no_underscore = text.replace('_', ' ')
    return "c {}".format(text_no_underscore)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask

"""
Flask app that runs on 0.0.0.0
"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns Helloe HBNB """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

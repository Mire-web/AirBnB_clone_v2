#!/usr/bin/python3
"""
Run Flask App on 5000 from 0.0.0.0
Author: Mire-web
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    return f"C {text.replace('_', ' ')}"


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythontext(text):
    if text:
        return f"Python {text.replace('_', ' ')}"
    else:
        return f"Python {text}"


@app.route(f'/number/<int:n>', strict_slashes=False)
def displayNumber(n):
    if int(n):
        return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
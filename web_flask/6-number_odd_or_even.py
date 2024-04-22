#!/usr/bin/python3
"""
Run Flask App on 5000 from 0.0.0.0
Author: Mire-web
"""
from flask import Flask, render_template


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


@app.route('/number/<int:n>', strict_slashes=False)
def displayNumber(n):
    if int(n):
        return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def numberHtml(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odoreven(n):
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, isEven=True)
    else:
        return render_template('6-number_odd_or_even.html', n=n, isEven=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)

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


@app.route(f'/c/<text>')
def ctext(text):
    return f"C {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)

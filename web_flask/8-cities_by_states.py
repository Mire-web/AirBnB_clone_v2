#!/usr/bin/python3
"""
Run Flask App on 5000 from 0.0.0.0
AirBnB Clone Project
Author: Mire-web
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/states_list', strict_slashes=False)
def list_state():
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def list_cities_by_state():
    cities = storage.all("City")
    states = storage.all("State")
    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)


@app.teardown_appcontext
def clean_up(error=None):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)

#!/usr/bin/python3
"""Starts a Flask web application for AirBnB clone"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()
# the city and state route
@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays a HTML page with states and cities"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    # to run the flask app with all hosts and in specific port
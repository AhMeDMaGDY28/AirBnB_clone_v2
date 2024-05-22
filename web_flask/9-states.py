#!/usr/bin/python3
"""Starts a Flask web application for AirBnB clone"""
from flask import Flask, render_template
from models import storage

# Create a new Flask web application
app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """reload storage after each request"""
    storage.close()


# the states route
@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """list states of each state sorted by name"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    # to run the flask app with all hosts and in specific port

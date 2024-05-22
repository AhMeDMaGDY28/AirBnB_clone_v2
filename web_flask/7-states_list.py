#!/usr/bin/python3
"""a simple flask app"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


# the home route
@app.route('/')
def home_route():
    return "HBNB is good"


# the states route
@app.route('/states_list', strict_slashes=False)
def states_to_html_route():
    """open the data to view it in html"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template("8-cities_by_states.html", states=sorted_states)


@app.teardown_appcontext
def close_storage(exception):
    """Closes the storage session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    # to run the flask app with all hosts and in specific port

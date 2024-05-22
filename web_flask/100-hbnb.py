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


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """list states of each state sorted by name"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template(
        '100-hbnb.html', states=states, amenities=amenities, places=places)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    # to run the flask app with all hosts and in specific port

#!/usr/bin/python3
"""a simple flask application"""

from flask import Flask

# make new flask app
app = Flask(__name__)


# the home route
@app.route('/', strict_slashes=False)
def home_route():
    """Display 'Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    # to run the flask app with all hosts and in specific port

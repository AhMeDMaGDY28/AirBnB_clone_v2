#!/usr/bin/python3
"""a simple flask application"""

from flask import Flask

# make new flask app
app = Flask(__name__)


# the home route
@app.route('/', strict_slashes=False)
def home_route():
    """Display 'Hello HBNB!"""
    return "Hello HBNB"


# the HBNB route
@app.route('/hbnb', strict_slashes=False)
def HBNB_route():
    """Display 'HBNB!"""
    return "HBNB"


# the C dynamic route
@app.route('/c/<text>', strict_slashes=False)
def C_route(text):
    """C dynamic route"""
    mod_text = text.replace("_", " ")
    return f"C {mod_text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    # to run the flask app with all hosts and in specific port

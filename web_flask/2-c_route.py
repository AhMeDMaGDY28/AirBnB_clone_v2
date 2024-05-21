#!/usr/bin/python3
"""a simple flask application"""

from flask import Flask

# make new flask app
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def master():
    """Display 'Hello HBNB!"""
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """Display 'HBNB!"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """a dynamic route"""
    mod_text = text.replace("_", " ")
    return f"c {mod_text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    # to run the flask app with all hosts and in specific port

#!/usr/bin/python3
"""a simple flask application"""

# make new flask app
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def main_menu():
    """Display 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # to run the flask app with all hosts and in specific port

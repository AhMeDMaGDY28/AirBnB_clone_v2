#!/usr/bin/python3
"""a simple flask application"""

from flask import Flask, render_template

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


# the python dynamic route
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is_cool"):
    """python dynamic route"""
    mod_text = text.replace("_", " ")
    return f"Python {mod_text}"



# the number dynamic route
@app.route('/number/<int:n>', strict_slashes=False)
def int_route(n):
    """integer dynamic route"""
    return f"{n} is a number"



# the number dynamic route
@app.route('/number_template/<int:n>', strict_slashes=False)
def int_route2(n):
    """integer dynamic route"""
    return render_template("5-number.html", n=n)



# the odd/even dynamic route
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """ odd/even dynamic route"""
    o = "odd"
    if n % 2 == 0:
        o = "even" 
    return render_template("6-number_odd_or_even.html", n=n, o=o)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    # to run the flask app with all hosts and in specific port

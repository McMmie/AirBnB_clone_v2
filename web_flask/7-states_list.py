#!/usr/bin/python3
"""starts a flask web application
"""
from flask import Flask
from flask import abort
from flask import render_template
from markupsafe import escape
from models import storage
#from models import storage.all()


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """the function that displays on message on the browser
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """the function that displays on message on the browser
    """
    return "HBNB!"

@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """the function that displays on message on the browser
    """
    temp = ""
    for item in text:
        if item == "_":
            item = " "

        temp = temp + item
    return f'C {escape(temp)}'

@app.route("/python", strict_slashes=False)
def default_python():
    """the function that displays on message on the browser
    """

    return f'Python is cool'

@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """the function that displays on message on the browser
    """
    temp = ""
    for item in text:
        if item == "_":
            item = " "

        temp = temp + item
    return f'python {escape(temp)}'

@app.route("/number", strict_slashes=False)
def num():
    """display “n is a number” only if n is an integer"""
    return ""

@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    if n.isdigit():
        return f'{escape(n)} is a number'
    else:
        abort(404)

@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    """display “n is a number” only if n is an integer"""
    if n.isdigit():
        n = int(n)
        return render_template('5-number.html', n=int(n))
    else:
        abort(404)

@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def odd_or_even(n):
    """display “n is a number” only if n is an integer"""
    if n.isdigit():
        return render_template('6-number_odd_or_even.html', n=int(n))
    else:
        abort(404)

@app.teardown_appcontext
def teardown(self):
    """a method to handle @app.teardown_appcontext"""
    storage.close()

@app.route("/states_list", strict_slashes=False)
def states_list():
    """displays a html page with a list of all state objects present
    in DBStorage sorted by name
    """
    state_objs = [s for s in storage.all("State").values()]
    return render_template('7-states_list.html',
                                       state_objs=state_objs)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

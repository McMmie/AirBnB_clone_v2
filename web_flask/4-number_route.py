#!/usr/bin/python3
"""starts a flask web application
"""
from flask import Flask
from flask import abort
from flask import render_template
from markupsafe import escape


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
def number(n):
    """display “n is a number” only if n is an integer"""
    if n.isdigit():
        return render_template('5-number.html')
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

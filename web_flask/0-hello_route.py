#!/usr/bin/python3
"""starts a flask web application
"""
from flask import Flask


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """the function that displays on message on the browser
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

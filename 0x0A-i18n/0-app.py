#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """ GET route /
    Return:
      - a welcome message
    """
    return "Hello World!"


if __name__ == '__main__':
    app.run()

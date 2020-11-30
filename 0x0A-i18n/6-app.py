#!/usr/bin/env python3
"""
Get locale from request
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ class config for app Flask """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/')
def config():
    """ config for your Flask app """
    return render_template("6-index.html")


def get_user() -> Dict:
    """ function that returns a user dictionary """
    try:
        return users.get(int(request.args.get('login_as')))
    except Exception:
        return None


@app.before_request
def before_request():
    """ before request """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ Get locale from request """
    if request.args.get("locale"):
        return request.args.get("locale")
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

#!/usr/bin/env python3
"""
Get locale from request
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import flask_babel
from typing import Dict
from pytz import timezone
import pytz.exceptions
from datetime import datetime
from babel.dates import format_date, format_datetime, format_time
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
    return render_template("index.html")


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

    date_time_zone_now = flask_babel.to_user_timezone(datetime.now())
    g.date = format_datetime(date_time_zone_now,
                             locale=str(flask_babel.get_locale()))

@babel.localeselector
def get_locale():
    """ Get locale from request """
    if request.args.get("locale"):
        return request.args.get("locale")
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ Infer appropriate time zone """
    try:
        if get_user():
            timez = get_user()["timezone"]
        if request.args.get("timezone"):
            timez = request.args.get("timezone")
    except Exception:
        return None
    else:
        return pytz.timezone(timez).zone


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

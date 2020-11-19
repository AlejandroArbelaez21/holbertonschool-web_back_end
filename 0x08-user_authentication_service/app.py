#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    """ GET route /
    Return:
      - a welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """ the end-point should register it and respond with a JSON payload """
    email = request.form['email']
    password = request.form['password']
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": "{}".format(user.email),
                        "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """ login """
    email = request.form['email']
    password = request.form['password']
    if not AUTH.valid_login(email, password):
        abort(401)
    else:
        resp = jsonify({"email": "{}".format(email), "message": "logged in"})
        resp.set_cookie('session_id', AUTH.create_session(email))
        return resp


@app.route('/sessions', methods=['DELETE'])
def logout():
    """ logout """
    session_id = request.cookies.get('session_id')
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            AUTH.destroy_session(user.id)
            return redirect("http://0.0.0.0:5000/")
    abort(403)


@app.route('/profile', methods=['GET'])
def profile() -> str:
    """ The request is expected to contain a session_id cookie """
    session_id = request.cookies.get('session_id')
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            return jsonify({"email": "{}".format(user.email)})
    abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token() -> str:
    """ generate a token and respond with a 200 HTTP status """
    email = request.form['email']
    if not AUTH.create_session(email):
        abort(403)
    else:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": "{}".format(email),
                        "reset_token": "{}".format(token)})


@app.route('/reset_password', methods=['PUT'])
def update_password() -> str:
    """ Update the password. If the token is invalid """
    email = request.form['email']
    reset_token = request.form['reset_token']
    new_password = request.form['new_password']
    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)
    else:
        return jsonify({"email": "{}".format(email),
                        "message": "Password updated"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

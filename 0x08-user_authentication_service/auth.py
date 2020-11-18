#!/usr/bin/env python3
"""
Hash password
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """ returned string is a salted hash of the input password """
    password = bytes(password, 'utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Constructor """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ return the User object. """
        try:
            self._db.find_user_by(email=email)
        except ValueError:
            new_user = self._db.add_user(email, _hash_password(password))
            return new_user
        else:
            raise ValueError("User {} already exists".format(email))

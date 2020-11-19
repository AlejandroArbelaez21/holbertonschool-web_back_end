#!/usr/bin/env python3
"""
Hash password
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
from uuid import uuid4
from typing import Union


def _hash_password(password: str) -> str:
    """ returned string is a salted hash of the input password """
    password = bytes(password, 'utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())


def _generate_uuid() -> str:
    """ return a string representation of a new UUID """
    return str(uuid4())


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
        except NoResultFound:
            new_user = self._db.add_user(email, _hash_password(password))
            return new_user
        else:
            raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """ locating a user by email, check the pswrd if match return True """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(bytes(password, 'utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ The method find user by email, generate a UUID and save in db """
        try:
            user = self._db.find_user_by(email=email)
            uid = _generate_uuid()
            self._db.update_user(user.id, session_id=uid)
            return uid
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """ return the corresponding user """
        if session_id is None:
            return None
        try:
            data = self._db.find_user_by(session_id=session_id)
            return data
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ The method updates the corresponding user’s session ID to None """
        self._db.update_user(user_id, session_id=None)
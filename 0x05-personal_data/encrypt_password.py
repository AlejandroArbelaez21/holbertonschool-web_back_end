#!/usr/bin/env python3

"""
5. Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    returns a salted, hashed password, which is a byte string.
    """
    password = bytes(password, 'utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    function that expects 2 arguments and returns a boolean.
    """
    return bcrypt.checkpw(bytes(password, 'utf-8'), hashed_password)

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

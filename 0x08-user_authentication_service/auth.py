#!/usr/bin/env python3
"""
Hash password
"""
import bcrypt


def _hash_password(password: str) -> str:
    """ returned string is a salted hash of the input password """
    password = bytes(password, 'utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())

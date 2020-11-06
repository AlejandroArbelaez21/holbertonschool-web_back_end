#!/usr/bin/env python3

"""
3. Auth class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class for authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ will be used later """
        return False

    def authorization_header(self, request=None) -> str:
        """ Flask request object """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Flask request object """
        return None

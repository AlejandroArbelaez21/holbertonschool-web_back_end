#!/usr/bin/env python3

"""
3. Auth class
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ Class for authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ check paths in excluded_paths """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        for excluded in excluded_paths:
            if excluded[-1] == '*':
                if path[0] == excluded[:1]:
                    return False
        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """ Flask request object """
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """ Flask request object """
        return None

    def session_cookie(self, request=None):
        """ returns a cookie value from a request
        """
        if request is None:
            return None
        return request.cookies.get(getenv('SESSION_NAME'))

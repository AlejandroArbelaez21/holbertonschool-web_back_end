#!/usr/bin/env python3

"""
3. Auth class
"""
from flask import request
from typing import List, TypeVar


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
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Flask request object """
        return None

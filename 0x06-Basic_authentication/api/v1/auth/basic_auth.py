#!/usr/bin/env python3

"""
6. Basic auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ class BasicAuth that inherits from Auth """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ returns the Base64 part of the Authorization header """
        if authorization_header is None:
            return None
        if isinstance(authorization_header, str):
            if authorization_header.startswith("Basic "):
                return authorization_header[6:]
            else:
                return None
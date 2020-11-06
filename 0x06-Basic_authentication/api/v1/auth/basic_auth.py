#!/usr/bin/env python3

"""
6. Basic auth
"""
from api.v1.auth.auth import Auth
import base64
import binascii
from typing import TypeVar
from models.user import User


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ returns the decoded value of a Base64 string """
        if base64_authorization_header is None:
            return None
        if isinstance(base64_authorization_header, str):
            try:
                base64_authorization_header = base64.b64decode(
                                            base64_authorization_header
                                          )
                return base64_authorization_header.decode('utf-8')
            except Exception:
                return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ returns the user email and password from Base64 decoded value """
        if decoded_base64_authorization_header is None:
            return None, None
        if isinstance(decoded_base64_authorization_header, str):
            if ":" in decoded_base64_authorization_header:
                validate = decoded_base64_authorization_header.split(":", 1)
                return validate[0], validate[1]
            else:
                return None, None
        else:
            return None, None

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """ returns the User instance based on his email and password """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        users = User.search({'email': user_email})
        if not users:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

        def current_user(self, request=None) -> TypeVar('User'):
            """ retrieves the User instance for a request, otherwise None """
        authorization_header = self.authorization_header(request=request)
        extract_base64_authorization_header = (
            self.extract_base64_authorization_header(authorization_header)
        )
        decode_base64_authorization_header = (
            self.decode_base64_authorization_header(
                extract_base64_authorization_header
            )
        )
        extract_user_credentials = self.extract_user_credentials(
            decode_base64_authorization_header
        )
        user_object_from_credentials = self.user_object_from_credentials(
            user_email=extract_user_credentials[0],
            user_pwd=extract_user_credentials[1]
        )
        return user_object_from_credentials

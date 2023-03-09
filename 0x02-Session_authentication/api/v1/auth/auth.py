#!/usr/bin/env python3
"""
Authentication module for API.
"""
import re
from typing import List, TypeVar
from flask import request


class Auth:
    """
    Authentication class.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if a path requires authentication.
        :param path: path to be checked.
        :param excluded_paths: list of paths excluded.
        :return:
            - True if path is None
            - True if excluded_paths is None or empty.
            - False if path is in excluded_paths
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ""
                if exclusion_path[-1] == "*":
                    pattern = "{}.*".format(exclusion_path[0:-1])
                elif exclusion_path[-1] == "/":
                    pattern = "{}/*".format(exclusion_path[0:-1])
                else:
                    pattern = "{}/*".format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Gets the authorization header field from the request.
        :return:
            - If request is None, returns None
            - If request doesn’t contain the header key Authorization, returns None
            - value of the header request Authorization
        """
        if request is not None:
            return request.headers.get("Authorization", None)
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Gets the current user from the request.
        :return: None
        """
        return None

"""
PyPatchwork - Python Library for Patchwork REST API

Copyright (C) 2023  Tedd Ho-Jeong An <hj.tedd.an@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/
"""
import json
import requests

from urllib.parse import urlparse, urlencode

from . import PatchworkException


class Connection:
    """
    Connection class
    """

    def __init__(
        self,
        base_url,
        token,
    ):
        """
        :param base_url: Base url to connect
        :type base_url: string
        :param token: Authentication token
        :type token: string
        :param per_page: Number of item per page
        :type per_page: integer
        """

        self.__base_url = base_url
        u = urlparse(base_url)
        self.__scheme = u.scheme
        self.__hostname = u.hostname
        self.__path = u.path

        if u.port:
            self.__port = u.port
        else:
            if self.__scheme == "https":
                self.__port = 443
            else:
                self.__port = 80

        self.__token = token

    def __update_auth_token(self, headers):
        if self.__token is not None:
            headers["Authorization"] = f"Token {self.__token}"

    def __make_abs_url(self, url):
        if url.startswith("http"):
            return url
        # Relative path
        return f"{self.__scheme}://{self.__hostname}{self.__path}{url}"

    def __update_url_with_params(self, url, params):
        if len(params) == 0:
            return url
        return f"{url}?{urlencode(params)}"

    def __raise_exception(self, status, headers, output):
        # 400
        if status == 400:
            cls = PatchworkException.BadRequestException
        elif status == 403:
            cls = PatchworkException.ForbiddenException
        elif status == 404:
            cls = PatchworkException.NotFoundException
        elif status == 409:
            cls = PatchworkException.ConflictException
        else:
            cls = PatchworkException.PatchworkException
        return cls(status, headers, output)

    def __request(self, method, url, parameters, headers, input):
        assert method in ["GET", "POST", "PATCH", "PUT"]
        if parameters is None:
            parameters = dict()
        if headers is None:
            headers = dict()

        # Update Authorization token to headers
        self.__update_auth_token(headers)

        # Update URL to full format
        abs_url = self.__make_abs_url(url)
        abs_url = self.__update_url_with_params(abs_url, parameters)

        print(f"ABS_URL={abs_url}")

        enc_input = None
        if input is not None:
            headers["Content-Type"] = "application/json"
            enc_input = json.dumps(input)

        resp = requests.request(method, abs_url, headers=headers, data=enc_input)
        resp_status = resp.status_code
        resp_headers = resp.headers
        if len(resp.text) == 0:
            resp_data = None
        else:
            resp_data = json.loads(resp.text)

        print(f"resp status: {resp_status}")

        # Check resp status and raise the exception
        if resp_status >= 400:
            raise self.__raise_exception(resp_status, resp_headers, resp_data)
        return resp_headers, resp_data

    def request(self, method, url, parameters=None, headers=None, input=None):
        """Send request to URL and returns header and output data in json format

        :param method: Method of the new Request object. i.e. 'GET', 'PUT'
        :type method: string
        :param url: URL for the new Request object. i.e. 'patches'/{id}'
        :type url: string
        :param parameters: Parameters for URL request, defaults to None
        :type parameters: dict, optional
        :param headers: Extra headers for URL request, defaults to None
        :type headers: dict, optional
        :param input: Input data for URL request, defaults to None
        :type input: dict, optional
        """
        return self.__request(method, url, parameters, headers, input)

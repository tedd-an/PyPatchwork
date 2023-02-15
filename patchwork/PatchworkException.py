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


class PatchworkException(Exception):
    """
    Exception class for Patchwork
    """

    def __init__(self, status, headers, data):
        super().__init__()
        self.__status = status
        self.__headers = headers
        self.__data = data
        self.__detail = self.__get_detail()

    def __get_detail(self):
        if "Content-Type" in self.__headers:
            if self.__headers["Content-Type"] == "application/json":
                if "detail" in self.__data:
                    return self.__data["detail"]
                # In case of 400, it shows the list of invalid parameters
                return self.__data
        return "Generic Exception"

    @property
    def status(self):
        """
        HTTP status
        """
        return self.__status

    @property
    def detail(self):
        """
        Exception detail provided by the Patchwork server, if available
        """
        return self.__detail

    def __str__(self):
        return f"{self.__status} {self.__detail}"


class BadRequestException(PatchworkException):
    """
    400 Bad Request - Invalid Request
    """


class ForbiddenException(PatchworkException):
    """
    403 Forbidden - Fobidden
    """


class NotFoundException(PatchworkException):
    """
    404 Not Found - Not Found
    """


class ConflictException(PatchworkException):
    """
    409 Conflict - Conflict
    """

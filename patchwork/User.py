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
import patchwork.UserSettings


class User:
    """
    Class for User object
    """

    def __init__(self, connection, attributes):
        self._connection = connection
        self._id = None
        self._url = None
        self._username = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._settings = None
        # Update attributes
        self._update_attributes(attributes)

    def _update_attributes(self, attributes):
        if attributes is None:
            return
        if "id" in attributes:
            self._id = attributes["id"]
        if "url" in attributes:
            self._url = attributes["url"]
        if "username" in attributes:
            self._username = attributes["username"]
        if "first_name" in attributes:
            self._first_name = attributes["first_name"]
        if "last_name" in attributes:
            self._last_name = attributes["last_name"]
        if "email" in attributes:
            self._email = attributes["email"]
        if "settings" in attributes:
            self._settings = attributes["settings"]

    def __repr__(self):
        return f"User(id:{self._id} username:{self._username})"

    @property
    def id(self):
        """
        :type: integer
        """
        return self._id

    @property
    def url(self):
        """
        :type: string
        """
        return self._url

    @property
    def username(self):
        """
        :type: string
        """
        return self._username

    @property
    def first_name(self):
        """
        :type: string
        """
        return self._first_name

    @property
    def last_name(self):
        """
        :type: string
        """
        return self._last_name

    @property
    def email(self):
        """
        :type: string
        """
        return self._email

    @property
    def settings(self):
        """
        :type: :class:`patchwork.UserSettings.UserSettings`
        """
        return patchwork.UserSettings.UserSettings(self._connection, self._settings)

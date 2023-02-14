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
import patchwork.User


class People:
    """
    Class for People object
    """

    def __init__(self, connection, attributes):
        self._connection = connection
        self._id = None
        self._url = None
        self._name = None
        self._email = None
        self._user = None
        # Update attributes
        self._update_attributes(attributes)

    def _update_attributes(self, attributes):
        if "id" in attributes:
            self._id = attributes["id"]
        if "url" in attributes:
            self._url = attributes["url"]
        if "name" in attributes:
            self._name = attributes["name"]
        if "email" in attributes:
            self._email = attributes["email"]
        if "user" in attributes:
            self._user = attributes["user"]

    def __repr__(self):
        return f"People(id:{self._id} name:{self._name} email:{self._email})"

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
    def name(self):
        """
        :type: string
        """
        return self._name

    @property
    def email(self):
        """
        :type: string
        """
        return self._email

    def get_user_info(self):
        """
        User info if exist

        :rtype: :class:`patchwork.User.User`
        """
        if self._user is None:
            return None
        return patchwork.User.User(self._connection, self._user)

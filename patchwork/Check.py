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
import datetime
from .User import User


class Check:
    """
    Class for Chceck object
    """

    def __init__(self, connection, attributes):
        self._connection = connection
        self._id = None
        self._url = None
        self._user = None
        self._date = None
        self._state = None
        self._target_url = None
        self._context = None
        self._description = None
        self.__update_attributes(attributes)

    def __update_attributes(self, attributes):
        if "id" in attributes:
            self._id = attributes["id"]
        if "url" in attributes:
            self._url = attributes["url"]
        if "user" in attributes:
            self._user = attributes["user"]
        if "date" in attributes:
            self._date = datetime.datetime.strptime(
                attributes["date"], "%Y-%m-%dT%H:%M:%S.%f"
            )
        if "state" in attributes:
            self._state = attributes["state"]
        if "target_url" in attributes:
            self._target_url = attributes["target_url"]
        if "context" in attributes:
            self._context = attributes["context"]
        if "description" in attributes:
            self._description = attributes["description"]

    def __repr__(self):
        return f"Check(id:{self._id} state:{self._state} context:{self._context})"

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
    def date(self):
        """
        :type: datetime.datetime
        """
        return self._date

    @property
    def state(self):
        """
        :type: string
        """
        return self._state

    @property
    def target_url(self):
        """
        :type: string
        """
        return self._target_url

    @property
    def context(self):
        """
        :type: string
        """
        return self._context

    @property
    def description(self):
        """
        :type: dict
        """
        return self._description

    def get_user(self):
        """
        User detail (partial)

        :rtype: :class:`patchwork.User.User`
        """
        return User(self._connection, self._user)

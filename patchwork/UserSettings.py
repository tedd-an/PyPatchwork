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


class UserSettings:
    """
    Class for User setting object
    """

    def __init__(self, connection, attributes):
        self._connection = connection
        self._send_email = None
        self._items_per_page = None
        self._show_ids = None
        # Update attributes
        self._update_attributes(attributes)

    def _update_attributes(self, attributes):
        if "send_email" in attributes:
            self._send_email = attributes["send_email"]
        if "items_per_page" in attributes:
            self._items_per_page = attributes["items_per_page"]
        if "show_ids" in attributes:
            self._show_ids = attributes["show_ids"]

    def __repr__(self):
        output = ""
        if self._send_email is not None:
            output += f"{self._send_email}"
        if self._items_per_page is not None:
            output += f"{self._items_per_page}"
        if self._show_ids is not None:
            output += f"{self._show_ids}"
        return output

    @property
    def send_email(self):
        """
        :type: boolean
        """
        return self._send_email

    @property
    def items_per_page(self):
        """
        :type: integer
        """
        return self._items_per_page

    @property
    def show_ids(self):
        """
        :type: boolean
        """
        return self._show_ids

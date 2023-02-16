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
import patchwork.People


class Comment:
    """
    Class for Comment object
    """

    def __init__(self, connection, attributes):
        self._connection = connection
        self._id = None
        self._web_url = None
        self._msgid = None
        self._list_archive_url = None
        self._date = None
        self._subject = None
        self._submitter = None
        self._headers = None
        self._content = None
        self.__update_attributes(attributes)

    def __update_attributes(self, attributes):
        if "id" in attributes:
            self._id = attributes["id"]
        if "web_url" in attributes:
            self._web_url = attributes["web_url"]
        if "msgid" in attributes:
            self._msgid = attributes["msgid"]
        if "list_archive_url" in attributes:
            self._list_archive_url = attributes["list_archive_url"]
        if "date" in attributes:
            self._date = datetime.datetime.strptime(
                attributes["date"], "%Y-%m-%dT%H:%M:%S"
            )
        if "subject" in attributes:
            self._subject = attributes["subject"]
        if "submitter" in attributes:
            self._submitter = attributes["submitter"]
        if "headers" in attributes:
            self._headers = attributes["headers"]
        if "content" in attributes:
            self._content = attributes["content"]

    def __repr__(self):
        return f"Comment(id:{self._id} subject:{self._subject})"

    @property
    def id(self):
        """
        :type: integer
        """
        return self._id

    @property
    def web_url(self):
        """
        :type: string
        """
        return self._web_url

    @property
    def msgid(self):
        """
        :type: string
        """
        return self._msgid

    @property
    def list_archive_url(self):
        """
        :type: string
        """
        return self._list_archive_url

    @property
    def date(self):
        """
        :type: datetime.datetime
        """
        return self._date

    @property
    def subject(self):
        """
        :type: string
        """
        return self._subject

    @property
    def headers(self):
        """
        :type: dict
        """
        return self._headers

    @property
    def content(self):
        """
        :type: string
        """
        return self._content

    def get_submitter(self):
        """
        Submitter detail (partial)

        :rtype: :class:`patchwork.People.People`
        """
        return patchwork.People.People(self._connection, self._submitter)

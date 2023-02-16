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
import patchwork.Comment
import patchwork.Connection
import patchwork.People
import patchwork.Project
import patchwork.Series


class Cover:
    """
    Class for Cover Letter object
    """

    def __init__(self, connection, attributes):
        self._connection = connection
        self._id = None
        self._url = None
        self._web_url = None
        self._project = None
        self._msgid = None
        self._list_archive_url = None
        self._date = None
        self._name = None
        self._submitter = None
        self._mbox = None
        self._series = None
        self._comments = None
        self._headers = None
        self._content = None
        self.__update_attributes(attributes)

    def __update_attributes(self, attributes):
        if "id" in attributes:
            self._id = attributes["id"]
        if "url" in attributes:
            self._url = attributes["url"]
        if "web_url" in attributes:
            self._web_url = attributes["web_url"]
        if "project" in attributes:
            self._project = attributes["project"]
        if "msgid" in attributes:
            self._msgid = attributes["msgid"]
        if "list_archive_url" in attributes:
            self._list_archive_url = attributes["list_archive_url"]
        if "date" in attributes:
            self._date = datetime.datetime.strptime(
                attributes["date"], "%Y-%m-%dT%H:%M:%S"
            )
        if "name" in attributes:
            self._name = attributes["name"]
        if "submitter" in attributes:
            self._submitter = attributes["submitter"]
        if "mbox" in attributes:
            self._mbox = attributes["mbox"]
        if "series" in attributes:
            self._series = attributes["series"]
        if "comments" in attributes:
            self._comments = attributes["comments"]
        if "headers" in attributes:
            self._headers = attributes["headers"]
        if "content" in attributes:
            self._content = attributes["content"]

    def __repr__(self):
        return f"Cover(id:{self._id} name:{self._name})"

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
    def name(self):
        """
        :type: string
        """
        return self._name

    @property
    def mbox(self):
        """
        :type: string
        """
        return self._mbox

    @property
    def comments(self):
        """
        :type: string
        """
        return self._comments

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

    def get_project(self):
        """
        Project detail (partial)

        :rtype: :class:`patchwork.Project.Project`
        """
        return patchwork.Project.Project(self._connection, self._project)

    def get_submitter(self):
        """
        Submitter detail (partial)

        :rtype: :class:`patchwork.People.People`
        """
        return patchwork.People.People(self._connection, self._submitter)

    def get_series(self):
        """
        Series detail

        :rtype: List of :class:`patchwork.Series.Series`
        """
        series = []
        for ser in self._series:
            series.append(patchwork.Series.Series(self._connection, ser))
        return series

    def get_comments(self):
        """
        List comments

        :calls: GET /api/patches/{id}/comments
        :rtype: List of :class:`patchwork.Comment.Comment`
        """
        headers, data = self._connection.request(
            "GET", f"/api/patches/{self._id}/comments"
        )
        comments = []
        for comment in data:
            comments.append(patchwork.Comment.Comment(comment))
        return comments

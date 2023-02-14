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


class Project:
    """
    Class for project object
    """

    def __init__(self, connection, attributes):
        self._connection = connection
        self._id = None
        self._url = None
        self._name = None
        self._link_name = None
        self._list_id = None
        self._list_email = None
        self._web_url = None
        self._scm_url = None
        self._webscm_rul = None
        self._maintainers = None
        self._subject_match = None
        self._list_archive_url = None
        self._list_archive_url_format = None
        self._commit_url_format = None
        self.__update_attributes(attributes)

    def __update_attributes(self, attributes):
        if "id" in attributes:
            self._id = attributes["id"]
        if "url" in attributes:
            self._url = attributes["url"]
        if "name" in attributes:
            self._name = attributes["name"]
        if "link_name" in attributes:
            self._link_name = attributes["link_name"]
        if "list_id" in attributes:
            self._list_id = attributes["list_id"]
        if "list_email" in attributes:
            self._list_email = attributes["list_email"]
        if "web_url" in attributes:
            self._web_url = attributes["web_url"]
        if "scm_url" in attributes:
            self._scm_url = attributes["scm_url"]
        if "webscm_url" in attributes:
            self._webscm_url = attributes["webscm_url"]
        if "maintainers" in attributes:
            self._maintainers = attributes["maintainers"]
        if "subject_match" in attributes:
            self._subject_match = attributes["subject_match"]
        if "list_archive_url" in attributes:
            self._list_archive_url = attributes["list_archive_url"]
        if "list_archive_url_format" in attributes:
            self._list_archive_url_format = attributes["list_archive_url_format"]
        if "commit_url_format" in attributes:
            self._commit_url_format = attributes["commit_url_format"]

    def __repr__(self):
        return f"Project(id:{self._id} name:{self._name})"

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
    def link_name(self):
        """
        :type: string
        """
        return self._link_name

    @property
    def list_id(self):
        """
        :type: string
        """
        return self._list_id

    @property
    def list_email(self):
        """
        :type: string
        """
        return self._list_email

    @property
    def web_url(self):
        """
        :type: string
        """
        return self._web_url

    @property
    def scm_url(self):
        """
        :type: string
        """
        return self._scm_url

    @property
    def webscm_url(self):
        """
        :type: string
        """
        return self._webscm_url

    @property
    def subject_match(self):
        """
        :type: string
        """
        return self._subject_match

    @property
    def list_archive_url(self):
        """
        :type: string
        """
        return self._list_archive_url

    @property
    def list_archive_url_format(self):
        """
        :type: string
        """
        return self._list_archive_url_format

    @property
    def commit_url_format(self):
        """
        :type: string
        """
        return self._commit_url_format

    def get_maintainers(self):
        """
        List of maintainers

        :rtype: List of :class:`patchwork.User.User`
        """
        maintainers = []
        for maintainer in self._maintainers:
            maintainers.append(patchwork.User.User(self._connection, maintainer))
        return maintainers

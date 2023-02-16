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
import patchwork.Cover
import patchwork.Patch
import patchwork.People
import patchwork.Project


class Series:
    """
    Class for Series object
    """

    def __init__(self, connection, attributes):
        self._connection = connection
        self._id = None
        self._url = None
        self._web_url = None
        self._project = None
        self._name = None
        self._date = None
        self._submitter = None
        self._version = None
        self._total = None
        self._received_total = None
        self._received_all = None
        self._mbox = None
        self._cover_letter = None
        self._patches = None
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
        if "name" in attributes:
            self._name = attributes["name"]
        if "date" in attributes:
            self._date = datetime.datetime.strptime(
                attributes["date"], "%Y-%m-%dT%H:%M:%S"
            )
        if "submitter" in attributes:
            self._submitter = attributes["submitter"]
        if "version" in attributes:
            self._version = attributes["version"]
        if "total" in attributes:
            self._total = attributes["total"]
        if "received_total" in attributes:
            self._received_total = attributes["received_total"]
        if "received_all" in attributes:
            self._received_all = attributes["received_all"]
        if "mbox" in attributes:
            self._mbox = attributes["mbox"]
        if "cover_letter" in attributes:
            self._cover_letter = attributes["cover_letter"]
        if "patches" in attributes:
            self._patches = attributes["patches"]

    def __repr__(self):
        return f"Series(id:{self._id} name:{self._name})"

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
    def version(self):
        """
        :type: integer
        """
        return self._version

    @property
    def total(self):
        """
        :type: integer
        """
        return self._total

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
    def received_total(self):
        """
        :type: integer
        """
        return self._received_total

    @property
    def received_all(self):
        """
        :type: boolean
        """
        return self._received_all

    @property
    def mbox(self):
        """
        :type: string
        """
        return self._mbox

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

    def get_patches(self):
        """
        List of Patches

        :rtype: List of :class:`patchwork.Patch.Patch`
        """
        patches = []
        for patch in self._patches:
            patches.append(patchwork.Patch.Patch(self._connection, patch))
        return patches

    def get_cover_letter(self):
        """
        Cover letter detail

        :rtype: :class:`patchwork.Cover.Cover`
        """
        return patchwork.Cover.Cover(self._connection, self._cover_letter)

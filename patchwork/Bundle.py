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
import patchwork.Patch
import patchwork.Project
import patchwork.User


class Bundle:
    """
    Class for Bundle object
    """

    def __init__(self, connection, attributes):
        self._connection = connection
        self._id = None
        self._url = None
        self._web_url = None
        self._project = None
        self._name = None
        self._owner = None
        self._patches = None
        self._public = None
        self._mbox = None
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
        if "owner" in attributes:
            self._owner = attributes["owner"]
        if "patches" in attributes:
            self._patches = attributes["patches"]
        if "public" in attributes:
            self._public = attributes["public"]
        if "mbox" in attributes:
            self._mbox = attributes["mbox"]

    def __repr__(self):
        return f"Bundle(id:{self._id} name:{self._name})"

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
    def name(self):
        """
        :type: string
        """
        return self._name

    @property
    def public(self):
        """
        :type: string
        """
        return self._public

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

    def get_owner(self):
        """
        Owner detail (partial)

        :rtype: :class:`patchwork.User.User`
        """
        return patchwork.User.User(self._connection, self._owner)

    def get_patches(self):
        """
        List of Patches

        :rtype: List of :class:`patchwork.Patch.Patch`
        """
        patches = []
        for patch in self._patches:
            patches.append(patchwork.Patch.Patch(self._connection, patch))
        return patches

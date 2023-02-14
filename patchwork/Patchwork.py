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
import patchwork.Bundle
import patchwork.Connection
import patchwork.Cover
import patchwork.Pagination
import patchwork.Patch
import patchwork.People
import patchwork.Project
import patchwork.Series
import patchwork.User


class Patchwork:
    """
    This is the main class to access the Patchwork API.
    """

    def __init__(
        self,
        base_url,
        token=None,
    ):
        """
        :param base_url: Base url of the Patchwork site
        :type base_url: string
        """
        assert isinstance(base_url, str), "Invalid parameter: base_url"
        if token is not None:
            assert isinstance(token, str), "Invalid parameter: token"

        # Setup connection object
        self.__connection = patchwork.Connection.Connection(
            base_url,
            token,
        )

    def get_user(self, id):
        """
        Show a user

        :calls: GET /api/users/{id}/
        :param id: A unique integer value identifying this user
        :type id: integer
        :rtype: :class:`patchwork.User.User`
        """
        assert isinstance(id, int)

        headers, data = self.__connection.request(
            "GET",
            f"/api/users/{id}",
        )
        return patchwork.User.User(self.__connection, data)

    def get_all_users(self):
        """
        List Users

        :calls: GET /api/users/
        :rtype: :class:`patchwork.Pagination.Pagination` of :class:`patchwork.User.User`
        """
        return patchwork.Pagination.Pagination(
            patchwork.User.User,
            self.__connection,
            "/api/users",
        )

    def get_project(self, id):
        """
        Show a project

        :calls: GET /api/projects/{id}
        :param id: A unique integer value identifying this project
        :type id: integer
        :rtype: :class:`patchwork.Project.Project`
        """
        assert isinstance(id, int)

        headers, data = self.__connection.request(
            "GET",
            f"/api/projects/{id}",
        )
        return patchwork.Project.Project(self.__connection, data)

    def get_all_projects(self):
        """
        List projects

        :calls: GET /api/projects/
        :rtype: :class:`patchwork.Pagination.Pagination` of :class:`patchwork.Project.Project`
        """
        return patchwork.Pagination.Pagination(
            patchwork.Project.Project,
            self.__connection,
            "/api/projects",
        )

    def get_people(self, id):
        """
        Show a people

        :calls: GET /api/people/{id}
        :param id: A unique integer value identifying this person
        :type id: integer
        :rtype: :class:`patchwork.People.People`
        """
        assert isinstance(id, int)

        headers, data = self.__connection.request(
            "GET",
            f"/api/people/{id}",
        )
        return patchwork.People.People(self.__connection, data)

    def get_all_people(self):
        """
        List People

        :calls: GET /api/people/
        :rtype: :class:`patchwork.Pagination.Pagination` of :class:`patchwork.People.People`
        """
        return patchwork.Pagination.Pagination(
            patchwork.People.People,
            self.__connection,
            "/api/people",
        )

    def get_series(self, id):
        """
        Show a series

        :calls: GET /api/series/{id}
        :param id: A unique integer value identifying this series
        :type id: integer
        :rtype: :class:`patchwork.Series.Series`
        """
        assert isinstance(id, int)

        headers, data = self.__connection.request(
            "GET",
            f"/api/series/{id}",
        )
        return patchwork.Series.Series(self.__connection, data)

    def get_all_series(self):
        """
        List series

        :calls: GET /api/series/
        :rtype: :class:`patchwork.Pagination.Pagination` of :class:`patchwork.Series.Series`
        """
        return patchwork.Pagination.Pagination(
            patchwork.Series.Series,
            self.__connection,
            "/api/series",
        )

    def get_cover_letter(self, id):
        """
        Show a cover letter

        :calls: GET /api/covers/{id}
        :param id: A unique integer value identifying this cover letter
        :type id: integer
        :rtype: :class:`patchwork.Cover.Cover`
        """
        assert isinstance(id, int)

        headers, data = self.__connection.request(
            "GET",
            f"/api/covers/{id}",
        )
        return patchwork.Cover.Cover(self.__connection, data)

    def get_all_cover_letters(self):
        """
        List Cover letters

        :calls: GET /api/covers/
        :rtype: :class:`patchwork.Pagination.Pagination` of :class:`patchwork.Cover.Cover`
        """
        return patchwork.Pagination.Pagination(
            patchwork.Cover.Cover,
            self.__connection,
            "/api/covers",
        )

    def get_patch(self, id):
        """
        Show a patch

        :calls: GET /api/patches/{id}
        :param id: A unique integer value identifying this patch
        :type id: integer
        :rtype: :class:`patchwork.Patch.Patch`
        """
        assert isinstance(id, int)

        headers, data = self.__connection.request(
            "GET",
            f"/api/patches/{id}",
        )
        return patchwork.Patch.Patch(self.__connection, data)

    def get_all_patches(self):
        """
        List Patches

        :calls: GET /api/patches/
        :rtype: :class:`patchwork.Pagination.Pagination` of :class:`patchwork.Patch.Patch`
        """
        return patchwork.Pagination.Pagination(
            patchwork.Patch.Patch,
            self.__connection,
            "/api/patches",
        )

    def get_bundle(self, id):
        """
        Show a bundle

        :calls: GET /api/bundles/{id}
        :param id: A unique integer value identifying this bundle
        :type id: integer
        :rtype: :class:`patchwork.Bundle.Bundle`
        """
        assert isinstance(id, int)

        headers, data = self.__connection.request(
            "GET",
            f"/api/bundles/{id}/",
        )
        return patchwork.Bundle.Bundle(self.__connection, data)

    def get_all_bundles(self):
        """
        List Bundles

        :calls: GET /api/bundles
        :rtype: :class:`patchwork.Pagination.Pagination` of :class:`patchwork.Bundle.Bundle`
        """
        return patchwork.Pagination.Pagination(
            patchwork.Bundle.Bundle,
            self.__connection,
            "/api/bundles",
        )

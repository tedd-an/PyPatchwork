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

    def _validate_state(self, state):
        """
        Validate the states

        :param states: List of slug representation of state
        :type states: list
        :rtype: bool
        """
        if state != "" and state in [
            "new",
            "under-review",
            "accepted",
            "rejected",
            "rfc",
            "not-applicable",
            "changes-requested",
            "awaiting-upstream",
            "superseded",
            "deferred",
            "mainlined",
            "queued",
            "needs-ack",
            "handled-elsewhere",
            "in-next",
        ]:
            return True
        return False

    def search_patches(
        self,
        project=None,
        series=None,
        submitter=None,
        delegate=None,
        state=None,
        archived=None,
        hash=None,
        msgid=None,
    ):
        """
        List patches

        :calls: GET /api/patches/
        :param project: An ID or linkname of a project to filter patches by
        :type project: string
        :param series: An ID of a series to filter patches by
        :type series: integer
        :param submitter: An ID or email address of a person to filter patches by.
        :type submitter: string
        :param delegate: An ID or username of a user to filter patches by
        :type delegate: string
        :param state: A slug representation of a state to filter patches by
        :type state: string
        :param archived: Show only archived(True) or non-archived(False) patches
        :type archived: bool
        :param hash: The patch hash as a case-insensitive hexadecial string to filter by
        :type hash: string
        :param msgid: The patch message-id as a case-sensitive string, without leading or trailing angle brackets, to filter by
        :type msgid: string
        :rtype: :class:`patchwork.Pagination.Pagination` of :class:`patchwork.Patch.Patch`
        """
        # Check input parameters
        assert project is None or isinstance(project, str)
        assert series is None or isinstance(series, int)
        assert submitter is None or isinstance(submitter, str)
        assert delegate is None or isinstance(delegate, str)
        assert state is None or isinstance(state, str)
        assert self._validate_state(state)
        assert archived is None or isinstance(archived, bool)
        assert hash is None or isinstance(hash, str)
        assert msgid is None or isinstance(msgid, str)

        # Build the parameters
        params = {}
        if project is not None:
            params["project"] = project
        if series is not None:
            params["series"] = series
        if submitter is not None:
            params["submitter"] = submitter
        if delegate is not None:
            params["delegate"] = delegate
        if archived is not None:
            params["archived"] = archived
        if hash is not None:
            params["hash"] = hash
        if msgid is not None:
            params["msgid"] = msgid
        if state is not None:
            params["state"] = state

        # If all parameters are empty, throws an exception.
        # This is not what this function for...
        assert bool(params), "Illegal operation. Expect at least one parameter"

        return patchwork.Pagination.Pagination(
            patchwork.Patch.Patch,
            self.__connection,
            "/api/patches",
            params,
        )

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

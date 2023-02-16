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
import validators
import patchwork.Check
import patchwork.Comment
import patchwork.Connection
import patchwork.Patch
import patchwork.People
import patchwork.Project
import patchwork.Series
import patchwork.User


class Patch:
    """
    Class for Patch object
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
        self._commit_ref = None
        self._pull_url = None
        self._state = None
        self._archived = None
        self._hash = None
        self._submitter = None
        self._delegate = None
        self._mbox = None
        self._series = None
        self._comments = None
        self._check = None
        self._checks = None
        self._tags = None
        self._related = None
        self._headers = None
        self._content = None
        self._diff = None
        self._prefixes = None
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
        if "commit_ref" in attributes:
            self._commit_ref = attributes["commit_ref"]
        if "pull_url" in attributes:
            self._pull_url = attributes["pull_url"]
        if "state" in attributes:
            self._state = attributes["state"]
        if "archived" in attributes:
            self._archived = attributes["archived"]
        if "hash" in attributes:
            self._hash = attributes["hash"]
        if "submitter" in attributes:
            self._submitter = attributes["submitter"]
        if "delegate" in attributes:
            self._delegate = attributes["delegate"]
        if "mbox" in attributes:
            self._mbox = attributes["mbox"]
        if "series" in attributes:
            self._series = attributes["series"]
        if "comments" in attributes:
            self._comments = attributes["comments"]
        if "check" in attributes:
            self._check = attributes["check"]
        if "checks" in attributes:
            self._checks = attributes["checks"]
        if "tags" in attributes:
            self._tags = attributes["tags"]
        if "related" in attributes:
            self._related = attributes["related"]
        if "headers" in attributes:
            self._headers = attributes["headers"]
        if "content" in attributes:
            self._content = attributes["content"]
        if "diff" in attributes:
            self._diff = attributes["diff"]
        if "prefixes" in attributes:
            self._prefixes = attributes["prefixes"]

    def __repr__(self):
        return f"Patch(id:{self._id} state:{self._state} name:{self._name})"

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
    def commit_ref(self):
        """
        :type: integer
        """
        return self._commit_ref

    @property
    def pull_url(self):
        """
        :type: boolean
        """
        return self._pull_url

    @property
    def state(self):
        """
        :type: string
        """
        return self._state

    @property
    def archived(self):
        """
        :type: string
        """
        return self._archived

    @property
    def hash(self):
        """
        :type: string
        """
        return self._hash

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
    def check(self):
        """
        :type: string
        """
        return self._check

    @property
    def checks(self):
        """
        :type: string
        """
        return self._checks

    @property
    def tags(self):
        """
        :type: dict
        """
        return self._tags

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

    @property
    def diff(self):
        """
        :type: string
        """
        return self._diff

    @property
    def prefixes(self):
        """
        :type: list
        """
        return self._prefixes

    @property
    def related(self):
        return self._related

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
        Series detail (partial)

        :rtype: List of :class:`patchwork.Series.Series`
        """
        series = []
        for ser in self._series:
            series.append(patchwork.Series.Series(self._connection, ser))
        return series

    def get_related(self):
        """
        List of related patch detail (partial)

        :rtype: List of :class:`patchwork.Patch.Patch`
        """
        related = []
        for patch in self._related:
            related.append(patchwork.Patch.Patch(self._connection, patch))
        return related

    def get_delegate(self):
        """
        Delegated User detail (partial)

        :rtype: :class:`patchwork.User.User`
        """
        return patchwork.User.User(self._connection, self._delegate)

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
            comments.append(patchwork.Comment.Comment(self._connection, comment))
        return comments

    def get_checks(self):
        """
        List checks

        :calls: GET /api/patches/{id}/checks
        :rtype: List of :class:`patchwork.Check.Check`
        """
        headers, data = self._connection.request(
            "GET", f"/api/patches/{self._id}/checks"
        )
        checks = []
        for check in data:
            checks.append(patchwork.Check.Check(self._connection, check))
        return checks

    def get_check(self, check_id):
        """
        Show a check

        :calls: GET /api/patches/{id}/checks/{check_id}
        :param check_id: A unique integer value identifying this check
        :type check_id: integer
        :rtype: :class:`patchwork.Check.Check`
        """
        headers, data = self._connection.request(
            "GET", f"/api/patches/{self._id}/checks/{check_id}"
        )
        return patchwork.Check.Check(self._connection, data)

    def create_check(self, user, state, context, target_url=None, description=None):
        """
        Create a check

        :calls: POST /api/patches/{patch_id}/checks/
        :param user: User object
        :type user: :class:`patchwork.User.User`
        :param state: Result of the check like success, warning, fail, pending. Rquired.
        :type state: string
        :param target_url: URL of the check detail. Must be a valid URL. Optional
        :type target_url: string
        :param context: Context of the check like test name. Required field. No space allowed.
        :type context: string
        :param description: Description of the check. Optional
        :type description: string
        :rtype: :class:`patchwork.Check.Check`
        """
        assert isinstance(user, patchwork.User.User), "Invalid parameter: user"
        assert state in [
            "success",
            "warning",
            "fail",
            "pending",
        ], "Invalid parameter: state"
        assert context is not None, "Invalid parameter: context"
        assert " " not in context, "Invalid parameter: context cannot have a space"

        params = {}
        params["user"] = user.id
        params["state"] = state
        params["context"] = context

        if target_url is None:
            params["target_url"] = ""
        else:
            assert validators.url(target_url), "Invalid parameter: target_url"
            params["target_url"] = target_url

        if description is None:
            params["description"] = ""
        else:
            params["description"] = description

        headers, data = self._connection.request(
            "POST", f"/api/patches/{self._id}/checks/", input=params
        )
        return patchwork.Check.Check(self._connection, data)

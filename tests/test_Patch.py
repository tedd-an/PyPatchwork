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
import unittest
import patchwork
import datetime


class TestPatch(unittest.TestCase):
    def setUp(self):
        self.pw = patchwork.Patchwork("https://patchwork.kernel.org")
        self.patch = self.pw.get_patch(12567487)

    def testBasicAttributes(self):
        self.assertEqual(self.patch.id, 12567487)
        self.assertEqual(
            self.patch.url, "https://patchwork.kernel.org/api/patches/12567487/"
        )
        self.assertEqual(
            self.patch.web_url,
            "https://patchwork.kernel.org/project/bluetooth/patch/20211018172833.534191-2-hj.tedd.an@gmail.com/",
        )
        self.assertEqual(
            self.patch.msgid, "<20211018172833.534191-2-hj.tedd.an@gmail.com>"
        )
        self.assertEqual(
            self.patch.list_archive_url,
            "https://lore.kernel.org/r/20211018172833.534191-2-hj.tedd.an@gmail.com",
        )
        self.assertIsInstance(self.patch.date, datetime.datetime)
        self.assertEqual(
            self.patch.name, "[BlueZ,1/9] device: Fix unchecked return value"
        )
        self.assertEqual(self.patch.commit_ref, None)
        self.assertEqual(self.patch.pull_url, None)
        self.assertEqual(self.patch.state, "accepted")
        self.assertEqual(self.patch.archived, False)
        self.assertEqual(self.patch.hash, "f8ffe4bbc6a3f3f2ebf2da58a6d10348f8e4903d")
        self.assertEqual(
            self.patch.mbox,
            "https://patchwork.kernel.org/project/bluetooth/patch/20211018172833.534191-2-hj.tedd.an@gmail.com/mbox/",
        )
        self.assertEqual(
            self.patch.comments,
            "https://patchwork.kernel.org/api/patches/12567487/comments/",
        )
        self.assertEqual(self.patch.check, "success")
        self.assertEqual(
            self.patch.checks,
            "https://patchwork.kernel.org/api/patches/12567487/checks/",
        )
        self.assertEqual(self.patch.tags, {})
        self.assertEqual(self.patch.related, [])
        self.assertEqual(self.patch.prefixes, ["BlueZ", "1/9"])

    def testDateTime(self):
        read_date = datetime.datetime.strptime(
            "2021-10-18T17:28:25", "%Y-%m-%dT%H:%M:%S"
        )
        self.assertEqual(self.patch.date, read_date)

    def testProject(self):
        project = self.patch.get_project()
        self.assertEqual(project.id, 395)
        self.assertEqual(project.url, "https://patchwork.kernel.org/api/projects/395/")
        self.assertEqual(project.name, "Bluetooth")
        self.assertEqual(project.link_name, "bluetooth")
        self.assertEqual(project.list_id, "linux-bluetooth.vger.kernel.org")
        self.assertEqual(project.list_email, "linux-bluetooth@vger.kernel.org")
        self.assertEqual(project.web_url, "")
        self.assertEqual(project.scm_url, "")
        self.assertEqual(project.webscm_url, "")
        self.assertEqual(project.list_archive_url, "")
        self.assertEqual(
            project.list_archive_url_format, "https://lore.kernel.org/r/{}"
        )
        self.assertEqual(project.commit_url_format, "")
        self.assertTrue(self.patch.content.startswith("From: Tedd Ho-Jeong An"))

    def testSubmitter(self):
        submitter = self.patch.get_submitter()
        self.assertEqual(submitter.id, 196023)
        self.assertEqual(
            submitter.url, "https://patchwork.kernel.org/api/people/196023/"
        )
        self.assertEqual(submitter.name, "Tedd An")
        self.assertEqual(submitter.email, "hj.tedd.an@gmail.com")

    def testDelegate(self):
        delegate = self.patch.get_delegate()
        self.assertEqual(delegate.id, 103487)
        self.assertEqual(delegate.url, "https://patchwork.kernel.org/api/users/103487/")
        self.assertEqual(delegate.username, "vudentz")
        self.assertEqual(delegate.first_name, "Luiz")
        self.assertEqual(delegate.last_name, "Von Dentz")
        self.assertEqual(delegate.email, "luiz.dentz@gmail.com")

    def testSeries(self):
        series_list = self.patch.get_series()
        self.assertIsNotNone(series_list)
        self.assertTrue(len(series_list) >= 1)
        for series in series_list:
            self.assertIsInstance(series, patchwork.Series.Series)
        series_0 = series_list[0]
        self.assertEqual(series_0.id, 565705)
        self.assertEqual(
            series_0.url, "https://patchwork.kernel.org/api/series/565705/"
        )
        self.assertEqual(
            series_0.web_url,
            "https://patchwork.kernel.org/project/bluetooth/list/?series=565705",
        )
        self.assertIsInstance(series_0.date, datetime.datetime)
        self.assertEqual(series_0.name, "Fix unchecked return value")
        self.assertEqual(series_0.version, 1)
        self.assertEqual(
            series_0.mbox, "https://patchwork.kernel.org/series/565705/mbox/"
        )

    def testHeaders(self):
        headers = self.patch.headers
        # Only check a few of them..
        self.assertIn("From", headers)
        self.assertEqual(headers["From"], "Tedd Ho-Jeong An <hj.tedd.an@gmail.com>")
        self.assertIn("Subject", headers)
        self.assertEqual(
            headers["Subject"], "[BlueZ PATCH 1/9] device: Fix unchecked return value"
        )
        self.assertIn("Message-Id", headers)
        self.assertEqual(
            headers["Message-Id"], "<20211018172833.534191-2-hj.tedd.an@gmail.com>"
        )

    def testCreateCheckAssertion(self):
        mock_user = {"id": 104215}
        user = patchwork.User.User(None, mock_user)
        # invalid User
        with self.assertRaises(AssertionError):
            self.patch.create_check(None, "a", "b")
        # invalid status
        with self.assertRaises(AssertionError):
            self.patch.create_check(user, "a", "b")
        # Space in context
        with self.assertRaises(AssertionError):
            self.patch.create_check(user, "success", "c ontext")
        # Invalid url format
        with self.assertRaises(AssertionError):
            self.patch.create_check(user, "success", "context", "target")
        # ForbiddenException due to missing token
        with self.assertRaises(patchwork.ForbiddenException):
            self.patch.create_check(user, "fail", "testcontext")

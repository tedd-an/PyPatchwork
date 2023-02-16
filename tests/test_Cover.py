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


class TestCover(unittest.TestCase):
    def setUp(self):
        self.pw = patchwork.Patchwork("https://patchwork.kernel.org")
        self.cover = self.pw.get_cover_letter(12567485)

    def testBasicAttributes(self):
        self.assertEqual(self.cover.id, 12567485)
        self.assertEqual(
            self.cover.url, "https://patchwork.kernel.org/api/covers/12567485/"
        )
        self.assertEqual(
            self.cover.web_url,
            "https://patchwork.kernel.org/project/bluetooth/cover/20211018172833.534191-1-hj.tedd.an@gmail.com/",
        )
        self.assertEqual(
            self.cover.msgid, "<20211018172833.534191-1-hj.tedd.an@gmail.com>"
        )
        self.assertEqual(
            self.cover.list_archive_url,
            "https://lore.kernel.org/r/20211018172833.534191-1-hj.tedd.an@gmail.com",
        )
        self.assertIsInstance(self.cover.date, datetime.datetime)
        self.assertEqual(self.cover.name, "[BlueZ,0/9] Fix unchecked return value")
        self.assertEqual(
            self.cover.mbox,
            "https://patchwork.kernel.org/project/bluetooth/cover/20211018172833.534191-1-hj.tedd.an@gmail.com/mbox/",
        )
        self.assertEqual(
            self.cover.comments,
            "https://patchwork.kernel.org/api/covers/12567485/comments/",
        )
        self.assertTrue(self.cover.content.startswith("From: Tedd Ho-Jeong An"))

    def testDateTime(self):
        read_date = datetime.datetime.strptime(
            "2021-10-18T17:28:24", "%Y-%m-%dT%H:%M:%S"
        )
        self.assertEqual(self.cover.date, read_date)

    def testHeaders(self):
        headers = self.cover.headers
        # Only check a few of them..
        self.assertIn("From", headers)
        self.assertEqual(headers["From"], "Tedd Ho-Jeong An <hj.tedd.an@gmail.com>")
        self.assertIn("Subject", headers)
        self.assertEqual(
            headers["Subject"], "[BlueZ PATCH 0/9] Fix unchecked return value"
        )
        self.assertIn("Message-Id", headers)
        self.assertEqual(
            headers["Message-Id"], "<20211018172833.534191-1-hj.tedd.an@gmail.com>"
        )

    def testProject(self):
        project = self.cover.get_project()
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

    def testSubmitter(self):
        submitter = self.cover.get_submitter()
        self.assertEqual(submitter.id, 196023)
        self.assertEqual(
            submitter.url, "https://patchwork.kernel.org/api/people/196023/"
        )
        self.assertEqual(submitter.name, "Tedd An")
        self.assertEqual(submitter.email, "hj.tedd.an@gmail.com")

    def testSeries(self):
        series_list = self.cover.get_series()
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

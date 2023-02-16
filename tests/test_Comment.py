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


class TestComment(unittest.TestCase):
    def setUp(self):
        self.pw = patchwork.Patchwork("https://patchwork.kernel.org")
        self.patch = self.pw.get_patch(12567487)
        comments = self.patch.get_comments()
        self.assertIsNotNone(comments)
        self.assertTrue(len(comments) >= 1)
        self.comment = comments[0]
        self.assertIsInstance(self.comment, patchwork.Comment.Comment)

    def testBasicAttributes(self):
        self.assertEqual(self.comment.id, 24531077)
        self.assertEqual(
            self.comment.web_url, "https://patchwork.kernel.org/comment/24531077/"
        )
        self.assertEqual(
            self.comment.msgid, "<616db65f.1c69fb81.c4a83.fe17@mx.google.com>"
        )
        self.assertEqual(
            self.comment.list_archive_url,
            "https://lore.kernel.org/r/616db65f.1c69fb81.c4a83.fe17@mx.google.com",
        )
        self.assertIsInstance(self.comment.date, datetime.datetime)
        self.assertEqual(self.comment.subject, "RE: Fix unchecked return value")
        self.assertTrue(self.comment.content.startswith("This is automated email"))

    def testDateTime(self):
        read_date = datetime.datetime.strptime(
            "2021-10-18T18:01:03", "%Y-%m-%dT%H:%M:%S"
        )
        self.assertEqual(self.comment.date, read_date)

    def testHeaders(self):
        headers = self.comment.headers
        # Only check a few of them..
        self.assertIn("From", headers)
        self.assertEqual(headers["From"], "bluez.test.bot@gmail.com")
        self.assertIn("Subject", headers)
        self.assertEqual(headers["Subject"], "RE: Fix unchecked return value")

    def testSubmitter(self):
        submitter = self.comment.get_submitter()
        self.assertEqual(submitter.id, 191843)
        self.assertEqual(
            submitter.url, "https://patchwork.kernel.org/api/people/191843/"
        )
        self.assertEqual(submitter.name, None)
        self.assertEqual(submitter.email, "bluez.test.bot@gmail.com")

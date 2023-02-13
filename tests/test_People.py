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
import os

import patchwork


class TestPeople(unittest.TestCase):
    def testBasicAttributes(self):
        self.assertIn(
            "PW_USER_TOKEN", os.environ, "Missing PW_TOKEN environment variable"
        )
        self.pw = patchwork.Patchwork(
            "https://patchwork.kernel.org", os.environ["PW_USER_TOKEN"]
        )
        self.people = self.pw.get_people(196023)
        self.assertEqual(self.people.id, 196023)
        self.assertEqual(
            self.people.url, "https://patchwork.kernel.org/api/people/196023/"
        )
        self.assertEqual(self.people.name, "Tedd An")
        self.assertEqual(self.people.email, "hj.tedd.an@gmail.com")
        self.assertIsInstance(self.people.get_user_info(), patchwork.User.User)

    def testNoToken(self):
        self.pw = patchwork.Patchwork("https://patchwork.kernel.org")
        with self.assertRaises(patchwork.ForbiddenException):
            self.people = self.pw.get_people(196023)

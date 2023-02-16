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


class TestCheck(unittest.TestCase):
    def setUp(self):
        self.pw = patchwork.Patchwork("https://patchwork.kernel.org")
        self.patch = self.pw.get_patch(12567487)
        checks = self.patch.get_checks()
        self.assertIsNotNone(checks)
        self.assertTrue(len(checks) >= 1)
        self.check = checks[0]
        self.assertIsInstance(self.check, patchwork.Check.Check)

    def testBasicAttributes(self):
        self.assertEqual(self.check.id, 745895)
        self.assertEqual(
            self.check.url,
            "https://patchwork.kernel.org/api/patches/12567487/checks/745895/",
        )
        self.assertEqual(self.check.state, "success")
        self.assertIsInstance(self.check.date, datetime.datetime)
        self.assertEqual(
            self.check.target_url, "https://github.com/BluezTestBot/bluez/pull/1042"
        )
        self.assertEqual(self.check.context, "checkpatch")
        self.assertEqual(self.check.description, "Checkpatch PASS")

    def testDateTime(self):
        read_date = datetime.datetime.strptime(
            "2021-10-18T17:47:10.203518", "%Y-%m-%dT%H:%M:%S.%f"
        )
        self.assertEqual(self.check.date, read_date)

    def testUser(self):
        user = self.check.get_user()
        self.assertIsInstance(user, patchwork.User.User)
        self.assertEqual(user.id, 104215)
        self.assertEqual(user.url, "https://patchwork.kernel.org/api/users/104215/")
        self.assertEqual(user.username, "tedd_an")
        self.assertEqual(user.first_name, "Tedd")
        self.assertEqual(user.last_name, "An")
        self.assertEqual(user.email, "tedd.an@intel.com")


"""
"""

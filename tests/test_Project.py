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


class TestProject(unittest.TestCase):
    def setUp(self):
        self.pw = patchwork.Patchwork("https://patchwork.kernel.org")
        self.bt = self.pw.get_project(395)

    def testBasicAttributes(self):
        self.assertEqual(self.bt.id, 395)
        self.assertEqual(self.bt.url, "https://patchwork.kernel.org/api/projects/395/")
        self.assertEqual(self.bt.name, "Bluetooth")
        self.assertEqual(self.bt.link_name, "bluetooth")
        self.assertEqual(self.bt.list_id, "linux-bluetooth.vger.kernel.org")
        self.assertEqual(self.bt.list_email, "linux-bluetooth@vger.kernel.org")
        self.assertEqual(self.bt.web_url, "")
        self.assertEqual(self.bt.scm_url, "")
        self.assertEqual(self.bt.webscm_url, "")
        self.assertEqual(self.bt.subject_match, "")
        self.assertEqual(self.bt.list_archive_url, "")
        self.assertEqual(
            self.bt.list_archive_url_format, "https://lore.kernel.org/r/{}"
        )
        self.assertEqual(self.bt.commit_url_format, "")

    def testMaintainersList(self):
        maintainers = self.bt.get_maintainers()
        self.assertEqual(len(maintainers), 6)
        for maintainer in maintainers:
            self.assertIsInstance(maintainer, patchwork.User.User)

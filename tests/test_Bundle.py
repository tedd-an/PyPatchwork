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
import os
import unittest
import patchwork
import datetime


class TestBundle(unittest.TestCase):
    def setUp(self):
        self.assertIn(
            "PW_USER_TOKEN", os.environ, "Missing PW_TOKEN environment variable"
        )
        self.pw = patchwork.Patchwork(
            "https://patchwork.kernel.org", os.environ["PW_USER_TOKEN"]
        )
        self.bundle = self.pw.get_bundle(34802)

    def testNoToken(self):
        self.pw = patchwork.Patchwork("https://patchwork.kernel.org")
        with self.assertRaises(patchwork.NotFoundException):
            self.bundle = self.pw.get_bundle(34802)

    def testBasicAttributes(self):
        self.assertEqual(self.bundle.id, 34802)
        self.assertEqual(
            self.bundle.url, "https://patchwork.kernel.org/api/bundles/34802/"
        )
        self.assertEqual(
            self.bundle.web_url,
            "https://patchwork.kernel.org/bundle/tedd_an/Fix%20unchecked%20return%20value/",
        )
        self.assertEqual(self.bundle.name, "Fix unchecked return value")
        self.assertFalse(self.bundle.public)
        self.assertEqual(
            self.bundle.mbox,
            "https://patchwork.kernel.org/bundle/tedd_an/Fix%20unchecked%20return%20value/mbox/",
        )

    def testProject(self):
        project = self.bundle.get_project()
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

    def testOwner(self):
        user = self.bundle.get_owner()
        self.assertIsInstance(user, patchwork.User.User)
        self.assertEqual(user.id, 104215)
        self.assertEqual(user.url, "https://patchwork.kernel.org/api/users/104215/")
        self.assertEqual(user.username, "tedd_an")
        self.assertEqual(user.first_name, "Tedd")
        self.assertEqual(user.last_name, "An")
        self.assertEqual(user.email, "tedd.an@intel.com")

    def testPatches(self):
        patches = self.bundle.get_patches()
        self.assertIsNotNone(patches)
        self.assertEqual(len(patches), 9)
        patch_0 = patches[0]
        self.assertIsInstance(patch_0, patchwork.Patch.Patch)
        self.assertEqual(patch_0.id, 12567487)
        self.assertEqual(
            patch_0.url, "https://patchwork.kernel.org/api/patches/12567487/"
        )
        self.assertEqual(
            patch_0.web_url,
            "https://patchwork.kernel.org/project/bluetooth/patch/20211018172833.534191-2-hj.tedd.an@gmail.com/",
        )
        self.assertEqual(
            patch_0.msgid, "<20211018172833.534191-2-hj.tedd.an@gmail.com>"
        )
        self.assertEqual(
            patch_0.list_archive_url,
            "https://lore.kernel.org/r/20211018172833.534191-2-hj.tedd.an@gmail.com",
        )
        self.assertIsInstance(patch_0.date, datetime.datetime)
        self.assertEqual(patch_0.name, "[BlueZ,1/9] device: Fix unchecked return value")
        self.assertEqual(
            patch_0.mbox,
            "https://patchwork.kernel.org/project/bluetooth/patch/20211018172833.534191-2-hj.tedd.an@gmail.com/mbox/",
        )

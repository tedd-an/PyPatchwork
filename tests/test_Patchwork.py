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


class TestPatchwork(unittest.TestCase):
    def setUp(self):
        self.assertIn(
            "PW_USER_TOKEN", os.environ, "Missing PW_TOKEN environment variable"
        )
        self.pw = patchwork.Patchwork(
            "https://patchwork.kernel.org", os.environ["PW_USER_TOKEN"]
        )

    def testInvalidParameters(self):
        with self.assertRaises(AssertionError):
            patchwork.Patchwork(123)
        with self.assertRaises(AssertionError):
            patchwork.Patchwork("dummy", 123)

    def testGet_CheckInstance(self):
        self.assertIsInstance(self.pw.get_user(104215), patchwork.User.User)
        self.assertIsInstance(self.pw.get_project(395), patchwork.Project.Project)
        self.assertIsInstance(self.pw.get_people(196023), patchwork.People.People)
        self.assertIsInstance(self.pw.get_series(565705), patchwork.Series.Series)
        self.assertIsInstance(self.pw.get_cover_letter(12567485), patchwork.Cover.Cover)
        self.assertIsInstance(self.pw.get_patch(12567487), patchwork.Patch.Patch)
        self.assertIsInstance(self.pw.get_bundle(34802), patchwork.Bundle.Bundle)

    def testGet_InvalidParameter(self):
        with self.assertRaises(AssertionError):
            self.pw.get_user("104215")
        with self.assertRaises(AssertionError):
            self.pw.get_project("395")
        with self.assertRaises(AssertionError):
            self.pw.get_people("196023"),
        with self.assertRaises(AssertionError):
            self.pw.get_series("565705")
        with self.assertRaises(AssertionError):
            self.pw.get_cover_letter("12567485")
        with self.assertRaises(AssertionError):
            self.pw.get_patch("12567487")
        with self.assertRaises(AssertionError):
            self.pw.get_bundle("34802")

    def runGetAll(self, func, cls, max_count=35):
        all = func()
        count = 0
        for item in all:
            if count >= max_count:
                break
            self.assertIsInstance(item, cls)
            count += 1

    def testGetAll(self):
        self.runGetAll(self.pw.get_all_projects, patchwork.Project.Project)
        self.runGetAll(self.pw.get_all_users, patchwork.User.User)
        self.runGetAll(self.pw.get_all_people, patchwork.People.People)
        self.runGetAll(self.pw.get_all_series, patchwork.Series.Series)
        self.runGetAll(self.pw.get_all_cover_letters, patchwork.Cover.Cover)
        self.runGetAll(self.pw.get_all_patches, patchwork.Patch.Patch)
        self.runGetAll(self.pw.get_all_bundles, patchwork.Bundle.Bundle)

    def testSearchPatchError(self):
        with self.assertRaises(AssertionError):
            self.pw.search_patches()
        with self.assertRaises(AssertionError):
            self.pw.search_patches(project=1)
        with self.assertRaises(AssertionError):
            self.pw.search_patches(series="one")
        with self.assertRaises(AssertionError):
            self.pw.search_patches(submitter=1)
        with self.assertRaises(AssertionError):
            self.pw.search_patches(delegate=1)
        with self.assertRaises(AssertionError):
            self.pw.search_patches(archived=1)
        with self.assertRaises(AssertionError):
            self.pw.search_patches(hash=1)
        with self.assertRaises(AssertionError):
            self.pw.search_patches(msgid=1)
        with self.assertRaises(AssertionError):
            self.pw.search_patches(state=1)
        with self.assertRaises(AssertionError):
            self.pw.search_patches(state="notnew")

    def testSearchPatch(self):
        patches = self.pw.search_patches(
            project="bluetooth", state="new", archived=False
        )
        self.assertTrue(bool(patches))
        for patch in patches:
            self.assertEqual(patch.state, "new")
            self.assertFalse(patch.archived)
            project = patch.get_project()
            self.assertEqual(project.link_name, "bluetooth")

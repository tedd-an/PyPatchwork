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


class TestSeries(unittest.TestCase):
    def setUp(self):
        self.pw = patchwork.Patchwork("https://patchwork.kernel.org")
        self.series = self.pw.get_series(565705)

    def testBasicAttributes(self):
        self.assertEqual(self.series.id, 565705)
        self.assertEqual(
            self.series.url, "https://patchwork.kernel.org/api/series/565705/"
        )
        self.assertEqual(
            self.series.web_url,
            "https://patchwork.kernel.org/project/bluetooth/list/?series=565705",
        )
        self.assertEqual(self.series.name, "Fix unchecked return value")
        self.assertIsInstance(self.series.date, datetime.datetime)
        self.assertEqual(self.series.version, 1)
        self.assertEqual(self.series.total, 9)
        self.assertEqual(self.series.received_total, 9)
        self.assertTrue(self.series.received_all)
        self.assertEqual(
            self.series.mbox, "https://patchwork.kernel.org/series/565705/mbox/"
        )
        self.assertIsInstance(self.series.get_project(), patchwork.Project.Project)
        self.assertIsInstance(self.series.get_submitter(), patchwork.People.People)
        self.assertIsInstance(self.series.get_cover_letter(), patchwork.Cover.Cover)
        patches = self.series.get_patches()
        self.assertIsNotNone(patches)
        for patch in patches:
            self.assertIsInstance(patch, patchwork.Patch.Patch)

    def testDateTime(self):
        read_date = datetime.datetime.strptime(
            "2021-10-18T17:28:24", "%Y-%m-%dT%H:%M:%S"
        )
        self.assertEqual(self.series.date, read_date)

    def testProject(self):
        project = self.series.get_project()
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
        submitter = self.series.get_submitter()
        self.assertEqual(submitter.id, 196023)
        self.assertEqual(
            submitter.url, "https://patchwork.kernel.org/api/people/196023/"
        )
        self.assertEqual(submitter.name, "Tedd An")
        self.assertEqual(submitter.email, "hj.tedd.an@gmail.com")

    def testCoverLetter(self):
        cover = self.series.get_cover_letter()
        self.assertEqual(cover.id, 12567485)
        self.assertEqual(cover.url, "https://patchwork.kernel.org/api/covers/12567485/")
        self.assertEqual(
            cover.web_url,
            "https://patchwork.kernel.org/project/bluetooth/cover/20211018172833.534191-1-hj.tedd.an@gmail.com/",
        )
        self.assertEqual(cover.msgid, "<20211018172833.534191-1-hj.tedd.an@gmail.com>")
        self.assertEqual(
            cover.list_archive_url,
            "https://lore.kernel.org/r/20211018172833.534191-1-hj.tedd.an@gmail.com",
        )
        self.assertIsInstance(cover.date, datetime.datetime)
        self.assertEqual(cover.name, "[BlueZ,0/9] Fix unchecked return value")
        self.assertEqual(
            cover.mbox,
            "https://patchwork.kernel.org/project/bluetooth/cover/20211018172833.534191-1-hj.tedd.an@gmail.com/mbox/",
        )

    def testPatches(self):
        patches = self.series.get_patches()
        patch_0 = patches[0]
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

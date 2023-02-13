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


class TestConnection(unittest.TestCase):
    def testWithToken(self):
        self.assertIn(
            "PW_USER_TOKEN", os.environ, "Missing PW_TOKEN environment variable"
        )
        self.pw = patchwork.Patchwork(
            "https://patchwork.kernel.org", os.environ["PW_USER_TOKEN"]
        )
        self.bundle = self.pw.get_bundle(34802)
        self.assertIsInstance(self.bundle, patchwork.Bundle.Bundle)

    def testNoToken(self):
        self.pw = patchwork.Patchwork("https://patchwork.kernel.org")
        with self.assertRaises(patchwork.NotFoundException):
            self.bundle = self.pw.get_bundle(34802)

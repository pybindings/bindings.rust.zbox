# coding: utf-8

import unittest
import uuid

from fs.test import FSTestCases

try:
    from bindings.rust.zbox import ZboxFS
except ImportError:
    ZboxFS = None


@unittest.skip("Segfaults !")
@unittest.skipUnless(ZboxFS, "fs not available")
class TestZboxFS(FSTestCases, unittest.TestCase):

    def make_fs(self):
        fs = ZboxFS("mem://")
        fs.removetree('/')
        return fs
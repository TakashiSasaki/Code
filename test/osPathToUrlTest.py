import unittest
import marker.osPathToUrl
import marker.osPathToUrl2
import pathlib

class osPathToUrl(unittest.TestCase):
    path1 = "///a//b////c"
    path2 = "\\\\\\a\\\\\\\\b\\\\\\\\c\\d"

    def test_path1(self):
        x = marker.osPathToUrl.osPathToUrl(osPathToUrl.path1)
        self.assertRegex(x, "file://.+/a/b/c")
    
    def test_path2(self):
        x = marker.osPathToUrl.osPathToUrl(osPathToUrl.path2)
        self.assertRegex(x, "file://.+/a/b/c/d")

    def test_path3(self):
        x = marker.osPathToUrl2.osPathToUrl2(osPathToUrl.path1)
        self.assertRegex(x, "file://.+/a/b/c")

    def test_splitAll_1(self):
        x = marker.osPathToUrl.splitAll("/a/b/c")
        self.assertListEqual(x, ['a', 'b', 'c'])
    
    def test_splitAll_2(self):
        x = marker.osPathToUrl.splitAll("x/y/z/")
        self.assertListEqual(x, ["x", "y", "z"])

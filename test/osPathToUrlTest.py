import unittest
import marker.osPathToUrl1
import marker.osPathToUrl2
import pathlib

class osPathToUrlTest(unittest.TestCase):
    path1 = "///a//b////c"
    path2 = "\\\\\\a\\\\\\\\b\\\\\\\\c\\d"

    def test_path1(self):
        x = marker.osPathToUrl1.osPathToUrl1(osPathToUrlTest.path1)
        self.assertRegex(x, "file://.+/a/b/c")
    
    def test_path2(self):
        x = marker.osPathToUrl1.osPathToUrl1(osPathToUrlTest.path2)
        self.assertRegex(x, "file://.+/a/b/c/d")

    def test_path3(self):
        x = marker.osPathToUrl2.osPathToUrl2(osPathToUrlTest.path1)
        self.assertRegex(x, "file://.+/a/b/c")

    def test_splitAll_1(self):
        x = marker.osPathToUrl1.splitAll("/a/b/c")
        self.assertListEqual(x, ['a', 'b', 'c'])
    
    def test_splitAll_2(self):
        x = marker.osPathToUrl1.splitAll("x/y/z/")
        self.assertListEqual(x, ["x", "y", "z"])

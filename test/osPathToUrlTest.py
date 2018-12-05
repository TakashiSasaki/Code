import unittest
import pathlib
import marker.OsPath

class osPathToUrlTest(unittest.TestCase):
    path1 = "///a//b////c"
    path2 = "\\\\\\a\\\\\\\\b\\\\\\\\c\\d"

    def test_path1(self):
        x = marker.OsPath.osPathToUrl1(osPathToUrlTest.path1)
        self.assertRegex(x, "file://.+/a/b/c")
    
    def test_path2(self):
        x = marker.OsPath.osPathToUrl1(osPathToUrlTest.path2)
        self.assertRegex(x, "file://.+/a/b/c/d")

    def test_path3(self):
        x = marker.OsPath.osPathToUrl2(osPathToUrlTest.path1)
        self.assertRegex(x, "file://.+/a/b/c")

    def test_splitAll_1(self):
        x = marker.OsPath.splitAll("/a/b/c")
        self.assertListEqual(x, ['a', 'b', 'c'])
    
    def test_splitAll_2(self):
        x = marker.OsPath.splitAll("x/y/z/")
        self.assertListEqual(x, ["x", "y", "z"])


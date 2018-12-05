import unittest
import marker.osPathToUrl

class osPathToUrl(unittest.TestCase):
    def test_path1(self):
        path1 = "///a//b////c"
        x = marker.osPathToUrl.osPathToUrl(path1)
        self.assertRegex(x, "file://.+/a/b/c")
    
    def test_path2(self):
        path2 = "\\\\\\a\\\\\\\\b\\\\\\\\c\\d"
        x = marker.osPathToUrl.osPathToUrl(path2)
        self.assertRegex(x, "file://.+/a/b/c/d")

    def test_splitAll_1(self):
        x = marker.osPathToUrl.splitAll("/a/b/c")
        self.assertListEqual(x, ['a', 'b', 'c'])
    
    def test_splitAll_2(self):
        x = marker.osPathToUrl.splitAll("x/y/z/")
        self.assertListEqual(x, ["x", "y", "z"])

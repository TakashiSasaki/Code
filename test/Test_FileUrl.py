import unittest, pathlib, marker, os.path

PATH1 = "///a//b////c"
PATH2 = "\\\\\\a\\\\\\\\b\\\\\\\\c\\d"

class Test_FileUrl(unittest.TestCase):

    def test_path1(self):
        x = marker.osPathToUrl1(PATH1)
        self.assertRegex(x, "file://.+/a/b/c")
    
    def test_path2(self):
        x = marker.osPathToUrl1(PATH2)
        self.assertRegex(x, "file://.+/a/b/c/d")

    def test_path3(self):
        x = marker.osPathToUrl2(PATH1)
        self.assertRegex(x, "file://.+/a/b/c")

    def test_splitAll_1(self):
        x = marker.splitAll("/a/b/c")
        self.assertListEqual(x, ['a', 'b', 'c'])
    
    def test_splitAll_2(self):
        x = marker.splitAll("x/y/z/")
        self.assertListEqual(x, ["x", "y", "z"])

    def test_FileUrl1(self):
        x = marker.FileUrl("file://aaa/b/c/d")
        self.assertEqual(x.netloc, "aaa")
        self.assertEqual(x.path, "/b/c/d")

    def test_FileUrl2(self):
        absPath = os.path.abspath(".")
        x = marker.FileUrl(absPath)
        self.assertRegex(x.netloc, ".+")
        self.assertRegex(x.path, "/.:/.+[^/]")

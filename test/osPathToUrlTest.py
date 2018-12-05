import unittest
import marker.osPathToUrl

class osPathToUrl(unittest.TestCase):
    def test_path1(self):
        path1 = "///a//b////c"
        x = marker.osPathToUrl.osPathToUrl(path1)
        self.assertEqual(x, "/a/b/c")
        return
    
    def test_path2(self):
        path2 = "\\\\\\a\\\\\\\\b\\\\\\\\c\\d"
        x = marker.osPathToUrl.osPathToUrl(path2)
        self.assertEqual(x, "/a/b/c/d")
        return

    def test_hello(self):
        print("test_hello")
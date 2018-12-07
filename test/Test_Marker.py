from unittest import TestCase
from marker import Marker
import os.path

class Test_Marker(TestCase):
    def setUp(self):
        pass

    def test(self):
        self.assertEqual(os.path.sep, "\\")
        self.assertEqual(os.path.altsep, "/")
        self.assertEqual(os.path.pathsep, ";")

    def test_magic(self):
        m = Marker()
        self.assertTrue(m.checkDnsMagic())

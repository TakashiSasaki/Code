import binascii
import unittest
import hash.Md5Hex
import hash.Md5Bytes


def fromUtf8(testCase):
    x = testCase.CLASS()
    y = x.fromUtf8("hello")
    testCase.assertEqual(x,y)
    repr = x.__repr__()
    testCase.assertEqual(repr, b"5d41402abc4b2a76b9719d911017c592")

def fromHex(testCase):
    x = testCase.CLASS()
    y = x.fromHex("5d41402abc4b2a76b9719d911017c592")
    testCase.assertEqual(x,y)
    repr = x.__repr__()
    testCase.assertEqual(repr, b"5d41402abc4b2a76b9719d911017c592")

def fromBytes(testCase):
    x = testCase.CLASS()
    y = x.fromBytes(binascii.a2b_hex("5d41402abc4b2a76b9719d911017c592"))
    testCase.assertEqual(x,y)
    s = str(x)
    testCase.assertEqual(s, "5d41402abc4b2a76b9719d911017c592")

class Test_Md5Hex_Test(unittest.TestCase):
    def __init__(self, testName):
        self.CLASS = hash.Md5Hex.Md5Hex
    def test_fromUtf8(self):
        fromUtf8(self)
    def test_fromBytes(self):
        fromBytes(self)
    def test_fromHex(self):
        fromHex(self)

class Test_Md5Bytes_Test(unittest.TestCase):
    def setUp(self):
        self.CLASS = hash.Md5Bytes.Md5Bytes
    def test_fromUtf8(self):
        fromUtf8(self)
    def test_fromBytes(self):
        fromBytes(self)
    def test_fromHex(self):
        fromHex(self)

class Test_Sha1Bytes_Test(unittest.TestCase):
    def setUp(self):
        self.CLASS = hash.Sha1Bytes.Sha1Bytes
    def test_fromUtf8(self):
        fromUtf8(self)
    def test_fromBytes(self):
        fromBytes(self)
    def test_fromHex(self):
        fromHex(self)

class Test_Sha1Hex_Test(unittest.TestCase):
    def setUp(self):
        self.CLASS = hash.Sha1Hex.Sha1Hex
    def test_fromUtf8(self):
        fromUtf8(self)
    def test_fromBytes(self):
        fromBytes(self)
    def test_fromHex(self):
        fromHex(self)

class Test_Hello(unittest.TestCase):
    def setUp(self):
        unittest.TestCase(self)
    def test_hello(self):
        pass
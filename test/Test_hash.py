import hash.Md5Bytes
import unittest, binascii

class Test_Md5Bytes(unittest.TestCase):
    def test_fromUtf8(self):
        md5bytes = hash.Md5Bytes.Md5Bytes()
        md5bytes.fromUtf8("hello")
        x = md5bytes.__repr__()
        self.assertEqual(x, b"5d41402abc4b2a76b9719d911017c592")

    def test_fromHex(self):
        md5bytes = hash.Md5Bytes.Md5Bytes()
        md5bytes.fromHex("5d41402abc4b2a76b9719d911017c592")
        x = md5bytes.__repr__()
        self.assertEqual(x, b"5d41402abc4b2a76b9719d911017c592")

    def test_fromBytes(self):
        md5bytes = hash.Md5Bytes.Md5Bytes()
        md5bytes.fromBytes(binascii.a2b_hex("5d41402abc4b2a76b9719d911017c592"))
        self.assertEqual(str(md5bytes), "5d41402abc4b2a76b9719d911017c592")

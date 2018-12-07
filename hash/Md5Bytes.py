import hashlib
from .hex import bytesToHex
import binascii
from .xor import xorBytes

class Md5Bytes(object):
    __slots__ = ["bytes"]

    def __init__(self, x=None):
        if x is None:
            self.bytes = b"\0" * 16
        else:
            assert isinstance(x, bytes)
            assert len(x) == 16
            self.bytes = x
    
    def fromUtf8(self, s:str):
        m = hashlib.md5()
        m.update(s.encode("utf-8"))
        self.__init__(m.digest())
        return self

    def fromBytes(self, b:bytes):
        self.__init__(b)
        return self

    def fromHex(self, h:str):
        b = binascii.a2b_hex(h)
        self.__init__(b)
        return self

    def __repr__(self) -> str:
        return binascii.hexlify(self.bytes)

    def __str__(self) -> str:
        s = binascii.b2a_hex(self.bytes)
        return s.decode("ascii")

    def __xor__(self, right):
        return Md5Bytes(xorBytes(self.bytes, right))

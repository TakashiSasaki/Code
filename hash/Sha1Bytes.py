from hex import bytesToHex
from xor import xorBytes
import hashlib, binascii

class Sha1Bytes(object):
    __slots__ = ["bytes"]

    def __init__(self, bytes:bytes):
        if bytes is None:
            self.bytes = b"\0" * 20
        else:
            assert isinstance(bytes, bytes)
            assert len(bytes) == 20
            self.bytes = bytes
    
    def loadUtf8(self, utf8:str):
        m = hashlib.sha1()
        m.update(utf8.encode("utf-8"))
        self.__init__(m.digest())
        return self

    def loadBytes(self, bytse: bytes):
        self.__init__(bytes)
        return self

    def loadHex(self, hex: str):
        self.__init__(binascii.unhexlify(str))
        return self
        
    def __repr__(self):
        return bytesToHex(self.bytes)

    def __xor__(self, right: Sha1Bytes):
        return Sha1Bytes(xorBytes(self.bytes, right.bytes))

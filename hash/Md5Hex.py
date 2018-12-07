import hashlib
from .hex import bytesToHex
from .xor import xorHexStrings

class Md5Hex(object):
    __slots__=["hex"]

    def __init__(self, s=None):
        if s is None:
            self.hex = "0" * 16
        else:
            assert isinstance(s, str)
            assert len(s) == 16
            self.hex = s

    def fromUtf8(self, s:str):
        m = hashlib.md5()
        m.update(s.encode("utf-8"))
        self.__init__(m.hexdigest())
        return self
    
    def fromBytes(self, b:bytes):
        self.__init__(bytesToHex(b))
        return self
    
    def fromHex(self, hex):
        self.__init__(hex)
        return self

    def __repr__(self) -> str:
        return self.hex

    def __xor__(self, right):
        return Md5Hex(xorHexStrings(self.hex, right.hex))


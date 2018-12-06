import hashlib
from xor import xorHexStrings
from hex import bytesToHex

class Sha1Hex(object):
    __slots__ = ["hex"]

    def __init__(self, s=None):
        if s is None:
            self.hex = "0" * 40
        else:
            assert isinstance(s, str)
            assert len(s) == 40
            self.hex = s

    def fromUtf8(self, s:str):
        m = hashlib.sha1()
        m.update(s.encode("utf-8"))
        self.__init__(m.hexdigest())
        return self
    
    def fromBytes(self, b:bytes):
        self.__init__(bytesToHex(b))
        return self

    def fromHex(self, h:str):
        self.__init__(h)
        return self

    def __repr__(self) -> str:
        return self.hex

    def __xor__(self, right: Sha1Hex) -> Sha1Hex:
        return Sha1Hex(xorHexStrings(self.hex, right.hex))

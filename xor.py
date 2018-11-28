from singledispatch import singledispatch

hexdict = {}
for x in range(16):
    hexdict[format(x,"01x")] = {}
    for y in range(16):
        hexdict[format(x,"01x")][format(y,"01x")] = format(x^y,"01x")

def xorHexStrings(hexString1:str, hexString2:str) -> str:
    z = []
    for x,y in zip(hexString1, hexString2):
        z.append(hexdict[x.lower()][y.lower()])
    return "".join(z)

def utf8Md5Bytes(s : str) -> bytes:
    m = hashlib.md5()
    m.update(s.encode("utf-8"))
    return m.digest()

def utf8md5Hex(s:str) -> str:
    m = hashlib.md5()
    m.update(s.encode("utf-8"))
    return m.hexdigest()

def utf8Sha1Bytes(s:str) ->bytes:
    m = hashlib.sha1()
    m.update(s.encode("utf-8"))
    return m.digest()

def utf8Sha1Hex(s:str) ->bytes:
    m = hashlib.sha1()
    m.update(s.encode("utf-8"))
    return m.hexdigest()

def xorBytes(bytes1 : bytes, bytes2: bytes) -> bytes:
    return b"".join([(x^y).to_bytes(1, "big") for x,y in zip(bytes1, bytes2)])

def bytesToHex(bytes1: bytes) -> str:
    return "".join([format(b, "02x") for b in bytes1])

import hashlib

def xorUtf8Md5(string1:str, string2:str) -> str:
    bytes1 = utf8Md5Bytes(string1)
    bytes2 = utf8Md5Bytes(string2)
    bytes3 =  xorBytes(bytes1, bytes2)

    hex1 = bytesToHex(bytes1)
    hex2 = bytesToHex(bytes2)
    hex3 = xorHexStrings(hex1, hex2)

    assert(bytesToHex(bytes3) == hex3)
    return hex3

def xorUtf8Sha1(string1: str, string2: str) -> str:
    bytes1 = utf8Sha1Bytes(string1)
    bytes2 = utf8Sha1Bytes(string2)
    bytes3 = xorBytes(bytes1, bytes2)

    hex1 = utf8Sha1Hex(string1)
    hex2 = utf8Sha1Hex(string2)
    hex3 = xorHexStrings(hex1, hex2)

    assert(bytesToHex(bytes3) == hex3)
    return hex3

import functools
def xorUtf8Sha1All(stringList: list) -> str:
    bytesList = map(lambda x: utf8Sha1Bytes(x), stringList)
    x = functools.reduce(lambda x,y: xorBytes(x,y), bytesList)
    return bytesToHex(x)

def xorUtf8Md5All(stringList: list) -> str:
    bytesList = map(lambda x: utf8Md5Bytes(x), stringList)
    x = functools.reduce(lambda x,y: xorBytes(x,y), bytesList)
    return bytesToHex(x)

if __name__ == "__main__":
    print(xorUtf8Md5("hello", "world"))
    print(xorUtf8Sha1("hello", "world"))
    print(xorUtf8Sha1All(["hello", "world"]))
    print(xorUtf8Md5All(["hello", "world"]))

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

def xorBytes(byte1: bytes, byte2: bytes) -> bytearray:
    ba = bytearray()
    for x,y in zip(byte1, byte2):
        ba.append(x^y)
    return ba

import hashlib
def xorUtf8Md5(string1:str, string2:str) -> str:
    m1 = hashlib.md5()
    m1.update(string1.encode("utf-8"))
    byte1 = m1.digest()
    m2 = hashlib.md5()
    m2.update(string2.encode("utf-8"))
    byte2 = m2.digest()
    byte3 = xorBytes(byte1, byte2)
    byte3hex = "".join([format(b, "02x") for b in byte3])

    hex1 = "".join([format(b, "02x") for b in byte1])
    hex2 = "".join([format(b, "02x") for b in byte2])
    hex3 = xorHexStrings(hex1, hex2)

    assert(byte3hex == hex3)
    return byte3hex

def xorUtf8Sha1(string1: str, string2: str) -> str:
    m1 = hashlib.sha1()
    m1.update(string1.encode("utf-8"))
    byte1 = m1.digest()
    m2 = hashlib.sha1()
    m2.update(string2.encode("utf-8"))
    byte2 = m2.digest()
    byte3 = xorBytes(byte1, byte2)
    byte3hex = "".join([format(b, "02x") for b in byte3])

    hex1 = "".join([format(b, "02x") for b in byte1])
    hex2 = "".join([format(b, "02x") for b in byte2])
    hex3 = xorHexStrings(hex1, hex2)

    assert(byte3hex == hex3)
    return byte3hex

if __name__ == "__main__":
    print(xorUtf8Md5("hello", "world"))
    print(xorUtf8Sha1("hello", "world"))

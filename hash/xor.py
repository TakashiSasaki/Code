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

def xorBytes(bytes1 : bytes, bytes2: bytes) -> bytes:
    return b"".join([(x^y).to_bytes(1, "big") for x,y in zip(bytes1, bytes2)])

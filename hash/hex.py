def bytesToHex(bytes1: bytes) -> str:
    return "".join([format(b, "02x") for b in bytes1])

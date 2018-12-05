import pathlib, re, socket

def osPathToUrl2(osPath):
    osPath = re.sub("/+", "/", osPath)
    osPath = re.sub("\\\\+", "\\\\", osPath)
    hostname = socket.gethostname()
    hostname = hostname.lower()
    purePath = pathlib.PurePath(osPath)
    if purePath.is_absolute() == False:
        purePath = pathlib.PurePosixPath(osPath)
    assert purePath.is_absolute
    url = purePath.as_uri()
    return "file://" + hostname + url[7:]
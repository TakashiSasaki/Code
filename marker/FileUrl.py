import os, re, urllib, pathlib, socket

class FileUrl(object):
    __slots__=["netloc", "path"]

    def __init__(self, fileUrl=None):
        if fileUrl is None:
            self.netloc = ""
            self.path = ""
            return
        parseResult = urllib.parse.urlparse(fileUrl)
        assert parseResult.scheme == "file"
        self.netloc = parseResult.netloc
        self.path = parseResult.path

    def fromOsPath(self, osPath):
        fileUrl1 = osPathToUrl1(osPath)
        fileUrl2 = osPathToUrl2(osPath)
        assert fileUrl1 == fileUrl2
        self.__init__(fileUrl1)
    
def splitAll(s):
    components = []
    drive, path = os.path.splitdrive(s)
    head = path
    tail = None
    while True:
        head, tail = os.path.split(head)
        if tail == "" and head == "": break
        if tail == "" and head == "/": break
        if tail == "/" and head == "": break
        if tail == "" and head == "\\": break
        if tail == "\\" and head == "": break
        if tail != "": components.append(tail)
    if isinstance(drive, str) and len(drive) >0:
        components.append(drive.lower())
    components.reverse()
    return components

def osPathToUrl1(osPath):
    osPath = re.sub("/+", "/", osPath)
    osPath = re.sub("\\\\+", "\\\\", osPath)
    hostname = socket.gethostname()
    hostname = hostname.lower()
    splitPath = splitAll(osPath)
    joinedPath = "/".join(splitPath)
    return "file://" + hostname + "/" + joinedPath

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

if __name__ == "__main__":
    x = urllib.parse.urlparse("file://a/b/c/d")
    print(x)
    pass
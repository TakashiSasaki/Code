import os, re, urllib, pathlib, socket
from .Uri import Uri

hostname = socket.gethostname()
hostname = hostname.lower()

class FileUrl(Uri):

    def __init__(self, fileUrlOrPath=None):
        if fileUrlOrPath is None:
            self.netloc = ""
            self.path = ""
            return

        parseResult = urllib.parse.urlparse(fileUrlOrPath)
        if parseResult.scheme == "file":
            self.netloc = parseResult.netloc
            self.path = parseResult.path
            return

        fileUrl1 = osPathToUrl1(fileUrlOrPath)
        fileUrl2 = osPathToUrl2(fileUrlOrPath)
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
    splitPath = splitAll(osPath)
    joinedPath = "/".join(splitPath)
    return "file://" + hostname + "/" + joinedPath

def osPathToUrl2(osPath):
    osPath = re.sub("/+", "/", osPath)
    osPath = re.sub("\\\\+", "\\\\", osPath)
    purePath = pathlib.PurePath(osPath)
    if purePath.is_absolute() == False:
        purePath = pathlib.PurePosixPath(osPath)
    assert purePath.is_absolute
    url = purePath.as_uri()
    return "file://" + hostname + url[7:]

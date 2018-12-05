import os, re, urllib, pathlib, socket

class FileUrl(object):
    def __init__(self, fileUrl):
        self.fileUrl = fileUrl
    
    def fromOsPath(self, osPath):
        fileUrl1 = osPathToUrl1(osPath)
        fileUrl2 = osPathToUrl2(osPath)
        assert fileUrl1 == fileUrl2
        self.fileUrl = fileUrl1
    
def splitAll(s):
    components = []
    drive, path = os.path.splitdrive(s)
    if isinstance(drive, str) and len(drive) >0:
        components.append(drive.lower())
    head = s
    tail = None
    while True:
        head, tail = os.path.split(head)
        if tail == "" and head == "": break
        if tail == "" and head == "/": break
        if tail == "/" and head == "": break
        if tail == "" and head == "\\": break
        if tail == "\\" and head == "": break
        if tail != "": components.append(tail)
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

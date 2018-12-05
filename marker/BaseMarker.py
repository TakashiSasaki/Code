import dns.resolver
import logging
import urllib
import os.path
import socket, re

class BaseMarker(object):
    magic = b"c39bf83a4d185b0c2a1c2d0a069d37ae6c0cbc44"
    pass

def getDnsTxts(fqdn):
    answer = dns.resolver.query(fqdn, "TXT")
    answer0 = answer.response.answer[0]
    item = answer0.items[0]
    strings = item.strings
    return strings

def checkDnsMagic():
    strings = getDnsTxts("magic.moukaeritai.work")
    if len(strings) != 1:
         logging.warning("Failed to get TXT record of magic.moukaeritai.work.")
    if strings[0] != BaseMarker.magic:
         logging.warning("Magic number does not match with magic.moukaeritai.work.")

def osPathToUrl(osPath):
    osPath = re.sub("/+", "/", osPath)
    osPath = re.sub("\\\\+", "\\\\", osPath)
    hostname = socket.gethostname()
    hostname = hostname.lower()
    #absolutePath = os.path.abspath(osPath)
    components = [""]
    drive, path = os.path.splitdrive(osPath)
    if isinstance(drive, str) and len(drive) >0:
        components.append(drive.lower())
    splitPath = os.path.split(path)
    if len(splitPath) == 0:
        components.append(splitPath[0])
    else:
        headDir = splitPath[0]
        tailDir = splitPath[1:]
        if len(headDir) == 0: pass
        elif headDir == "\\": pass
        elif headDir[0] == "\\":
            components.append(headDir[1:])
        elif headDir[0] == "/":
            components.append(headDir[1:])
    components += tailDir
    joinedPath = "/".join(components)
    return joinedPath

def urlToOsPath(url):
    pass

if __name__ == "__main__":
    checkDnsMagic()    
    print(urllib.parse.urlsplit("file://surfacepro5/c:/a/b/c"))
    absolutePath = os.path.abspath(".")
    print(absolutePath)
    print(os.path.normpath(os.path.abspath(".")))
    assert os.path.sep == "\\"
    assert os.path.altsep == "/"
    assert os.path.pathsep == ";"
    #splitPath = os.path.split(absolutePath)
    #print(os.path.splitdrive(absolutePath))
    print(osPathToUrl(absolutePath))
    print (osPathToUrl("."))
    #print(os.path.curdir)
    #print(os.path.splitdrive("/abc/def"))
    print(osPathToUrl("/abc/def"))
    path1 = "///a//b////c"
    print(re.sub("/+","/", path1))
    path2 = "\\\\\\a\\\\\\\\b\\\\\\\\c\\d"
    print(re.sub("\\\\+", "\\\\", path2))
    print(osPathToUrl(path1))

import re, socket, os.path

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

def osPathToUrl(osPath):
    osPath = re.sub("/+", "/", osPath)
    osPath = re.sub("\\\\+", "\\\\", osPath)
    hostname = socket.gethostname()
    hostname = hostname.lower()
    splitPath = splitAll(osPath)
    joinedPath = "/".join(splitPath)
    return "file://" + hostname + "/" + joinedPath

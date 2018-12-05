import re, socket, os.path

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

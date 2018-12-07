import marker.BaseMarker
import os
import os.path
from .FileUrl import FileUrl

class FileMarker(marker.BaseMarker.BaseMarker):
    def __init__(self, filePath):
        self.writable = False
        if not os.path.isabs(filePath):
            raise RuntimeError(filePath + " is not absolute path")
        if os.path.isdir(filePath):
            self.directory = filePath
            self.file = None
            return
        if os.path.isfile(filePath):
            self.file = filePath
            head, tail = os.path.split(filePath)
            parent = os.path.join(head)

    
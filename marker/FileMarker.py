from .Marker import Marker
import os
import os.path
from .FileUrl import FileUrl

class FileMarker(Marker):
    def __init__(self):
        pass

    def fromPath(self, path):
        assert(os.path.isabs(path))
        if os.path.isdir(path):
            self.directory = path
            self.file = None
            return
        if os.path.isfile(path):
            self.file = path
            head, tail = os.path.split(path)
            self.directory = os.path.join(head)

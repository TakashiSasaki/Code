import  urllib.parse
from dataclasses import dataclass

@dataclass
class Uri:
    scheme : str = ""
    netloc : str = ""
    path : str = ""
    params: str = ""
    query : str = ""
    fragment : str = ""

    def __init__(self, s:str=None):
        if s is not None:
            self.fromString(s)

    def fromString(self, s:str):
        parseResult = urllib.parse.urlparse(s)
        self.scheme = parseResult.scheme
        self.netloc = parseResult.netloc
        self.path = parseResult.path
        self.params = parseResult.params
        self.query = parseResult.query
        self.fragment = parseResult.fragment

    def __str__(self):
        parseResult = urllib.parse.ParseResult(self.scheme, self.netloc, self.path, self.params, self.query, self.fragment)
        s = urllib.parse.urlunparse(parseResult)
        return s

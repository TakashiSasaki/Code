import  urllib.parse
from dataclasses import dataclass

@dataclass
class Uri:
    scheme : str
    netloc : str
    path : str
    params: str
    query : str
    fragment : str

    def fromString(self, s:str):
        parsedUrl = urllib.parse.urlparse(s)
        self.scheme = parsedUrl.scheme
        self.netloc = parsedUrl.netloc
        self.path = parsedUrl.path
        self.params = parsedUrl.params
        self.query = parsedUrl.query
        self.fragment = parsedUrl.fragment

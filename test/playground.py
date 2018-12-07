import urllib.parse, unittest

URLS = [
    "http://example.com/a/b/c?a=b&c=d",
    "uri:abcdef:xyz",
    "file://hostname/d1/d2/d3",
    "tag:john@example.com/abc"
]

class Playground(unittest.TestCase):
    def setUp(self):
        pass

    def test(self):
        for x in URLS:
            a = x
            b = urllib.parse.urlparse(a)
            c = urllib.parse.urlunparse(b)
            self.assertEqual(a,c)

import urllib.parse, unittest

URLS = [
    "http://example.com/a/b/c?a=b&c=d",
    "uri:abcdef:xyz",
    "file://my.windows.pc/d1/d2/d3",
    "file://SurfacePro4/d1/d2/d3",
    "tag:john@example.com/abc",
    "file:///c:/d/e/f;a=b,c?X=Y&x=y#111",
    "http://www.mysite.com/admin/UpdateUserServlet;/user/HomeServlet",
    "scheme://netloc/path;parameters?query#fragment"
]

class Playground(unittest.TestCase):
    def setUp(self):
        pass

    def test(self):
        for x in URLS:
            a = x
            b = urllib.parse.urlparse(a)
            self.assertEqual(b._fields, ('scheme', 'netloc', 'path', 'params', 'query', 'fragment'))
            c = urllib.parse.urlunparse(b)
            self.assertEqual(a,c)
            print(urllib.parse.urlsplit(a))

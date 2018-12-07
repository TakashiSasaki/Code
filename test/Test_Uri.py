from marker.Uri import Uri
from unittest import TestCase
from urllib.parse import urlparse, urlunparse

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


class Test_Uri(TestCase):
    def setUp(self):
        pass

    def test(self):
        for x in URLS:
            a = x
            b = urlparse(a)
            self.assertEqual(b._fields, ('scheme', 'netloc', 'path', 'params', 'query', 'fragment'))
            c = urlunparse(b)
            self.assertEqual(a,c)

    def test_fromString(self):
        for x in URLS:
            uri = Uri()
            uri.fromString(x)
            s = str(uri)
            self.assertEqual(s, x)

    def test_init(self):
        for x in URLS:
            uri = Uri(x)
            s = str(uri)
            self.assertEqual(s, x)
    
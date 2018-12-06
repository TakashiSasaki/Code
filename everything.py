import socket
import http.client
import urllib.parse
import json

class Everything():
    def __init__(self, ipAddress, port):
        Everything.hostname = socket.gethostname()
        if ipAddress is None:
            for i in range(1, 256):
                print(i)
                httpConnection = http.client.HTTPConnection(
                    "127.0.0." + str(i), timeout=1)
                try:
                    httpConnection.request("GET", "/")
                    response = httpConnection.getresponse()
                    if response.headers["Server"] == "Everything HTTP Server":
                        self.ipAddress = "127.0.0." + str(i)
                        self.port = 80
                        httpConnection.close()
                        break
                    httpConnection.close()
                except Exception as e:
                    pass
        else:
            self.ipAddress = ipAddress
        if port is None:
            self.port = 80
        else:
            self.port = port

    def query(self, queryString):
        httpConnection = http.client.HTTPConnection(
            self.ipAddress, port=self.port, timeout=2)
        httpConnection.request("GET", "/?" + urllib.parse.urlencode({
            "j": 1,
            "q": queryString,
            "path": 1,
            "size": 1,
            "date_modified_column": 1,
            "date_created_column": 1,
            "attributes_column": 1
        }))
        jsonString = httpConnection.getresponse()
        o = json.load(jsonString)
        return o


if __name__ == "__main__":
    e = Everything("127.0.0.3", 80)
    o = e.query("Document")
    print(o)

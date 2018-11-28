print("hello world from hello.py")

import http.server

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/hello.py":
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("world".encode("utf-8"))
            return
        http.server.SimpleHTTPRequestHandler.do_GET(self)
        return
    pass

httpServer = http.server.HTTPServer(("", 8000), MyHandler)
httpServer.serve_forever()
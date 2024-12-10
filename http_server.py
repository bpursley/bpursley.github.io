#http_server.py

import http.server
import socketserver

PORT = 8080
DIRECTORY = "html-files"

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/bapursley.net':
            self.path = '/bapursley.html'
          
        elif self.path == '/bpursley.net"
            self.path = '/bpursley.html'

        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def translate_path(self, path):
        return f"./{DIRECTORY}/{path}"

handler_object = MyHttpRequestHandler
my_server = socketserver.TCPServer(("0.0.0.0", PORT), handler_object)

print(f"Serving HTTP on port {PORT}")
my_server.serve_forever()



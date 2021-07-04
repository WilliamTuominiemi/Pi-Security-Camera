# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import time

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        print('request received')
        self.wfile.write(
            bytes(json.dumps({'received': 'ok'}, ensure_ascii=False), 'utf-8'))
        # self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}))
        # if self.path == '/left':
        #     print('left')
        # elif self.path == '/right':
        #     print('right')


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

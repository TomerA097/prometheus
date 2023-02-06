import http.server
from prometheus_client import start_http_server


class HandleRequests(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
        self.wfile.close()


if __name__ == "__main__":
    start_http_server(5001)
    server = http.server.HTTPServer(('localhost', 5000), HandleRequests)
    server.serve_forever()

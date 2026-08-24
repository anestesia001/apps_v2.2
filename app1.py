from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"Hello from my Docker image!\n"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


port = int(os.getenv("PORT", "8080"))
server = HTTPServer(("0.0.0.0", port), Handler)
print(f"Server started on port {port}")
server.serve_forever()

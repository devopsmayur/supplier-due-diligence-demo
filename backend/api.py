"""Local demonstration API; uses only Python's standard library."""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from backend.service import evaluate_supplier, deletion_eligibility


class Handler(BaseHTTPRequestHandler):
    def respond(self, status, payload):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            self.respond(200, {"status": "ok"})
        else:
            self.respond(404, {"error": "unknown endpoint"})

    def do_POST(self):
        routes = {"/suppliers/evaluate": evaluate_supplier,
                  "/records/deletion-eligibility": deletion_eligibility}
        if self.path not in routes:
            self.respond(404, {"error": "unknown endpoint"})
            return
        try:
            size = int(self.headers.get("Content-Length", "0"))
            if not 0 < size <= 16384:
                raise ValueError("request size must be 1–16384 bytes")
            payload = json.loads(self.rfile.read(size))
            if not isinstance(payload, dict):
                raise ValueError("request must be an object")
            result = routes[self.path](payload)
        except (ValueError, TypeError, KeyError, OverflowError):
            self.respond(400, {"error": "invalid request"})
            return
        self.respond(200, result)


if __name__ == "__main__":
    print("Demo API: http://127.0.0.1:8000", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()

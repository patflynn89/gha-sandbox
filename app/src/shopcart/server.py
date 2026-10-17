"""Minimal HTTP server (stdlib only) so the Docker image stays tiny.

GET /health  -> {"status": "ok"}
GET /version -> {"version": "<APP_VERSION env var>"}
"""

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def _send(self, code: int, body: dict) -> None:
        payload = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self) -> None:
        if self.path == "/health":
            self._send(200, {"status": "ok"})
        elif self.path == "/version":
            self._send(200, {"version": os.environ.get("APP_VERSION", "dev")})
        else:
            self._send(404, {"error": "not found"})


def main() -> None:
    port = int(os.environ.get("PORT", "8080"))
    print(f"listening on :{port}")
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()


if __name__ == "__main__":
    main()

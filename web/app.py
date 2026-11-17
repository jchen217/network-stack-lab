import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

from redis import Redis
from redis.exceptions import RedisError

BANNER = Path(__file__).with_name("banner.txt").read_text(encoding="utf-8").strip()
COUNTER = Redis(
    host=os.environ.get("REDIS_HOST", "redis"),
    port=6379,
    socket_connect_timeout=1,
    socket_timeout=1,
)


class CounterHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if urlsplit(self.path).path != "/":
            self.respond(404, "Not found\n")
            return

        try:
            visits = COUNTER.incr("visits")
        except RedisError as error:
            self.log_error("Redis request failed: %s", error)
            self.respond(503, "Redis unavailable\n")
            return

        self.respond(200, f"{BANNER}\nVisits: {visits}\n")

    def respond(self, status, message):
        body = message.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    with ThreadingHTTPServer(("0.0.0.0", 8000), CounterHandler) as server:
        server.serve_forever()

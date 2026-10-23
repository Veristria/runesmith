"""J10-F (issue #7): the whole failover path through the real stdlib HTTP transport.

The router's "429" failover is already covered with injected fake transports
(``tests/test_free_key_pacing.py``, ``tests/test_router_fallthrough.py``).
This file adds what those cannot: a real ``http.server`` socket, the real
``urllib`` transport in ``runesmith.instruments.http_json``, a real HTTP 429
response with a ``Retry-After`` header, and the real ``PACING.json`` written
under ``<home>``. Only the standard library is used, servers bind 127.0.0.1
only, and no ``time.sleep`` appears: the point is the code path, not waiting.
"""

import json
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from runesmith.config import build_router
from runesmith.instruments import TransportCensored

GROQ_RATE_LIMIT = {
    "error": {
        "message": "Rate limit reached for model on tokens per minute (TPM): "
        "Limit 6000, Used 100. Please try again in 30s.",
        "code": "rate_limit_exceeded",
    }
}


def completion(content):
    return {"choices": [{"message": {"content": content}, "finish_reason": "stop"}]}


class _CountingHandler(BaseHTTPRequestHandler):
    requests = 0

    def do_POST(self):  # noqa: N802 - the stdlib calls this
        length = int(self.headers.get("Content-Length") or 0)
        self.rfile.read(length)
        type(self).requests += 1
        self.respond()

    def respond(self):  # overridden per server kind
        raise NotImplementedError

    def log_message(self, *args):  # keep the test output quiet
        pass


def _server(handler_class):
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), handler_class)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    return httpd


class _Limited(_CountingHandler):
    def respond(self):
        body = json.dumps(GROQ_RATE_LIMIT).encode("utf-8")
        self.send_response(429)
        self.send_header("Retry-After", "30")
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


class _Answering(_CountingHandler):
    def respond(self):
        body = json.dumps(completion('{"ok": true}')).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def _config(first_url, second_url):
    return {
        "instruments": {
            "first": {"kind": "openai", "model": "m1", "base_url": first_url, "timeout_s": 5},
            "second": {"kind": "openai", "model": "m2", "base_url": second_url, "timeout_s": 5},
        },
        "roles": {"plan": ["first", "second"]},
    }


def _call(router):
    return router.call("plan", prompt="say ok", system="answer with one JSON object",
                       schema=None, max_tokens=100, key="k")


class FailoverLocalHTTP(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.home = self._tmp.name

        _Limited.requests = 0
        _Answering.requests = 0
        self.a = _server(_Limited)
        self.b = _server(_Answering)
        self.addCleanup(self.a.shutdown)
        self.addCleanup(self.b.shutdown)

        def base(httpd, path):
            return f"http://127.0.0.1:{httpd.server_address[1]}{path}"

        self.router = build_router(
            _config(base(self.a, "/v1"), base(self.b, "/v1")),
            home=self.home,
            backoff_s=(),
        )

    def test_429_moves_to_the_next_instrument_and_holds_the_first(self):
        outcome = _call(self.router)
        self.assertTrue(outcome.ok, outcome.error)
        self.assertEqual(outcome.receipt["instrument"], "second")
        self.assertEqual(_Limited.requests, 1)
        self.assertEqual(_Answering.requests, 1)

        # The second call goes straight to B: "first" is held until its reset.
        outcome = _call(self.router)
        self.assertTrue(outcome.ok, outcome.error)
        self.assertEqual(outcome.receipt["instrument"], "second")
        self.assertEqual(_Limited.requests, 1)
        self.assertEqual(_Answering.requests, 2)

        # The limit was remembered with roughly the announced Retry-After window.
        with open(f"{self.home}/PACING.json", encoding="utf-8") as file:
            limits = json.load(file)
        entry = limits["first"]
        self.assertIn("until", entry)
        self.assertAlmostEqual(entry["until"], entry["since"] + 30, delta=1.0)

    def test_every_instrument_at_its_limit_names_them_all(self):
        _Limited.requests = 0
        first = _server(_Limited)
        second = _server(_Limited)
        self.addCleanup(first.shutdown)
        self.addCleanup(second.shutdown)

        def base(httpd, path):
            return f"http://127.0.0.1:{httpd.server_address[1]}{path}"

        router = build_router(
            _config(base(first, "/v1"), base(second, "/v1")),
            home=self.home,
            backoff_s=(),
        )
        with self.assertRaises(TransportCensored) as caught:
            _call(router)
        plain = caught.exception.plain or ""
        self.assertIn("first", plain)
        self.assertIn("second", plain)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

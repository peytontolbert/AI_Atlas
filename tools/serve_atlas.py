#!/usr/bin/env python3
"""Serve the built AI Dependency Atlas viewer on localhost."""
from __future__ import annotations

import argparse
import errno
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class AtlasRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def redirect_to_viewer(self) -> bool:
        if self.path not in {"/", ""}:
            return False
        self.send_response(302)
        self.send_header("Location", "/dist/ai_dependency_atlas_v2.html")
        self.end_headers()
        return True

    def do_GET(self) -> None:
        if not self.redirect_to_viewer():
            super().do_GET()

    def do_HEAD(self) -> None:
        if not self.redirect_to_viewer():
            super().do_HEAD()


def parse_args() -> argparse.Namespace:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8088)
    parser.add_argument("--root", type=Path, default=root)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = args.root.resolve()
    html = root / "dist" / "ai_dependency_atlas_v2.html"
    if not html.is_file():
        raise SystemExit(f"Built viewer not found: {html}\nRun `make build` first.")

    handler = partial(AtlasRequestHandler, directory=str(root))
    try:
        server = ThreadingHTTPServer((args.host, args.port), handler)
    except OSError as exc:
        if exc.errno == errno.EADDRINUSE:
            raise SystemExit(
                f"Port {args.port} is already in use on {args.host}. "
                f"Stop the other server or run `make serve PORT={args.port + 1}`."
            ) from exc
        raise
    url = f"http://{args.host}:{args.port}/"
    print(f"Serving AI Dependency Atlas at {url}")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()

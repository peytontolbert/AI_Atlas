#!/usr/bin/env python3
"""Browser smoke test for the generated standalone atlas.

Requires Playwright and an installed Chromium browser. The test injects the
standalone HTML with page.set_content, so it does not need a local web server.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from playwright.sync_api import sync_playwright


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--html", type=Path, default=root / "dist" / "ai_dependency_atlas_v2.html"
    )
    parser.add_argument(
        "--screenshot",
        type=Path,
        default=root / "dist" / "ai_dependency_atlas_v2_preview.png",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=root / "dist" / "browser_smoke_report.json",
    )
    parser.add_argument("--chromium-executable", type=Path)
    args = parser.parse_args()

    errors: list[str] = []
    console: list[str] = []
    html = args.html.read_text(encoding="utf-8")

    with sync_playwright() as playwright:
        launch_kwargs = {
            "headless": True,
            "args": ["--no-sandbox", "--disable-dev-shm-usage"],
        }
        if args.chromium_executable:
            launch_kwargs["executable_path"] = str(args.chromium_executable)
        browser = playwright.chromium.launch(**launch_kwargs)
        page = browser.new_page(viewport={"width": 1800, "height": 1100})
        page.on("pageerror", lambda exc: errors.append(f"pageerror: {exc}"))
        page.on(
            "console",
            lambda message: console.append(f"{message.type}: {message.text}")
            if message.type in {"error", "warning"}
            else None,
        )
        page.set_content(html, wait_until="load")
        page.wait_for_selector(".node")

        initial = page.evaluate(
            """() => ({
              title: document.querySelector('#title').textContent,
              node_count: document.querySelectorAll('.node').length,
              layer_count: document.querySelectorAll('.layer').length,
              status: document.querySelector('#status-pill').textContent,
            })"""
        )

        page.click('button[data-id="transformer"]')
        page.wait_for_timeout(350)
        explore = page.evaluate(
            """() => ({
              selected: document.querySelectorAll('.node.selected').length,
              ancestors: document.querySelectorAll('.node.ancestor').length,
              descendants: document.querySelectorAll('.node.descendant').length,
              paths: document.querySelectorAll('#edge-layer path').length,
              inspector_title: document.querySelector('#inspector h2')?.textContent,
            })"""
        )
        args.screenshot.parent.mkdir(parents=True, exist_ok=True)
        page.screenshot(path=str(args.screenshot), full_page=False)

        page.click('button[data-kind="compare"]')
        page.wait_for_timeout(250)
        compare = page.evaluate(
            """() => ({
              a: document.querySelectorAll('.node.sel-a').length,
              b: document.querySelectorAll('.node.sel-b').length,
              shared: document.querySelectorAll('.node.shared').length,
              inspector_title: document.querySelector('#inspector h2')?.textContent,
            })"""
        )

        page.click("#scope-btn")
        page.wait_for_selector("#scope-modal.open")
        scope_text = page.locator("#scope-body").inner_text().lower()
        page.click("#scope-close")

        page.fill("#search", "GRPO")
        page.wait_for_timeout(120)
        search_hits = page.locator(".node.search-hit").count()
        browser.close()

    assertions = {
        "expected_node_count": initial["node_count"] == 320,
        "expected_layer_count": initial["layer_count"] == 12,
        "explore_selection": explore["selected"] == 1,
        "explore_edges_rendered": explore["paths"] > 0,
        "compare_selection": compare["a"] == 1 and compare["b"] == 1,
        "compare_shared_substrate": compare["shared"] > 0,
        "scope_discloses_non_exhaustive": "not exhaustive" in scope_text,
        "scope_discloses_editorial_provenance": "graph-derived" in scope_text,
        "search_returns_results": search_hits > 0,
        "no_page_errors": not errors,
        "no_console_errors": not any(item.startswith("error:") for item in console),
    }
    report = {
        "passed": all(assertions.values()),
        "initial": initial,
        "explore": explore,
        "compare": compare,
        "search_hits": search_hits,
        "assertions": assertions,
        "console": console,
        "errors": errors,
        "screenshot": str(args.screenshot),
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

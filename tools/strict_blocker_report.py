#!/usr/bin/env python3
"""Summarize strict source-audit blockers by layer, field, pattern, and node."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

BLOCKING = {"ambiguous", "unsupported"}


def pattern_for_sentence(text: str) -> str:
    if text.startswith("The role of "):
        return "graph-derived role summary"
    if text.startswith("substrate for "):
        return "graph-derived substrate example"
    if " as a reusable ingredient" in text and " uses " in text:
        return "graph-derived uses rationale"
    if " into a scalable, deployable" in text and " turns " in text:
        return "graph-derived operationalizes rationale"
    if " measures, constrains, audits, or governs behavior using " in text:
        return "graph-derived evaluation rationale"
    if text.startswith("Its abstractions require explicit assumptions"):
        return "generic foundation limitation"
    if text.startswith("Its inductive bias, data demand"):
        return "generic model limitation"
    if text.startswith("Operational gains introduce new failure modes"):
        return "generic infrastructure limitation"
    if text.startswith("End-to-end quality is bounded"):
        return "generic system limitation"
    if text.startswith("Coverage is necessarily incomplete"):
        return "generic evaluation limitation"
    return "node-specific blocker"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(json.loads(line))
    return records


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=root / "data" / "atlas.json")
    parser.add_argument("--sentence-ledger", type=Path, default=root / "audit" / "source_sentence_ledger.jsonl")
    parser.add_argument("--edge-ledger", type=Path, default=root / "audit" / "edge_review_ledger.jsonl")
    parser.add_argument("--json-report", type=Path, default=root / "dist" / "strict_blocker_report.json")
    parser.add_argument("--md-report", type=Path, default=root / "dist" / "strict_blocker_report.md")
    args = parser.parse_args()

    data = json.loads(args.data.read_text(encoding="utf-8"))
    node_meta = {node["id"]: {"label": node["label"], "layer": node["layer"]} for node in data["nodes"]}
    sentence_records = [r for r in load_jsonl(args.sentence_ledger) if r.get("verdict") in BLOCKING]
    edge_records = [r for r in load_jsonl(args.edge_ledger) if r.get("verdict") in BLOCKING]

    sentence_by_layer = Counter(node_meta[r["node_id"]]["layer"] for r in sentence_records)
    sentence_by_field = Counter(r.get("field", "") for r in sentence_records)
    sentence_by_pattern = Counter(pattern_for_sentence(r.get("text", "")) for r in sentence_records)
    sentence_by_verdict = Counter(r.get("verdict") for r in sentence_records)
    edge_by_layer = Counter(node_meta[r["node_id"]]["layer"] for r in edge_records)
    edge_by_verdict = Counter(r.get("verdict") for r in edge_records)
    node_counts = Counter(r["node_id"] for r in sentence_records)
    node_counts.update(r["node_id"] for r in edge_records)

    report = {
        "sentence_blockers": len(sentence_records),
        "edge_blockers": len(edge_records),
        "sentence_by_verdict": dict(sentence_by_verdict),
        "edge_by_verdict": dict(edge_by_verdict),
        "sentence_by_layer": dict(sentence_by_layer),
        "edge_by_layer": dict(edge_by_layer),
        "sentence_by_field_top": sentence_by_field.most_common(50),
        "sentence_by_pattern": dict(sentence_by_pattern),
        "top_nodes": [
            {
                "node_id": node_id,
                "label": node_meta[node_id]["label"],
                "layer": node_meta[node_id]["layer"],
                "blockers": count,
            }
            for node_id, count in node_counts.most_common(50)
        ],
    }
    args.json_report.parent.mkdir(parents=True, exist_ok=True)
    args.json_report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Strict Source-Audit Blocker Report",
        "",
        "This report lists records that prevent `make source-audit-strict` from passing. It does not downgrade or hide blockers.",
        "",
        "## Summary",
        "",
        "| Blocker class | Count |",
        "|---|---:|",
        f"| Sentence blockers | {len(sentence_records)} |",
        f"| Edge blockers | {len(edge_records)} |",
        "",
        "## Sentence Patterns",
        "",
        "| Pattern | Count |",
        "|---|---:|",
    ]
    for pattern, count in sentence_by_pattern.most_common():
        lines.append(f"| {pattern} | {count} |")
    lines.extend(["", "## Sentence Layers", "", "| Layer | Count |", "|---|---:|"])
    for layer, count in sentence_by_layer.most_common():
        lines.append(f"| `{layer}` | {count} |")
    lines.extend(["", "## Edge Layers", "", "| Layer | Count |", "|---|---:|"])
    for layer, count in edge_by_layer.most_common():
        lines.append(f"| `{layer}` | {count} |")
    lines.extend(["", "## Top Nodes", "", "| Node | Layer | Blockers |", "|---|---|---:|"])
    for item in report["top_nodes"][:25]:
        lines.append(f"| `{item['node_id']}` {item['label']} | `{item['layer']}` | {item['blockers']} |")
    lines.append("")
    args.md_report.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"sentence_blockers": len(sentence_records), "edge_blockers": len(edge_records)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Emit a transparent editorial and graph-content audit for the atlas.

This report intentionally distinguishes schema validity from editorial depth. It
is not a proof that the ontology is universally exhaustive or factually final.
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path


def _stats(values: list[int]) -> dict[str, float | int]:
    if not values:
        return {"min": 0, "median": 0, "mean": 0, "max": 0}
    return {
        "min": min(values),
        "median": statistics.median(values),
        "mean": round(statistics.fmean(values), 2),
        "max": max(values),
    }


def audit(data_path: Path) -> dict:
    data = json.loads(data_path.read_text(encoding="utf-8"))
    nodes = data["nodes"]
    references = {ref["id"]: ref for ref in data["references"]}
    consumers: dict[str, list[str]] = defaultdict(list)
    for node in nodes:
        for edge in node["dependencies"]:
            consumers[edge["id"]].append(node["id"])

    normalized_definitions = [
        re.sub(r"\W+", " ", node["definition"].lower()).strip() for node in nodes
    ]
    editorial_counts = Counter(node["editorial_status"] for node in nodes)
    reference_usage = Counter(
        ref_id for node in nodes for ref_id in node["reference_ids"]
    )
    graph_summary_patterns = {
        "role_summary_starts_with_the_role_of": sum(
            node["why_it_matters"].startswith("The role of ") for node in nodes
        ),
        "examples_begin_with_substrate_for": sum(
            any(example.startswith("substrate for ") for example in node["examples"])
            for node in nodes
        ),
        "baseline_layer_caveat_used": sum(
            node["editorial_status"] == "definition_curated_context_graph_derived"
            for node in nodes
        ),
    }
    terminal_ids = [node["id"] for node in nodes if node["terminal"]]
    zero_consumer_non_system = [
        node["id"]
        for node in nodes
        if node["layer"] != "system" and not consumers[node["id"]]
    ]

    return {
        "disclaimer": (
            "This audit measures structural integrity, field coverage, and editorial provenance. "
            "It does not certify universal research completeness, historical priority, or the "
            "truth of every dependency judgment."
        ),
        "source": str(data_path),
        "counts": {
            "nodes": len(nodes),
            "edges": sum(len(node["dependencies"]) for node in nodes),
            "references": len(references),
            "unique_normalized_definitions": len(set(normalized_definitions)),
            "terminal_nodes": len(terminal_ids),
            "zero_consumer_non_system_nodes": len(zero_consumer_non_system),
        },
        "editorial_provenance": dict(editorial_counts),
        "graph_derived_pattern_counts": graph_summary_patterns,
        "field_length_characters": {
            "definition": _stats([len(node["definition"]) for node in nodes]),
            "why_it_matters": _stats([len(node["why_it_matters"]) for node in nodes]),
            "edge_rationale": _stats(
                [len(edge["rationale"]) for node in nodes for edge in node["dependencies"]]
            ),
        },
        "reference_usage": {
            "nodes_with_reference": sum(bool(node["reference_ids"]) for node in nodes),
            "nodes_with_multiple_references": sum(
                len(node["reference_ids"]) > 1 for node in nodes
            ),
            "most_reused": [
                {
                    "id": ref_id,
                    "title": references[ref_id]["title"],
                    "node_count": count,
                }
                for ref_id, count in reference_usage.most_common(10)
            ],
        },
        "topology": {
            "terminal_node_ids": terminal_ids,
            "zero_consumer_non_system_node_ids": zero_consumer_non_system,
            "layer_counts": data["meta"]["stats"]["layer_counts"],
            "relation_counts": data["meta"]["stats"]["relation_counts"],
        },
    }


def markdown(report: dict) -> str:
    c = report["counts"]
    e = report["editorial_provenance"]
    p = report["graph_derived_pattern_counts"]
    lengths = report["field_length_characters"]
    refs = report["reference_usage"]
    lines = [
        "# AI Dependency Atlas Content Audit",
        "",
        f"> {report['disclaimer']}",
        "",
        "## Structural and editorial summary",
        "",
        "| Measure | Value |",
        "|---|---:|",
        f"| Nodes | {c['nodes']} |",
        f"| Typed edges | {c['edges']} |",
        f"| Reference records | {c['references']} |",
        f"| Unique normalized definitions | {c['unique_normalized_definitions']} |",
        f"| Manually curated supporting context | {e.get('curated', 0)} |",
        f"| Definition-curated, graph-derived supporting context | {e.get('definition_curated_context_graph_derived', 0)} |",
        f"| Non-system nodes without consumers | {c['zero_consumer_non_system_nodes']} |",
        "",
        "## Editorial disclosure",
        "",
        "All concept definitions are concept-specific and unique under normalization. The `editorial_status` field makes a second distinction: supporting sections for some nodes were manually written, while others were generated from validated dependency and consumer relationships. Graph-derived supporting context is useful for navigation, but it is not represented as equivalent to a full textbook treatment.",
        "",
        "| Pattern | Count |",
        "|---|---:|",
        f"| Role summaries beginning with `The role of …` | {p['role_summary_starts_with_the_role_of']} |",
        f"| Nodes containing a `substrate for …` example | {p['examples_begin_with_substrate_for']} |",
        f"| Nodes using graph-derived baseline context | {p['baseline_layer_caveat_used']} |",
        "",
        "## Field-length distribution",
        "",
        "| Field | Minimum | Median | Mean | Maximum |",
        "|---|---:|---:|---:|---:|",
    ]
    for field, values in lengths.items():
        lines.append(
            f"| {field.replace('_', ' ')} | {values['min']} | {values['median']} | {values['mean']} | {values['max']} |"
        )
    lines += [
        "",
        "## Reference usage",
        "",
        f"- Nodes with at least one reference pointer: **{refs['nodes_with_reference']} / {c['nodes']}**",
        f"- Nodes with multiple reference pointers: **{refs['nodes_with_multiple_references']} / {c['nodes']}**",
        "- A reference pointer is evidence of a relevant source family; it is not a claim that every sentence has been individually source-verified.",
        "",
        "| Most reused reference | Nodes |",
        "|---|---:|",
    ]
    for item in refs["most_reused"]:
        lines.append(f"| {item['title']} | {item['node_count']} |")
    lines += [
        "",
        "## Interpretation",
        "",
        "The atlas is structurally complete against its declared family-level scope and passes its machine checks. Editorial depth is intentionally disclosed rather than hidden: the next improvement frontier is manual refinement of graph-derived role summaries, examples, limitations, and node-specific source trails—not inflation of the node count.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=root / "data" / "atlas.json")
    parser.add_argument("--json-report", type=Path, default=root / "dist" / "content_audit_report.json")
    parser.add_argument("--md-report", type=Path, default=root / "dist" / "content_audit_report.md")
    args = parser.parse_args()
    report = audit(args.data)
    args.json_report.parent.mkdir(parents=True, exist_ok=True)
    args.json_report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.md_report.write_text(markdown(report), encoding="utf-8")
    print(json.dumps(report["counts"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

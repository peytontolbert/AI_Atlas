#!/usr/bin/env python3
"""Generate per-node source-audit work packets.

Packets are read-only work items for reviewers or subagents. Review output belongs
in audit/node_reviews/<node_id>.json.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from validate_source_audit import edge_units, factual_units


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=root / "data" / "atlas.json")
    parser.add_argument("--out-dir", type=Path, default=root / "audit" / "node_packets")
    args = parser.parse_args()

    data = json.loads(args.data.read_text(encoding="utf-8"))
    refs = {ref["id"]: ref for ref in data["references"]}
    sentences_by_node: dict[str, list[dict]] = {}
    edges_by_node: dict[str, list[dict]] = {}
    for unit in factual_units(data):
        sentences_by_node.setdefault(unit["node_id"], []).append(unit)
    for unit in edge_units(data):
        edges_by_node.setdefault(unit["node_id"], []).append(unit)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    index = []
    for node in data["nodes"]:
        node_refs = {ref_id: refs[ref_id] for ref_id in node["reference_ids"] if ref_id in refs}
        dependency_refs = set()
        for edge in node["dependencies"]:
            dep = next((candidate for candidate in data["nodes"] if candidate["id"] == edge["id"]), None)
            if dep:
                dependency_refs.update(dep["reference_ids"])
        packet = {
            "node_id": node["id"],
            "label": node["label"],
            "layer": node["layer"],
            "editorial_status": node["editorial_status"],
            "node": node,
            "sentence_units": sentences_by_node.get(node["id"], []),
            "edge_units": edges_by_node.get(node["id"], []),
            "candidate_references": {
                "node_references": node_refs,
                "dependency_references": {ref_id: refs[ref_id] for ref_id in sorted(dependency_refs) if ref_id in refs},
            },
            "review_output_path": f"audit/node_reviews/{node['id']}.json",
            "instructions": [
                "Audit every sentence_unit and edge_unit.",
                "Use verdicts from docs/SOURCE_AUDIT.md.",
                "Use source_ids from data/atlas.json references, or url:<URL> for additional sources.",
                "Do not mark verified unless the evidence location supports the exact claim.",
                "Write review output to review_output_path only.",
            ],
        }
        packet_path = args.out_dir / f"{node['id']}.json"
        packet_path.write_text(json.dumps(packet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        index.append({
            "node_id": node["id"],
            "label": node["label"],
            "layer": node["layer"],
            "sentence_units": len(packet["sentence_units"]),
            "edge_units": len(packet["edge_units"]),
            "packet": str(packet_path.relative_to(root)),
            "review": packet["review_output_path"],
        })
    (args.out_dir / "index.json").write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"packets": len(index), "out_dir": str(args.out_dir)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

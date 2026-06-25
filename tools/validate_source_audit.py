#!/usr/bin/env python3
"""Validate sentence-level and edge-level source audit ledgers.

By default this emits a coverage report without failing on missing audit records.
Use --strict when every factual unit and edge is expected to be audited.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

VERDICTS = {
    "verified",
    "supported_by_synthesis",
    "ambiguous",
    "disputed",
    "unsupported",
    "stale",
}
REQUIRED_SENTENCE_FIELDS = {
    "unit_id",
    "node_id",
    "field",
    "text",
    "source_ids",
    "evidence_location",
    "reviewer",
    "review_date",
    "verdict",
}
REQUIRED_EDGE_FIELDS = {
    "edge_id",
    "node_id",
    "dependency_id",
    "source_ids",
    "reviewer",
    "review_date",
    "verdict",
}
NODE_TEXT_FIELDS = ("definition", "why_it_matters")
NODE_LIST_FIELDS = ("examples", "limitations")


def stable_id(*parts: str) -> str:
    payload = "\x1f".join(parts).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:16]


def split_sentences(text: str) -> list[str]:
    text = " ".join(text.split())
    if not text:
        return []
    pieces = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9`])", text)
    return [piece.strip() for piece in pieces if piece.strip()]


def factual_units(data: dict[str, Any]) -> list[dict[str, str]]:
    units: list[dict[str, str]] = []
    for node in data["nodes"]:
        node_id = node["id"]
        for field in NODE_TEXT_FIELDS:
            for idx, sentence in enumerate(split_sentences(node[field]), start=1):
                units.append({
                    "unit_id": stable_id(node_id, field, str(idx), sentence),
                    "node_id": node_id,
                    "field": field,
                    "text": sentence,
                })
        for field in NODE_LIST_FIELDS:
            for idx, item in enumerate(node[field], start=1):
                text = " ".join(str(item).split())
                units.append({
                    "unit_id": stable_id(node_id, field, str(idx), text),
                    "node_id": node_id,
                    "field": f"{field}[{idx}]",
                    "text": text,
                })
        if node.get("terminal_reason"):
            text = " ".join(str(node["terminal_reason"]).split())
            units.append({
                "unit_id": stable_id(node_id, "terminal_reason", "1", text),
                "node_id": node_id,
                "field": "terminal_reason",
                "text": text,
            })
        for idx, edge in enumerate(node["dependencies"], start=1):
            text = " ".join(edge["rationale"].split())
            units.append({
                "unit_id": stable_id(node_id, edge["id"], edge["type"], str(idx), text),
                "node_id": node_id,
                "field": f"dependencies.{edge['id']}.rationale",
                "text": text,
            })
    return units


def edge_units(data: dict[str, Any]) -> list[dict[str, str]]:
    units: list[dict[str, str]] = []
    for node in data["nodes"]:
        for edge in node["dependencies"]:
            edge_id = stable_id(node["id"], edge["id"], edge["type"], edge["strength"], edge["rationale"])
            units.append({
                "edge_id": edge_id,
                "node_id": node["id"],
                "dependency_id": edge["id"],
                "type": edge["type"],
                "strength": edge["strength"],
                "rationale": edge["rationale"],
            })
    return units


def read_jsonl(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    if not path.exists():
        return [], [f"missing ledger: {path}"]
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}:{line_no}: invalid JSON: {exc}")
            continue
        if not isinstance(record, dict):
            errors.append(f"{path}:{line_no}: record must be an object")
            continue
        record["_line"] = line_no
        records.append(record)
    return records, errors


def validate_sentence_records(records: list[dict[str, Any]], source_ids: set[str]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for record in records:
        line = record.get("_line", "?")
        missing = REQUIRED_SENTENCE_FIELDS - set(record)
        if missing:
            errors.append(f"sentence ledger line {line}: missing fields {sorted(missing)}")
        unit_id = record.get("unit_id")
        if unit_id in seen:
            errors.append(f"sentence ledger line {line}: duplicate unit_id {unit_id}")
        if isinstance(unit_id, str):
            seen.add(unit_id)
        verdict = record.get("verdict")
        if verdict not in VERDICTS:
            errors.append(f"sentence ledger line {line}: invalid verdict {verdict!r}")
        refs = record.get("source_ids", [])
        if not isinstance(refs, list) or not refs:
            errors.append(f"sentence ledger line {line}: source_ids must be a non-empty list")
        else:
            unknown = sorted(ref for ref in refs if ref not in source_ids and not str(ref).startswith("url:"))
            if unknown:
                errors.append(f"sentence ledger line {line}: unknown source_ids {unknown}")
    return errors


def validate_edge_records(records: list[dict[str, Any]], source_ids: set[str]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for record in records:
        line = record.get("_line", "?")
        missing = REQUIRED_EDGE_FIELDS - set(record)
        if missing:
            errors.append(f"edge ledger line {line}: missing fields {sorted(missing)}")
        edge_id = record.get("edge_id")
        if edge_id in seen:
            errors.append(f"edge ledger line {line}: duplicate edge_id {edge_id}")
        if isinstance(edge_id, str):
            seen.add(edge_id)
        verdict = record.get("verdict")
        if verdict not in VERDICTS:
            errors.append(f"edge ledger line {line}: invalid verdict {verdict!r}")
        refs = record.get("source_ids", [])
        if not isinstance(refs, list) or not refs:
            errors.append(f"edge ledger line {line}: source_ids must be a non-empty list")
        else:
            unknown = sorted(ref for ref in refs if ref not in source_ids and not str(ref).startswith("url:"))
            if unknown:
                errors.append(f"edge ledger line {line}: unknown source_ids {unknown}")
    return errors


def audit(args: argparse.Namespace) -> tuple[dict[str, Any], list[str]]:
    data = json.loads(args.data.read_text(encoding="utf-8"))
    source_ids = {ref["id"] for ref in data["references"]}
    sentence_units = factual_units(data)
    edge_review_units = edge_units(data)
    sentence_records, sentence_errors = read_jsonl(args.sentence_ledger)
    edge_records, edge_errors = read_jsonl(args.edge_ledger)

    errors = sentence_errors + edge_errors
    errors.extend(validate_sentence_records(sentence_records, source_ids))
    errors.extend(validate_edge_records(edge_records, source_ids))

    expected_sentence_ids = {unit["unit_id"] for unit in sentence_units}
    expected_edge_ids = {unit["edge_id"] for unit in edge_review_units}
    audited_sentence_ids = {record.get("unit_id") for record in sentence_records}
    audited_edge_ids = {record.get("edge_id") for record in edge_records}
    unknown_sentence_ids = sorted(str(unit_id) for unit_id in audited_sentence_ids - expected_sentence_ids if unit_id)
    unknown_edge_ids = sorted(str(edge_id) for edge_id in audited_edge_ids - expected_edge_ids if edge_id)
    if unknown_sentence_ids:
        errors.append(f"sentence ledger contains unknown unit_ids: {unknown_sentence_ids[:20]}")
    if unknown_edge_ids:
        errors.append(f"edge ledger contains unknown edge_ids: {unknown_edge_ids[:20]}")

    audited_sentence_count = len(expected_sentence_ids & audited_sentence_ids)
    audited_edge_count = len(expected_edge_ids & audited_edge_ids)
    sentence_verdicts = Counter(record.get("verdict") for record in sentence_records if record.get("unit_id") in expected_sentence_ids)
    edge_verdicts = Counter(record.get("verdict") for record in edge_records if record.get("edge_id") in expected_edge_ids)
    missing_sentences = [unit for unit in sentence_units if unit["unit_id"] not in audited_sentence_ids]
    missing_edges = [unit for unit in edge_review_units if unit["edge_id"] not in audited_edge_ids]

    report = {
        "strict": args.strict,
        "data": str(args.data),
        "sentence_ledger": str(args.sentence_ledger),
        "edge_ledger": str(args.edge_ledger),
        "sentence_units": len(sentence_units),
        "audited_sentence_units": audited_sentence_count,
        "unaudited_sentence_units": len(missing_sentences),
        "sentence_coverage_percent": round(100 * audited_sentence_count / len(sentence_units), 2) if sentence_units else 100.0,
        "edge_units": len(edge_review_units),
        "audited_edge_units": audited_edge_count,
        "unaudited_edge_units": len(missing_edges),
        "edge_coverage_percent": round(100 * audited_edge_count / len(edge_review_units), 2) if edge_review_units else 100.0,
        "sentence_verdicts": dict(sentence_verdicts),
        "edge_verdicts": dict(edge_verdicts),
        "sample_unaudited_sentences": missing_sentences[:20],
        "sample_unaudited_edges": missing_edges[:20],
        "errors": errors,
    }

    if args.strict:
        if missing_sentences:
            errors.append(f"strict mode: {len(missing_sentences)} factual units lack sentence audit records")
        if missing_edges:
            errors.append(f"strict mode: {len(missing_edges)} edges lack edge audit records")
        blocking_sentence_verdicts = sentence_verdicts.get("unsupported", 0) + sentence_verdicts.get("ambiguous", 0)
        blocking_edge_verdicts = edge_verdicts.get("unsupported", 0) + edge_verdicts.get("ambiguous", 0)
        if blocking_sentence_verdicts:
            errors.append(f"strict mode: {blocking_sentence_verdicts} sentence records are unsupported or ambiguous")
        if blocking_edge_verdicts:
            errors.append(f"strict mode: {blocking_edge_verdicts} edge records are unsupported or ambiguous")
    return report, errors


def markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Source Audit Coverage Report",
        "",
        "This report measures sentence-level and edge-level source audit ledger coverage. It does not perform source retrieval or judge source quality by itself.",
        "",
        "## Summary",
        "",
        "| Measure | Value |",
        "|---|---:|",
        f"| Factual sentence units | {report['sentence_units']} |",
        f"| Audited sentence units | {report['audited_sentence_units']} |",
        f"| Unaudited sentence units | {report['unaudited_sentence_units']} |",
        f"| Sentence coverage | {report['sentence_coverage_percent']}% |",
        f"| Edge units | {report['edge_units']} |",
        f"| Audited edge units | {report['audited_edge_units']} |",
        f"| Unaudited edge units | {report['unaudited_edge_units']} |",
        f"| Edge coverage | {report['edge_coverage_percent']}% |",
        f"| Ledger errors | {len(report['errors'])} |",
        "",
        "## Sentence Verdicts",
        "",
        "| Verdict | Count |",
        "|---|---:|",
    ]
    for verdict in sorted(VERDICTS):
        lines.append(f"| `{verdict}` | {report['sentence_verdicts'].get(verdict, 0)} |")
    lines.extend([
        "",
        "## Edge Verdicts",
        "",
        "| Verdict | Count |",
        "|---|---:|",
    ])
    for verdict in sorted(VERDICTS):
        lines.append(f"| `{verdict}` | {report['edge_verdicts'].get(verdict, 0)} |")
    lines.extend([
        "",
        "## Sample Unaudited Sentences",
        "",
    ])
    for unit in report["sample_unaudited_sentences"]:
        lines.append(f"- `{unit['node_id']}` `{unit['field']}` `{unit['unit_id']}`: {unit['text']}")
    lines.extend([
        "",
        "## Sample Unaudited Edges",
        "",
    ])
    for unit in report["sample_unaudited_edges"]:
        lines.append(f"- `{unit['node_id']} -> {unit['dependency_id']}` `{unit['type']}` `{unit['strength']}` `{unit['edge_id']}`")
    if report["errors"]:
        lines.extend(["", "## Errors", ""])
        for error in report["errors"]:
            lines.append(f"- {error}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=root / "data" / "atlas.json")
    parser.add_argument("--sentence-ledger", type=Path, default=root / "audit" / "source_sentence_ledger.jsonl")
    parser.add_argument("--edge-ledger", type=Path, default=root / "audit" / "edge_review_ledger.jsonl")
    parser.add_argument("--json-report", type=Path, default=root / "dist" / "source_audit_report.json")
    parser.add_argument("--md-report", type=Path, default=root / "dist" / "source_audit_report.md")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    report, errors = audit(args)
    args.json_report.parent.mkdir(parents=True, exist_ok=True)
    args.json_report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.md_report.write_text(markdown(report), encoding="utf-8")
    print(json.dumps({
        "sentence_coverage_percent": report["sentence_coverage_percent"],
        "edge_coverage_percent": report["edge_coverage_percent"],
        "errors": len(errors),
        "strict": args.strict,
    }, indent=2))
    if errors:
        for error in errors[:50]:
            print(f"source-audit: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

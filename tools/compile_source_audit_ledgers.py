#!/usr/bin/env python3
"""Compile per-node audit reviews into canonical JSONL ledgers."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_review(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: review must be a JSON object")
    return data


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reviews-dir", type=Path, default=root / "audit" / "node_reviews")
    parser.add_argument("--sentence-ledger", type=Path, default=root / "audit" / "source_sentence_ledger.jsonl")
    parser.add_argument("--edge-ledger", type=Path, default=root / "audit" / "edge_review_ledger.jsonl")
    args = parser.parse_args()

    sentence_records: list[dict[str, Any]] = []
    edge_records: list[dict[str, Any]] = []
    for path in sorted(args.reviews_dir.glob("*.json")):
        review = load_review(path)
        for record in review.get("sentence_reviews", []):
            if not isinstance(record, dict):
                raise ValueError(f"{path}: sentence_reviews entries must be objects")
            sentence_records.append(record)
        for record in review.get("edge_reviews", []):
            if not isinstance(record, dict):
                raise ValueError(f"{path}: edge_reviews entries must be objects")
            edge_records.append(record)

    args.sentence_ledger.parent.mkdir(parents=True, exist_ok=True)
    args.sentence_ledger.write_text("".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in sentence_records), encoding="utf-8")
    args.edge_ledger.write_text("".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in edge_records), encoding="utf-8")
    print(json.dumps({
        "review_files": len(list(args.reviews_dir.glob("*.json"))),
        "sentence_records": len(sentence_records),
        "edge_records": len(edge_records),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

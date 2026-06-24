#!/usr/bin/env python3
"""Validate and build the standalone AI Dependency Atlas viewer.

The canonical source of truth is data/atlas.json. The generated HTML embeds an
exact minified copy of that data so it can be opened directly from disk without
a server or external dependency.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import shutil
import sys
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_validator(path: Path):
    spec = importlib.util.spec_from_file_location("atlas_validator", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load validator: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def safe_embedded_json(data: dict) -> str:
    # Prevent an embedded string from terminating the application/json script.
    return (
        json.dumps(data, ensure_ascii=False, separators=(",", ":"))
        .replace("</", "<\\/")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


def build(root: Path) -> dict:
    data_path = root / "data" / "atlas.json"
    schema_path = root / "schema" / "atlas.schema.json"
    template_path = root / "viewer.template.html"
    validator_path = root / "tools" / "validate_atlas.py"
    audit_path = root / "tools" / "audit_content.py"
    dist = root / "dist"
    dist.mkdir(parents=True, exist_ok=True)

    for path in (data_path, schema_path, template_path, validator_path, audit_path):
        if not path.is_file():
            raise FileNotFoundError(path)

    validator = load_validator(validator_path)
    report = validator.validate(data_path, schema_path)
    (dist / "validation_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (dist / "validation_report.md").write_text(
        validator.markdown_report(report), encoding="utf-8"
    )
    if not report["passed"]:
        for error in report["errors"]:
            print(f"ERROR: {error}", file=sys.stderr)
        raise RuntimeError("Atlas validation failed; build stopped.")


    auditor = load_validator(audit_path)
    content_audit = auditor.audit(data_path)
    (dist / "content_audit_report.json").write_text(
        json.dumps(content_audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (dist / "content_audit_report.md").write_text(
        auditor.markdown(content_audit), encoding="utf-8"
    )

    data = json.loads(data_path.read_text(encoding="utf-8"))
    template = template_path.read_text(encoding="utf-8")
    placeholder = "__ATLAS_JSON__"
    if template.count(placeholder) != 1:
        raise ValueError("Viewer template must contain exactly one __ATLAS_JSON__ placeholder.")

    html = template.replace(placeholder, safe_embedded_json(data))
    html_path = dist / "ai_dependency_atlas_v2.html"
    html_path.write_text(html, encoding="utf-8")

    export_json = dist / "ai_dependency_atlas_v2_data.json"
    shutil.copyfile(data_path, export_json)

    manifest = {
        "artifact": data["meta"]["title"],
        "version": data["meta"]["version"],
        "updated": data["meta"]["updated"],
        "status": data["meta"]["status"],
        "canonical_source": "data/atlas.json",
        "generated_files": {
            "ai_dependency_atlas_v2.html": sha256(html_path),
            "ai_dependency_atlas_v2_data.json": sha256(export_json),
            "validation_report.json": sha256(dist / "validation_report.json"),
            "validation_report.md": sha256(dist / "validation_report.md"),
            "content_audit_report.json": sha256(dist / "content_audit_report.json"),
            "content_audit_report.md": sha256(dist / "content_audit_report.md"),
        },
        "inputs": {
            "data/atlas.json": sha256(data_path),
            "schema/atlas.schema.json": sha256(schema_path),
            "viewer.template.html": sha256(template_path),
            "tools/validate_atlas.py": sha256(validator_path),
            "tools/audit_content.py": sha256(audit_path),
        },
        "validated_metrics": report["summary"],
    }
    manifest_path = dist / "build_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return manifest


def main() -> int:
    default_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=default_root)
    args = parser.parse_args()
    manifest = build(args.root.resolve())
    metrics = manifest["validated_metrics"]
    print(
        f"Built {metrics['nodes']} nodes and {metrics['typed_edges']} typed edges: "
        f"{args.root.resolve() / 'dist' / 'ai_dependency_atlas_v2.html'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

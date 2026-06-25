PYTHON ?= python3
SERVE_HOST ?= 127.0.0.1
PORT ?= 8088

.PHONY: validate build test smoke serve audit-packets compile-source-audit source-audit source-audit-strict strict-blockers clean

validate:
	$(PYTHON) tools/validate_atlas.py

build: validate
	$(PYTHON) tools/build_atlas.py

test: build
	$(PYTHON) -m unittest discover -s tests -v

smoke: build
	$(PYTHON) tools/smoke_test_viewer.py

audit-packets:
	$(PYTHON) tools/generate_audit_packets.py

compile-source-audit:
	$(PYTHON) tools/compile_source_audit_ledgers.py

source-audit: compile-source-audit
	$(PYTHON) tools/validate_source_audit.py

source-audit-strict: compile-source-audit
	$(PYTHON) tools/validate_source_audit.py --strict

strict-blockers: compile-source-audit
	$(PYTHON) tools/strict_blocker_report.py

serve: build
	$(PYTHON) tools/serve_atlas.py --host $(SERVE_HOST) --port $(PORT)

clean:
	rm -f dist/ai_dependency_atlas_v2.html \
	      dist/ai_dependency_atlas_v2_data.json \
	      dist/build_manifest.json \
	      dist/validation_report.json \
	      dist/validation_report.md \
	      dist/content_audit_report.json \
	      dist/content_audit_report.md \
	      dist/source_audit_report.json \
	      dist/source_audit_report.md \
	      dist/strict_blocker_report.json \
	      dist/strict_blocker_report.md \
	      dist/ai_dependency_atlas_v2_preview.png \
	      dist/browser_smoke_report.json

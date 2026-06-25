# Exhaustiveness Roadmap

This project should not claim an unqualified "100% exhaustive map of all AI knowledge." AI research is open-ended, terminology changes, and boundaries are disputed. The stronger achievable target is a sequence of bounded completeness claims.

## Target Claim Format

Use this format for any strong completeness claim:

> The atlas is exhaustive for reusable family-level AI concepts within the declared scope, corpus, and update date, and each factual sentence has an audit record.

The claim must name:

- scope boundary;
- source corpus;
- update date;
- audit method;
- known exclusions;
- unresolved disputes.

## Coverage Levels

| Level | Claim | Evidence required |
|---|---|---|
| L0 | Structural graph validity | Schema validation, acyclic graph, typed edges, references present. |
| L1 | Declared family coverage | Layer coverage and required modern concepts represented. |
| L2 | Corpus-backed coverage | Systematic search across selected textbooks, surveys, papers, standards, and implementation docs. |
| L3 | Sentence-level source audit | Every factual sentence has an audit verdict and evidence pointer. |
| L4 | Expert-reviewed coverage | Independent subject-matter reviewers sign off by layer. |
| L5 | Living update process | Scheduled re-audits, stale-claim detection, and challenge workflow. |

The current repository is at L1 with structural validation and reference coverage. It is not yet at L3.

## Work Plan

### Phase 1: Freeze the Audit Boundary

Define:

- update date;
- included source classes;
- excluded source classes;
- layer-by-layer inclusion rules;
- what counts as a concept family;
- what counts as a subvariant, alias, product, benchmark, or implementation detail.

Output:

- updated `docs/SCOPE.md`;
- `audit/corpus.md`;
- `audit/search_strategy.md`.

### Phase 2: Build the Citation Ledger

Create machine-readable records for sentence-level audit.

Output:

- `audit/source_sentence_ledger.jsonl`;
- `audit/edge_review_ledger.jsonl`;
- a validator that fails on unaudited factual sentences once the audit mode is enabled.

### Phase 3: Layer-by-Layer Coverage Review

For each layer:

- search the declared corpus;
- extract candidate concepts;
- merge aliases and subvariants;
- add missing first-class families;
- record rejected candidates;
- document unresolved disputes.

Output:

- `audit/coverage_reviews/foundation.md`;
- `audit/coverage_reviews/representation.md`;
- `audit/coverage_reviews/paradigm.md`;
- `audit/coverage_reviews/objective.md`;
- `audit/coverage_reviews/mechanism.md`;
- `audit/coverage_reviews/model.md`;
- `audit/coverage_reviews/training.md`;
- `audit/coverage_reviews/memory.md`;
- `audit/coverage_reviews/reasoning.md`;
- `audit/coverage_reviews/alignment.md`;
- `audit/coverage_reviews/infrastructure.md`;
- `audit/coverage_reviews/system.md`.

### Phase 4: Edge Review

Review every dependency edge for:

- direction;
- relationship type;
- strength;
- rationale;
- source support;
- plausible missing prerequisite;
- plausible overclaim.

Output:

- audited edge ledger;
- generated edge-audit report;
- list of changed, removed, or disputed edges.

### Phase 5: Sentence Audit

Split every prose field into factual sentences and assign verdicts.

Output:

- verified sentence ledger;
- unsupported sentence report;
- stale sentence report;
- disputed sentence report.

### Phase 6: Release Gate

Only after Phases 1-5 are complete should the README claim sentence-level fact checking. The release should still avoid universal language.

Allowed:

> Exhaustive against the declared 2026-06-25 corpus and source-audited at sentence level.

Not allowed:

> Complete map of all AI knowledge.

## Reviewer Standard

For a high-confidence release, each layer should have at least one reviewer with direct expertise in that layer. Cross-layer dependencies should receive a second review because edge direction and strength are often where ontology errors hide.

## Maintenance Standard

Re-audit at fixed intervals or when any of these happen:

- major new survey appears;
- new architecture or training family becomes reusable;
- standards or regulations change;
- source URL disappears;
- a user challenges an omission;
- a dependency edge is disputed.

## Practical Next Milestone

The next realistic milestone is:

> L2 coverage review plus L3 sentence audit for the 42 currently curated nodes.

After that, expand to the 278 graph-derived nodes and all 1,225 edges.

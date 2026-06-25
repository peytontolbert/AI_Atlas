# Source Audit Protocol

This document defines the standard required before the atlas can claim sentence-level fact checking. It is intentionally stricter than the current reference-pointer model.

## Current Claim

The current atlas has reference coverage for every node and rationale text for every dependency edge. That is not the same as sentence-level verification.

The current claim is:

- every node has at least one relevant source pointer;
- every dependency edge is typed, strength-labeled, and justified;
- the graph passes structural validation;
- supporting prose discloses whether it is curated or graph-derived.

## Stronger Claim Target

A node is sentence-audited only when every factual sentence in these fields is individually checked against one or more sources:

- `definition`
- `why_it_matters`
- `examples`
- `limitations`
- dependency `rationale`
- terminal `terminal_reason`

Each checked sentence must have an audit record with:

- node ID;
- field name;
- sentence text or stable sentence hash;
- source ID or source URL;
- source type;
- evidence location, such as section, page, theorem, figure, table, paragraph, or quoted phrase;
- reviewer;
- review date;
- verdict;
- notes for ambiguity or dispute.

## Verdicts

Use one of these verdicts:

| Verdict | Meaning |
|---|---|
| `verified` | The sentence is directly supported by the cited source. |
| `supported_by_synthesis` | The sentence is a defensible synthesis of multiple sources. |
| `ambiguous` | The source partially supports the sentence, but wording should be narrowed. |
| `disputed` | Credible sources disagree. The atlas should disclose the dispute. |
| `unsupported` | The sentence lacks adequate support and should be edited or removed. |
| `stale` | The sentence may have been accurate before but needs a newer source. |

## Source Quality

Prefer sources in this order:

1. Primary papers, specifications, and standards.
2. Official technical reports from recognized institutions.
3. High-quality surveys and textbooks.
4. Reproducible implementation documentation.
5. Vendor documentation only for vendor-specific behavior.

Do not use blog posts, marketing pages, forum comments, or generated summaries as sole support for core claims unless the sentence is explicitly about that source.

## Edge Audit Standard

A dependency edge is audited only when the reviewer can answer all of these:

- Does the source support the existence of the dependency?
- Is the chosen relationship type the narrowest correct type?
- Is the strength label defensible as `core`, `common`, or `optional`?
- Is the direction correct under the atlas convention, from higher-level concept to prerequisite?
- Does the rationale avoid overstating necessity?

## Completeness Audit Standard

Completeness must be bounded by a declared corpus and time window. A defensible audit can claim:

> Exhaustive against corpus X, scope Y, and update date Z.

It cannot honestly claim:

> Exhaustive over all AI knowledge for all time.

For each layer, a completeness audit must include:

- source corpus searched;
- query strategy;
- inclusion and exclusion decisions;
- candidate concepts rejected as aliases or subvariants;
- missing-concept challenges and resolutions;
- reviewer sign-off;
- update date.

## Required Audit Artifacts

Before upgrading the project claim, add these files or equivalent structured data:

- `audit/source_sentence_ledger.jsonl`
- `audit/edge_review_ledger.jsonl`
- `audit/coverage_reviews/`
- `audit/disputed_claims.md`
- `audit/stale_claims.md`

Generated audit reports should summarize:

- total factual sentences;
- verified sentences;
- synthesis-supported sentences;
- ambiguous, disputed, unsupported, and stale sentences;
- audited edges;
- unaudited edges;
- coverage status by layer.

## Release Rule

Do not describe a release as sentence-level fact-checked unless:

- every factual sentence has an audit verdict;
- every `unsupported` sentence has been edited or removed;
- every `ambiguous` sentence has been narrowed or explicitly qualified;
- every `disputed` sentence has a visible dispute note;
- every source URL or bibliographic reference resolves or has archival metadata;
- the audit report is generated from machine-readable audit records.

# Search Strategy

This file records the method used to support bounded completeness claims.

## Required Per-Layer Procedure

1. Search canonical textbooks and surveys for the layer.
2. Search primary-paper chains for major families and named omissions.
3. Search standards, specifications, and official technical reports where relevant.
4. Extract candidate concepts, aliases, subvariants, and implementation details.
5. Merge candidates that do not introduce distinct dependency patterns.
6. Record rejected candidates with reasons.
7. Record unresolved disputes.
8. Update the coverage review file for the layer.

## Candidate Disposition Values

| Value | Meaning |
|---|---|
| `accepted_node` | Added or already represented as a first-class atlas node. |
| `alias` | Covered as an alias of an existing node. |
| `subvariant` | Covered by a broader existing concept family. |
| `product_or_release` | Excluded because it is a product, release, benchmark, dataset, or implementation. |
| `out_of_scope` | Outside the declared atlas scope. |
| `disputed` | Needs reviewer discussion. |
| `deferred` | Plausible but not yet resolved. |

## Query Log

Add search queries here during coverage reviews.

| Date | Layer | Query or source | Result summary | Reviewer |
|---|---|---|---|---|

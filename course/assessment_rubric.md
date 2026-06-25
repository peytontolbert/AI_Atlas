# Assessment Rubric

## Lesson Artifact Rubric

| Criterion | Developing | Proficient | Advanced |
|---|---|---|---|
| Atlas grounding | Mentions concepts loosely. | Uses valid atlas node IDs and layer relationships. | Traces dependencies across layers and explains why they matter. |
| Technical accuracy | Contains vague or unsupported claims. | Claims are mostly accurate and scoped. | Claims are precise, sourced where needed, and limitations are explicit. |
| System thinking | Focuses on isolated model behavior. | Connects data, objective, model, and evaluation. | Adds memory, tools, safety, infrastructure, monitoring, and rollback. |
| Evaluation quality | Uses a single success metric. | Defines task and regression checks. | Adds adversarial, calibration, human, operational, and release-gate checks. |
| Communication | Hard to follow or incomplete. | Clear and complete. | Concise, defensible, and useful for implementation. |

## Capstone Rubric

| Area | Points | Requirements |
|---|---:|---|
| Dependency map | 20 | Includes at least five atlas layers and valid node IDs. |
| Data and representation plan | 15 | Defines data sources, transformations, preserved/lost information, and leakage risks. |
| Objective and model choice | 15 | Justifies objective and architecture against alternatives and baselines. |
| Evaluation and safety | 20 | Includes golden tests, regressions, adversarial cases, human or judge review where relevant, thresholds, and rollback. |
| Infrastructure and operations | 15 | Specifies request path, serving constraints, observability, cost, and failure recovery. |
| Evidence and limitations | 15 | States what evidence is required for release and what remains out of scope. |

## Passing Standard

A passing capstone must:

- Use valid node IDs from `data/atlas.json`.
- Include at least one evaluation artifact.
- Include at least one failure or safety case.
- Include at least one deployment or operational constraint.
- State what would make the system not ready for release.

## Advanced Standard

An advanced capstone also:

- Compares at least two objectives or model families.
- Separates retrieval, generation, and citation evaluation where relevant.
- Includes monitoring and rollback plans.
- Documents uncertainty, provenance, or audit needs.
- Explains how the design could be simplified while preserving the goal.

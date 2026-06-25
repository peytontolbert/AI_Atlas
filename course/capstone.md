# Capstone Project

## Goal

Design or prototype an AI system using the Dependency Atlas as the dependency map.

The capstone should prove that the learner can move from abstract AI concepts to a complete, auditable system design.

## Project Options

Choose one:

1. RAG assistant over a small document set.
2. Coding assistant with tool-use boundaries.
3. LLM-as-judge evaluation harness.
4. Image, audio, or multimodal generation workflow.
5. Time-series anomaly detection system.
6. Recommendation or ranking prototype.
7. Scientific or simulation assistant.
8. Verified agent workflow with structured outputs.
9. Custom project approved by the instructor.

## Required Sections

### 1. System Goal

State the target behavior and users.

### 2. Atlas Dependency Map

List at least five layers and valid node IDs.

Example format:

| Layer | Node IDs | Role in system |
|---|---|---|
| representation | `tokens_vocab`, `embeddings` | Encode text and retrieval queries. |
| memory | `rag`, `dense_retrieval` | Retrieve supporting evidence. |
| alignment | `benchmarks_metrics`, `human_evaluation` | Evaluate quality and risk. |

### 3. Data Plan

Include:

- Source data.
- Filtering and cleaning.
- Splits.
- Leakage risks.
- Provenance requirements.

### 4. Objective and Model Plan

Include:

- Objective or scoring rule.
- Candidate model families.
- Baseline.
- Training or adaptation plan if applicable.

### 5. Evaluation Plan

Include:

- Golden tests.
- Regression tests.
- Adversarial or edge cases.
- Human review or LLM-as-judge rubric if useful.
- Release threshold.

### 6. Safety and Failure Analysis

Include:

- Known failure modes.
- Refusal or escalation rules.
- Monitoring signals.
- Rollback plan.

### 7. Infrastructure Plan

Include:

- Request path.
- Runtime or serving plan.
- Storage and retrieval dependencies.
- Observability.
- Cost or latency targets.

### 8. Evidence Required for Completion

State exactly what evidence would make the project complete and what remains out of scope.

## Submission Formats

Choose one:

- Design brief, 4 to 6 pages.
- Working prototype plus 2-page report.
- Slide deck plus appendix.
- Repository with README, eval results, and architecture diagram.

## Review Questions

The final review should ask:

- Are the node IDs valid?
- Are the dependencies plausible and explained?
- Is the evaluation strong enough for the stated risk?
- Are limitations explicit?
- Is there enough evidence to decide release or no-release?

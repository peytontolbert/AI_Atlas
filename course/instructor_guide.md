# Instructor Guide

## Audience

This course works for:

- Engineers learning modern AI system design.
- Researchers who want a dependency map across AI subfields.
- Product and safety teams who need shared language for evaluation and release decisions.
- Self-study learners building a portfolio project.

## Teaching Principles

- Teach dependency order, not trivia.
- Require artifacts every week.
- Ask learners to identify what evidence would change their mind.
- Separate model behavior from system behavior.
- Separate audit-record coverage from universal exhaustiveness.

## Pacing Options

| Format | Duration | Plan |
|---|---:|---|
| Workshop | 2 days | Lessons 01, 02, 04, 08, 10, 12 plus capstone sketch. |
| Fast track | 2 weeks | One lesson per weekday plus final project. |
| Standard | 6 weeks | Two lessons per week plus capstone review. |
| Semester | 12 to 14 weeks | One lesson per week, labs, and project demos. |

## Class Session Template

Use this structure for each lesson:

1. Opening diagnostic question, 5 minutes.
2. Atlas node walkthrough, 15 minutes.
3. Concept lecture, 20 minutes.
4. Small-group exercise, 25 minutes.
5. Artifact drafting, 20 minutes.
6. Review and critique, 15 minutes.
7. Exit ticket, 5 minutes.

## Facilitation Prompts

Ask repeatedly:

- What is the input representation?
- What is the learning signal?
- What objective is optimized?
- What model family is appropriate and why?
- What evidence proves the system works?
- What failure mode remains after the proposed mitigation?
- What changes in production?

## Recommended Grading

- Lesson artifacts: 50%.
- Participation or peer review: 15%.
- Capstone dependency map: 15%.
- Capstone implementation or design brief: 20%.

## Using the Atlas Files

Primary files:

- `data/atlas.json`: Canonical graph and node data.
- `dist/ai_dependency_atlas_v2.html`: Standalone viewer.
- `docs/SOURCE_AUDIT.md`: Audit standard.
- `dist/source_audit_report.md`: Audit-record coverage report.
- `dist/strict_blocker_report.md`: Strict blocker report, expected to be zero after completion work.

## Instructor Cautions

- Do not let learners treat a named model as an explanation.
- Do not accept benchmarks without failure analysis.
- Do not accept RAG answers without retrieval evidence.
- Do not accept agent designs without permission and rollback boundaries.
- Do not claim universal coverage of all AI knowledge; teach bounded, auditable coverage.

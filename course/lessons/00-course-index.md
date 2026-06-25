# AI Dependency Atlas Course

This course teaches the Dependency Atlas as a dependency-ordered map of AI concepts. It is designed for self-study, classroom use, or team onboarding.

## Course Outcomes

By the end of the course, learners should be able to:

- Trace an AI system from foundations through representations, objectives, models, training, memory, reasoning, evaluation, infrastructure, and applications.
- Explain why each layer depends on earlier layers.
- Choose appropriate model families, objectives, evaluation methods, and deployment patterns for a concrete system.
- Build a small AI system design brief with explicit evidence, risks, and operational constraints.
- Use the atlas audit artifacts to distinguish graph structure, sourced facts, synthesis claims, and remaining scope boundaries.

## Format

Each lesson is a teachable module with:

- Learning outcomes.
- Atlas nodes to review.
- Lecture plan.
- Guided discussion prompts.
- Hands-on lab.
- Assessment questions.
- Deliverable and mastery rubric.

Suggested pacing:

- Fast track: 2 weeks, one lesson per weekday plus capstone.
- Standard track: 6 weeks, two lessons per week plus project time.
- Deep track: 12 to 14 weeks, one lesson per week with implementation labs.

## Lesson Sequence

| Lesson | Topic | Primary outcome |
|---:|---|---|
| 01 | Mathematical and Computational Foundations | Translate core math into code, diagnostics, and scaling checks. |
| 02 | Data and Representations | Explain how raw information becomes model-readable structure. |
| 03 | Learning Paradigms | Identify the source of learning signal and interaction pattern. |
| 04 | Objectives and Statistical Inference | Connect model behavior to losses, rewards, likelihoods, and uncertainty. |
| 05 | Computational Primitives and Mechanisms | Trace information flow through reusable model and agent mechanisms. |
| 06 | Model and Architecture Families | Compare model families by inductive bias, data fit, and failure mode. |
| 07 | Training, Adaptation, and Compression | Design training and adaptation workflows with evaluation and recovery. |
| 08 | Memory, Retrieval, and Knowledge | Build retrieval, RAG, provenance, and structured memory evaluations. |
| 09 | Reasoning, Planning, and Agency | Design safe multi-step systems with tools, state, permissions, and verification. |
| 10 | Alignment, Safety, and Evaluation | Build eval plans that cover quality, safety, robustness, and release gates. |
| 11 | Infrastructure and Serving | Explain production tradeoffs around latency, throughput, cost, and observability. |
| 12 | Systems and Applications | Combine all layers into complete system dependency maps. |

## Required Artifacts

Learners should produce one artifact per lesson:

- Lesson 01: gradient and shape-check note.
- Lesson 02: representation comparison table.
- Lesson 03: learning lifecycle map.
- Lesson 04: objective comparison memo.
- Lesson 05: mechanism walkthrough diagram.
- Lesson 06: architecture selection matrix.
- Lesson 07: training run card.
- Lesson 08: retrieval evaluation table.
- Lesson 09: agent loop design.
- Lesson 10: evaluation and safety checklist.
- Lesson 11: serving plan.
- Lesson 12: system dependency map.
- Capstone: complete design brief or working prototype report.

## Completion Criteria

A learner completes the course when they can defend a capstone system with:

- At least five atlas layers represented.
- Valid node references from `data/atlas.json`.
- Data, objective, model, evaluation, and deployment choices justified.
- Safety and failure cases documented.
- Evidence required for release stated explicitly.

See `course/instructor_guide.md`, `course/assessment_rubric.md`, and `course/capstone.md` for teaching support.

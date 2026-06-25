# Lesson 10: Alignment, Safety, and Evaluation

## Learning Outcomes

After this lesson, learners can:

- Design evaluation plans that cover quality, safety, robustness, and release decisions.
- Distinguish task metrics, human evaluation, LLM-as-judge, calibration, red teaming, and monitoring.
- Build release gates tied to risk thresholds and regression tests.
- Explain what provenance, watermarking, formal verification, and runtime assurance can and cannot prove.

## Atlas Nodes

`benchmarks_metrics`, `human_evaluation`, `llm_as_judge`, `calibration_evaluation`, `robustness_ood`, `adversarial_security_eval`, `fairness_bias`, `safety_policy_alignment`, `red_teaming`, `interpretability`, `causal_ablation`, `mechanistic_interpretability`, `privacy_governance`, `repro_monitoring`, `eval_driven_development`, `output_watermarking`, `content_provenance`, `formal_model_verification`, `formal_agent_verification`, `runtime_assurance`

## Prerequisites

Learners should understand objectives, system behavior, and deployment context.

## Core Concepts

- Evaluation should cover capability, reliability, safety, and regressions.
- Benchmarks are useful but incomplete proxies.
- Human evaluation and LLM-as-judge methods require calibration and bias checks.
- Robustness, OOD, and adversarial tests reveal brittle behavior.
- Runtime monitors and release gates make evaluation operational.
- Provenance and watermarking support integrity claims but do not prove content truth.

## Teaching Plan

1. Start with a feature and ask what release would mean.
2. Define task metrics, safety metrics, and regression metrics.
3. Add human review and LLM-as-judge only where appropriate.
4. Add adversarial tests and calibration checks.
5. Convert the eval plan into release gates and monitoring.

## Guided Discussion

- What failure would be unacceptable even if average score improves?
- What should be evaluated before release and after release?
- When is a judge model useful, and how can it be biased?
- What does provenance prove, and what does it not prove?
- Which risks require runtime controls rather than offline tests?

## Lab

Create an evaluation harness plan for one AI feature.

Include:

- Golden tests.
- Regression tests.
- Adversarial cases.
- Human review criteria.
- Optional LLM-as-judge rubric and calibration sample.
- Release thresholds.
- Runtime monitoring.
- Rollback condition.

## Assessment Questions

1. Why can a benchmark hide a regression?
2. What is the difference between task success and safety success?
3. Why must LLM-as-judge be calibrated against human judgment?
4. What does runtime assurance add after deployment?
5. Why is provenance not the same as truth?

## Deliverable

An evaluation and safety checklist.

## Mastery Rubric

| Level | Evidence |
|---|---|
| Developing | Lists benchmarks only. |
| Proficient | Designs task, safety, regression, and release checks. |
| Advanced | Adds calibrated judging, adversarial testing, monitoring, and rollback. |

## Common Failure Mode

Testing only average performance and missing rare but high-impact failures.

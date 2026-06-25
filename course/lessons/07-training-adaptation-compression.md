# Lesson 07: Training, Adaptation, and Compression

## Learning Outcomes

After this lesson, learners can:

- Design a training or adaptation run with data, objective, stability, checkpoint, and evaluation plans.
- Explain pretraining, instruction tuning, LoRA, RLHF/RLAIF, DPO, RLVR, and GRPO as lifecycle stages.
- Identify risks from contamination, deduplication failures, instability, and regressions.
- Compare compression methods by cost, quality, latency, and recovery tradeoffs.

## Atlas Nodes

`pretraining`, `data_curation`, `dedup_decontamination`, `augmentation_synthetic`, `regularization`, `schedules_stabilization`, `distributed_mixed_precision`, `checkpoint_recovery`, `compute_optimal_training`, `sft_instruction`, `peft_lora`, `reward_rlhf`, `dpo_posttraining`, `grpo`, `rlvr`, `distillation_pruning`, `quantization_training`, `continual_testtime_adaptation`, `curriculum_data_mixtures`, `neural_architecture_search`, `domain_randomization`, `model_merging`, `task_arithmetic`

## Prerequisites

Learners should understand paradigms, objectives, and model families.

## Core Concepts

- Data quality and curation are central training decisions.
- Pretraining builds broad capability before task-specific adaptation.
- Instruction tuning and preference optimization shape user-facing behavior.
- LoRA and adapters reduce adaptation cost but introduce composition questions.
- Checkpoints, reproducibility, and recovery are part of training correctness.
- Compression trades capability, latency, memory, and cost.

## Teaching Plan

1. Walk through a model lifecycle from corpus to deployment.
2. Identify where each training or adaptation method enters.
3. Discuss contamination, deduplication, and provenance.
4. Compare fine-tuning, adapters, merging, and preference optimization.
5. Close with compression and serving constraints.

## Guided Discussion

- What evidence shows training improved the target behavior?
- What could regress after adaptation?
- What data should be excluded from training?
- What makes a checkpoint reproducible?
- When is compression acceptable, and how would you prove it?

## Lab

Design a small fine-tuning or adaptation run.

Include:

- Dataset source and filtering rules.
- Base model and adaptation method.
- Objective and training configuration.
- Checkpoint and rollback plan.
- Evaluation before and after.
- Failure analysis plan.

## Assessment Questions

1. Why do deduplication and decontamination matter?
2. What does LoRA change and what does it leave frozen?
3. How does DPO differ from reward-model RLHF?
4. What does quantization trade away?
5. Why is checkpoint recovery a correctness concern, not only convenience?

## Deliverable

A training run card.

## Mastery Rubric

| Level | Evidence |
|---|---|
| Developing | Lists training steps without evaluation or recovery. |
| Proficient | Designs a complete run with data, objective, checkpoint, and eval plan. |
| Advanced | Anticipates regressions, contamination, cost, and deployment constraints. |

## Common Failure Mode

Reporting that a model was fine-tuned without proving behavior improved or identifying what regressed.

# Lesson 03: Learning Paradigms

## Learning Outcomes

After this lesson, learners can:

- Identify the learning signal used by a system.
- Distinguish supervised, self-supervised, generative, reinforcement, preference, and adaptation paradigms.
- Explain how paradigms combine across the lifecycle of a modern AI product.
- Identify failure modes specific to interaction, feedback, and distribution shift.

## Atlas Nodes

`supervised_learning`, `unsupervised_learning`, `semi_weak_learning`, `self_supervised_learning`, `contrastive_learning`, `predictive_jepa_learning`, `generative_learning`, `reinforcement_learning`, `model_based_rl`, `imitation_inverse_rl`, `preference_learning`, `active_curriculum_learning`, `meta_learning`, `transfer_multitask_learning`, `continual_online_learning`, `federated_private_learning`, `evolutionary_population_learning`, `incontext_testtime_learning`, `automl_paradigm`, `sim_to_real_transfer`

## Prerequisites

Learners should understand labels, rewards, preferences, datasets, and objectives from Lessons 02 and 04.

## Core Concepts

- Supervised learning uses labeled examples.
- Self-supervised learning creates training signals from the input data itself.
- Generative learning models data production or transformation.
- Reinforcement learning learns from actions, rewards, and state transitions.
- Preference learning uses comparative judgments to shape behavior.
- Continual, transfer, meta, and test-time learning describe how systems adapt across tasks or time.

## Teaching Plan

1. Show five training records: labeled example, masked token, reward trajectory, preference pair, and unlabeled corpus.
2. Ask learners to identify the paradigm before naming it.
3. Map each paradigm to objectives and evaluation risks.
4. Discuss how a chat assistant or coding assistant combines multiple paradigms.
5. Close with lifecycle thinking: pretraining, adaptation, feedback, evaluation, deployment, monitoring.

## Guided Discussion

- What exactly is the learning signal?
- Who or what supplies the target?
- How can the signal be noisy, biased, sparse, or gameable?
- Which paradigms can be used before deployment, and which can continue after deployment?
- Why is in-context learning not the same as parameter training?

## Lab

Choose one AI product. Map the paradigms used across its lifecycle:

- Pretraining.
- Task adaptation.
- Feedback collection.
- Preference optimization or policy shaping.
- Evaluation.
- Runtime adaptation.

## Assessment Questions

1. How does self-supervised learning differ from unsupervised learning?
2. Why is reinforcement learning sensitive to reward design?
3. What does preference learning capture that labels may not capture?
4. How does transfer learning differ from meta-learning?
5. Why can continual learning create forgetting risks?

## Deliverable

A lifecycle map connecting paradigms to system stages.

## Mastery Rubric

| Level | Evidence |
|---|---|
| Developing | Names paradigms by surface features. |
| Proficient | Identifies the learning signal and expected failure mode. |
| Advanced | Maps multiple paradigms across a realistic system lifecycle. |

## Common Failure Mode

Using paradigm names as labels without identifying the actual source of feedback.

# Lesson 04: Objectives and Statistical Inference

## Learning Outcomes

After this lesson, learners can:

- Explain how losses, likelihoods, rewards, verifiers, and inference procedures shape behavior.
- Compare objectives by what they reward, ignore, and make easy to game.
- Connect uncertainty, calibration, and approximate inference to decision quality.
- Design evaluation tests that reveal objective mismatch.

## Atlas Nodes

`mle_cross_entropy`, `regression_losses`, `margin_ranking_metric`, `masked_prediction`, `autoregressive_objective`, `reconstruction_objective`, `contrastive_objective`, `elbo_variational`, `energy_objective`, `adversarial_minimax`, `score_matching`, `flow_matching`, `bellman_td`, `policy_actor_critic`, `reward_modeling`, `preference_optimization`, `bayesian_approx_inference`, `mcmc_em_message_passing`, `calibration_uncertainty_objective`, `multiobjective_constraints`, `process_reward_models`, `outcome_verifiers`

## Prerequisites

Learners should understand gradients, probability, labels, rewards, and preferences.

## Core Concepts

- Objectives define what improvement means during training or search.
- Cross-entropy and maximum likelihood reward probability assigned to observed data.
- Ranking and contrastive objectives shape relative comparisons.
- Reward models and verifiers convert preferences or outcomes into optimization signals.
- Calibration matters when scores influence decisions under risk.
- A proxy objective can improve while real-world utility declines.

## Teaching Plan

1. Present a desired behavior and ask what can actually be measured.
2. Compare two objectives for the same behavior.
3. Show how each objective can be gamed.
4. Connect objectives to data collection and evaluation.
5. Discuss uncertainty and calibration when predictions inform decisions.

## Guided Discussion

- What behavior does the objective directly optimize?
- What does it ignore?
- What would a model learn if it exploited the metric?
- How would you detect objective hacking?
- When is outcome verification easier than process supervision?

## Lab

Pick one model behavior to improve. Define two possible objectives and compare:

- Direct measurement.
- Missing behavior.
- Failure or gaming mode.
- Data requirements.
- Evaluation needed to distinguish them.

## Assessment Questions

1. What does cross-entropy penalize?
2. Why can a reward model be misaligned with user value?
3. What is the difference between process and outcome supervision?
4. Why is calibration not the same as accuracy?
5. When does approximate inference enter an AI system?

## Deliverable

A two-objective comparison memo.

## Mastery Rubric

| Level | Evidence |
|---|---|
| Developing | Describes objectives as generic scores. |
| Proficient | Explains what an objective rewards and ignores. |
| Advanced | Designs tests for objective mismatch and gaming. |

## Common Failure Mode

Assuming the objective is the intended behavior rather than a proxy for it.

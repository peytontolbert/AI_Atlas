# Lesson 04: Objectives and Statistical Inference

## Goal

Connect model behavior to the loss, likelihood, reward, verifier, or inference procedure that shaped it.

## Review Nodes

`mle_cross_entropy`, `autoregressive_objective`, `score_matching`, `margin_ranking_metric`, `bayesian_approx_inference`, `calibration_uncertainty_objective`, `reward_modeling`, `preference_optimization`, `outcome_verifiers`, `process_reward_models`

## Key Ideas

- Objectives define what improvement means during training.
- Cross-entropy and maximum likelihood reward probability assigned to observed data.
- Ranking and metric objectives shape relative comparisons.
- Reward models and verifiers turn preferences or outcomes into optimization signals.
- Calibration and uncertainty matter when systems make decisions under risk.

## Review Checklist

- Can you describe what cross-entropy penalizes?
- Can you distinguish outcome reward from process reward?
- Can you explain why a proxy objective can create unwanted behavior?
- Can you define calibration in practical terms?
- Can you identify when approximate inference is being used?

## Exercise

Pick one model behavior you want to improve. Define two possible objectives for it and compare:

- What each objective directly measures.
- What each objective ignores.
- How each could be gamed.
- Which evaluation would reveal the difference.

## Deliverable

A two-objective comparison memo.

## Common Failure Mode

Assuming the objective matches the intended behavior. It usually only approximates it.

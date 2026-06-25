# Lesson 06: Model and Architecture Families

## Learning Outcomes

After this lesson, learners can:

- Compare model families by inductive bias, data fit, training cost, and failure mode.
- Choose baselines before selecting large architectures.
- Explain why transformers, CNNs, diffusion models, SSMs, GNNs, and classical models fit different tasks.
- Defend an architecture choice with representation, objective, and deployment constraints.

## Atlas Nodes

`linear_glm`, `tree_ensemble_models`, `gaussian_processes`, `mlp`, `cnn`, `resnet_densenet`, `unet`, `rnn`, `lstm_gru`, `transformer`, `encoder_decoder_transformer`, `decoder_only_transformer`, `vision_transformer_perceiver`, `structured_ssm`, `mamba_selective_ssm`, `gnn`, `graph_transformer`, `autoencoder`, `vae`, `vqvae_tokenizer`, `gan`, `diffusion_model`, `flow_based_model`, `moe_model`, `neural_operator_pinn`, `world_model`, `jepa_model`, `multimodal_foundation`, `probabilistic_programming`, `vision_language_action_model`

## Prerequisites

Learners should understand representations, objectives, and mechanisms.

## Core Concepts

- Classical models remain essential baselines and diagnostic tools.
- CNNs encode locality and translation structure.
- Transformers scale flexible sequence modeling through attention.
- Diffusion and flow-style models generate through iterative transformation.
- GNNs and graph transformers preserve relational structure.
- SSMs and recurrent hybrids target long-sequence efficiency.
- Multimodal and VLA systems align multiple representation and action spaces.

## Teaching Plan

1. Start with a task and ask for the simplest credible baseline.
2. Compare three architecture families using the same data representation.
3. Discuss inductive bias and scaling behavior.
4. Map architecture choice to objective and evaluation.
5. Discuss deployment constraints: memory, latency, interpretability, and maintenance.

## Guided Discussion

- What does this architecture assume about the data?
- What does it scale well, and what does it make expensive?
- What baseline would embarrass this model if it performed similarly?
- Which failure modes come from the architecture rather than the data?
- What changes when the system becomes multimodal?

## Lab

For one task, choose three candidate architecture families.

For each candidate, write:

- Why it fits the representation.
- Required training data and objective.
- Expected strengths.
- Failure modes.
- Baseline comparison.
- Deployment concerns.

## Assessment Questions

1. Why are tree ensembles still useful in an AI atlas?
2. Why are decoder-only transformers natural for next-token prediction?
3. When is a diffusion model a better fit than an autoregressive model?
4. What does a graph neural network preserve that a flat vector may lose?
5. Why might an SSM be considered for long-context workloads?

## Deliverable

An architecture selection matrix.

## Mastery Rubric

| Level | Evidence |
|---|---|
| Developing | Chooses models by popularity. |
| Proficient | Matches architecture to data, objective, and evaluation. |
| Advanced | Defends architecture under baseline, scaling, and deployment constraints. |

## Common Failure Mode

Selecting an architecture before understanding the representation and objective.

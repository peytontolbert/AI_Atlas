# Lesson 06: Model and Architecture Families

## Goal

Compare architecture families by what they assume, what they scale, and where they fail.

## Review Nodes

`linear_glm`, `tree_ensemble_models`, `gaussian_processes`, `mlp`, `cnn`, `resnet_densenet`, `autoencoder`, `transformer`, `decoder_only_transformer`, `vision_transformer_perceiver`, `diffusion_model`, `unet`, `structured_ssm`, `mamba_selective_ssm`, `multimodal_foundation`, `world_model`

## Key Ideas

- Classical models remain essential baselines and diagnostic tools.
- CNNs encode locality and translation structure.
- Transformers scale flexible sequence modeling through attention.
- Diffusion and flow-style models generate through iterative transformation.
- SSMs and recurrent alternatives target long-sequence efficiency.
- Multimodal models align multiple representation spaces.

## Review Checklist

- Can you choose a baseline before choosing a deep architecture?
- Can you explain why CNNs work well for images?
- Can you explain why decoder-only transformers fit next-token prediction?
- Can you identify when diffusion is a natural fit?
- Can you compare transformer and SSM tradeoffs for long context?

## Exercise

For one task, choose three candidate architecture families. For each, write:

- Why it fits the data.
- What it would require to train.
- What it may fail at.
- What baseline would challenge it.

## Deliverable

An architecture selection matrix.

## Common Failure Mode

Choosing architectures by popularity instead of representation, objective, data size, and deployment constraints.

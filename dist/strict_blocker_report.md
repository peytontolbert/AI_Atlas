# Strict Source-Audit Blocker Report

This report lists records that prevent `make source-audit-strict` from passing. It does not downgrade or hide blockers.

## Summary

| Blocker class | Count |
|---|---:|
| Sentence blockers | 1254 |
| Edge blockers | 326 |

## Sentence Patterns

| Pattern | Count |
|---|---:|
| node-specific blocker | 546 |
| graph-derived substrate example | 293 |
| graph-derived role summary | 178 |
| graph-derived uses rationale | 94 |
| generic model limitation | 45 |
| generic system limitation | 27 |
| generic infrastructure limitation | 18 |
| generic foundation limitation | 18 |
| graph-derived operationalizes rationale | 16 |
| generic evaluation limitation | 10 |
| graph-derived evaluation rationale | 9 |

## Sentence Layers

| Layer | Count |
|---|---:|
| `model` | 213 |
| `system` | 186 |
| `mechanism` | 129 |
| `paradigm` | 119 |
| `training` | 106 |
| `infrastructure` | 95 |
| `representation` | 89 |
| `foundation` | 77 |
| `reasoning` | 72 |
| `memory` | 67 |
| `objective` | 63 |
| `alignment` | 38 |

## Edge Layers

| Layer | Count |
|---|---:|
| `system` | 82 |
| `model` | 55 |
| `paradigm` | 41 |
| `training` | 31 |
| `representation` | 21 |
| `mechanism` | 19 |
| `reasoning` | 17 |
| `infrastructure` | 16 |
| `alignment` | 12 |
| `objective` | 12 |
| `memory` | 11 |
| `foundation` | 9 |

## Top Nodes

| Node | Layer | Blockers |
|---|---|---:|
| `robotics` Robotics & embodied AI | `system` | 21 |
| `scientific_digital_twins` Scientific ML, simulators & digital twins | `system` | 18 |
| `timeseries_anomaly` Time-series forecasting, anomaly & fraud detection | `system` | 16 |
| `autonomous_vehicles` Autonomous vehicles, drones & navigation | `system` | 14 |
| `drug_protein` Drug discovery, protein & molecular design | `system` | 14 |
| `game_control` Game-playing, control & simulation agents | `system` | 13 |
| `multimodal_simulated_streams` Multimodal, simulated & streaming data | `representation` | 13 |
| `vqvae_tokenizer` VQ-VAE & learned discrete tokenizers | `model` | 13 |
| `cache_tool_interfaces` Caches, APIs & tool interfaces | `mechanism` | 12 |
| `cyber_finance` Cybersecurity, finance & operational risk AI | `system` | 12 |
| `differentiable_solvers` Differentiable ODE/PDE/SDE solvers | `mechanism` | 12 |
| `incontext_testtime_learning` In-context & test-time learning | `paradigm` | 12 |
| `medical_ai` Medical imaging & clinical decision support | `system` | 12 |
| `weather_climate` Weather, climate & geospatial forecasting | `system` | 12 |
| `automl_paradigm` AutoML & automated model design | `paradigm` | 11 |
| `llms` Large language models | `system` | 11 |
| `meta_learning` Meta-learning | `paradigm` | 11 |
| `multimodal_foundation` Multimodal foundation models | `model` | 11 |
| `neuroscience_cognition` Neuroscience & cognitive science | `foundation` | 11 |
| `chat_assistants` Conversational assistants & chatbots | `system` | 10 |
| `code_execution` Code execution, interpreters & sandboxes | `reasoning` | 10 |
| `edge_ondevice` Edge, on-device & neuromorphic deployment | `infrastructure` | 10 |
| `local_plasticity_learning` Perceptron, Hebbian, Oja & spike-timing plasticity | `paradigm` | 10 |
| `self_organizing_maps` Self-organizing maps & competitive learning | `model` | 10 |
| `sim_to_real_transfer` Sim-to-real, real-to-sim & digital transfer | `paradigm` | 10 |

# Scope and Completeness Contract

## Declared scope

The atlas is a curated, family-level dependency ontology for artificial intelligence. It maps reusable ideas across the path from formal substrate to deployed systems:

| Order | Layer | Inclusion boundary |
|---:|---|---|
| 1 | Mathematical & Computational Foundations | mathematics, computation, information, control, logic, systems, and formal specification |
| 2 | Data & Representations | data forms, symbolic units, latent state, uncertainty, knowledge, programs, and formal output languages |
| 3 | Learning Paradigms | how supervision, interaction, transfer, adaptation, privacy, simulation, and automated design organize learning |
| 4 | Objectives & Statistical Inference | losses, probabilistic inference, reward, preference, risk, and verification objectives |
| 5 | Computational Primitives & Mechanisms | reusable operations such as attention, convolution, routing, retrieval, recurrence, diffusion, constraints, and adaptive computation |
| 6 | Model & Architecture Families | enduring model families with a distinct computational or statistical dependency pattern |
| 7 | Training, Adaptation & Compression | data preparation, optimization, post-training, parameter adaptation, scaling, compression, and composition |
| 8 | Memory, Retrieval & Knowledge | working, episodic, semantic, procedural, parametric, retrieval, provenance, and lifecycle mechanisms |
| 9 | Reasoning, Planning & Agency | search, proof, program synthesis, planning, tool use, deliberation, repair, and agent control |
| 10 | Alignment, Safety & Evaluation | measurement, robustness, governance, interpretation, provenance, formal assurance, and runtime safety |
| 11 | Infrastructure & Serving | accelerators, kernels, compilers, storage, orchestration, serving, inference optimization, observability, and simulation |
| 12 | Systems & Applications | end-to-end systems that integrate multiple lower-layer families |

## Inclusion criteria

A concept is in scope when it satisfies most of the following:

1. It is reusable across multiple papers, systems, or implementations.
2. It has a distinct dependency pattern that would be lost if merged into another node.
3. It belongs to an enduring conceptual family rather than a single release or vendor feature.
4. It materially changes representation, learning, inference, reasoning, assurance, deployment, or application behavior.
5. It can be defined without relying on a product name.
6. At least one credible source family can ground the concept.

## Explicit exclusions

The following are outside the declared completeness boundary:

- individual GPT, BERT, Llama, Qwen, Claude, Gemini, Stable Diffusion, or other release/version nodes;
- every benchmark, dataset, package, framework, compiler, accelerator SKU, or commercial product;
- fine-grained variants that do not introduce a distinct dependency pattern;
- exhaustive historical priority claims where research lineages are disputed;
- an assurance that research terminology after the update date will remain stable;
- sentence-level source verification for every prose field;
- a claim that all domain-specific applications are enumerated.

Named models can appear as aliases or examples of a family. They become first-class nodes only when they introduce a reusable architecture, objective, training, reasoning, or deployment pattern not already represented.

## Modern coverage ledger

The v2 scope explicitly requires dedicated nodes for the omissions identified during review:

| Theme | Required nodes |
|---|---|
| Scaling | empirical scaling laws; compute-optimal training |
| Post-training | GRPO; RL with verifiable rewards; process supervision; outcome verifiers |
| Inference-time reasoning | test-time compute; best-of-N/verifier selection; Tree-of-Thought; Graph-of-Thought |
| Automated design | AutoML; neural architecture search |
| Adaptive computation | early exit/token skipping; Mixture-of-Depths |
| Structured generation | grammars/schemas; constrained decoding; typed outputs; validation/repair; runtime support |
| Provenance | generation-time watermarking; signed content credentials; cryptographic logs |
| Embodied transfer | sim-to-real; real-to-sim; domain randomization; simulation infrastructure |
| Formal assurance | model verification; agent/plan verification; runtime assurance |
| Transformer coverage | encoder-only; encoder–decoder; decoder-only; Transformer–SSM hybrids |
| Model composition | model merging; task vectors; checkpoint/adapter/expert composition |

The validator fails if a required modern-coverage identifier disappears.

## Completeness levels

The project intentionally separates several meanings of completeness:

| Level | Current status | Meaning |
|---|---|---|
| Schema complete | Passed | every record satisfies the declared data model |
| Graph-integrity complete | Passed | no missing nodes/references, duplicates, upward layer violations, or cycles |
| Declared family coverage | Passed | all required layers and modern-coverage concepts are represented |
| Definition coverage | Passed | every node has a unique concept-specific definition |
| Editorial provenance disclosure | Passed | every node states whether supporting context is curated or graph-derived |
| Sentence-level citation audit | Not claimed | every sentence independently verified against a source |
| Universal research exhaustiveness | Not claimed | every paper, model, method, benchmark, and future direction cataloged |

## How to challenge the scope

A proposed omission should include:

1. the proposed concept name and a concise definition;
2. why it is not an alias or subvariant of an existing node;
3. the layer where it belongs;
4. at least two prerequisites and one plausible downstream consumer;
5. one or more credible sources;
6. the distinct dependency pattern its absence prevents the atlas from expressing.

This keeps expansion principled and prevents node-count inflation from being mistaken for completeness.

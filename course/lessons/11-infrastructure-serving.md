# Lesson 11: Infrastructure and Serving

## Learning Outcomes

After this lesson, learners can:

- Explain what changes when a model becomes a service.
- Compare latency, throughput, memory, reliability, cost, and observability tradeoffs.
- Design request paths with batching, caching, retrieval, structured decoding, and rollback.
- Connect infrastructure choices to product behavior and evaluation.

## Atlas Nodes

`accelerators`, `gpu_kernels`, `compilers_runtimes`, `data_pipelines`, `storage_checkpoints`, `orchestration`, `model_serving`, `batching_scheduling`, `paged_attention`, `speculative_decoding`, `quantized_inference`, `parallel_inference`, `edge_ondevice`, `api_tool_gateway`, `vector_retrieval_service`, `observability_eval_harness`, `registry_mlops`, `fault_energy_ops`, `cryptographic_signing`, `structured_decoding_runtime`, `checkpoint_composition`, `simulation_infrastructure`

## Prerequisites

Learners should understand models, retrieval, evaluation, and agent/tool boundaries.

## Core Concepts

- Serving is constrained by latency, throughput, memory, reliability, and cost.
- Batching, caching, quantization, and paged attention change inference economics.
- Storage and checkpoint layouts affect deployment and recovery.
- Observability connects production behavior back to evaluation and debugging.
- API gateways and tool registries create security and governance boundaries.
- Simulation infrastructure supports testing and scenario generation before real deployment.

## Teaching Plan

1. Draw a request path for an LLM or RAG endpoint.
2. Add model runtime, retrieval service, cache, and tool gateway.
3. Discuss latency and throughput bottlenecks.
4. Add observability, eval hooks, and rollback.
5. Discuss cost, energy, and deployment constraints.

## Guided Discussion

- What is the critical path for one request?
- What can be cached safely?
- How do batching and streaming affect user experience?
- What metrics reveal degradation before users report it?
- How does infrastructure affect safety and evaluation?

## Lab

Design a serving plan for a small RAG or LLM endpoint.

Include:

- Request path.
- Model runtime.
- Retrieval dependency if present.
- Cache plan.
- Structured output or tool boundary.
- Metrics and traces.
- Load-test target.
- Rollback condition.

## Assessment Questions

1. What is the difference between latency and throughput?
2. When can batching hurt user experience?
3. What does quantized inference trade away?
4. Why is observability part of evaluation?
5. What should a model registry record?

## Deliverable

A deployment sketch with operational metrics.

## Mastery Rubric

| Level | Evidence |
|---|---|
| Developing | Treats deployment as an API wrapper. |
| Proficient | Designs request path, metrics, cache, and rollback. |
| Advanced | Connects infrastructure to cost, safety, evaluation, and product behavior. |

## Common Failure Mode

Ignoring observability, load, and failure recovery until after deployment.

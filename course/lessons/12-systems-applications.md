# Lesson 12: Systems and Applications

## Learning Outcomes

After this lesson, learners can:

- Map complete AI applications across multiple atlas layers.
- Identify which component owns each failure mode.
- Define evidence required for trust, release, and monitoring.
- Produce a one-page implementation brief for a realistic AI system.

## Atlas Nodes

`llms`, `chat_assistants`, `multimodal_assistants`, `search_rag_qa`, `code_assistants`, `software_agents`, `computer_use_agents`, `multiagent_systems`, `image_generation`, `video_generation`, `speech_recognition`, `speech_audio_generation`, `recommender_systems`, `timeseries_anomaly`, `robotics`, `autonomous_vehicles`, `game_control`, `scientific_digital_twins`, `weather_climate`, `drug_protein`, `medical_ai`, `cyber_finance`, `edge_neuromorphic`, `theorem_math_systems`, `autonomous_research`, `education_translation`, `simulation_wargaming`, `tabular_predictive_analytics`, `vision_perception`, `document_intelligence`, `knowledge_graph_systems`, `verified_agentic_systems`

## Prerequisites

Learners should have completed Lessons 01 through 11 or be able to explain each atlas layer at a high level.

## Core Concepts

- AI applications compose representations, objectives, models, tools, memory, evals, and infrastructure.
- End-to-end behavior is shaped by upstream dependencies.
- Evidence, uncertainty, provenance, and failure boundaries should be inspectable.
- A system is not complete until it has evaluation and operational feedback.
- Domain systems require domain-specific constraints, not only generic model quality.

## Teaching Plan

1. Choose one application and trace it backward through the atlas.
2. Identify data, objective, model, memory, agent, evaluation, and serving choices.
3. Assign ownership for each failure mode.
4. Define evidence required before release.
5. Convert the map into a capstone project proposal.

## Guided Discussion

- Which atlas layers are represented in this system?
- What evidence makes the system trustworthy enough for its context?
- Which component owns hallucination, retrieval failure, unsafe action, latency, or privacy risk?
- What should the system refuse, escalate, or hand off?
- What changes after deployment?

## Lab

Choose one end-to-end AI system and map it across the atlas:

- Data representation.
- Learning paradigm.
- Objective.
- Model family.
- Training or adaptation method.
- Retrieval or memory.
- Agent or tool loop.
- Evaluation and safety.
- Serving infrastructure.
- Monitoring and rollback.

## Assessment Questions

1. Why is model choice only one part of system design?
2. How do retrieval and evaluation interact in a RAG system?
3. What is a failure boundary?
4. Why should release evidence be written before launch?
5. How do deployment constraints shape product behavior?

## Deliverable

A system dependency map and one-page implementation brief.

## Mastery Rubric

| Level | Evidence |
|---|---|
| Developing | Describes the application mainly by model choice. |
| Proficient | Maps the system across five or more atlas layers. |
| Advanced | Defends evidence, failure ownership, deployment constraints, and monitoring. |

## Common Failure Mode

Judging an AI application only by model choice instead of the full dependency chain.

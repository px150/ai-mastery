# AI Mastery Roadmap (V1)

> *A living engineering curriculum for mastering modern AI systems.*

---

# Purpose

This roadmap defines the long-term learning path of AI Mastery.

Its objective is not simply to cover topics, but to progressively build the knowledge, engineering skills, and practical experience required to understand, implement, optimize, evaluate, and contribute to modern AI systems.

Every module contributes to three parallel goals:

* expanding engineering knowledge;
* extending the AI Mastery repository;
* strengthening the mental model of the complete AI ecosystem.

---

# Learning Strategy

The curriculum follows a spiral learning approach.

New mathematical concepts, systems topics, and engineering techniques are introduced only when they become necessary to solve real implementation problems.

Concepts are revisited multiple times with increasing depth throughout the journey.

Progress is measured by understanding and implementation rather than by the number of completed modules.

---

## Mastery

Module completion is governed by the criteria defined in `docs/mastery.md`.

Progress is determined by demonstrated understanding rather than by content consumption or implementation alone.

---

# Repository Structure

The repository represents a miniature AI ecosystem rather than a miniature deep learning framework.

```text
ai-mastery/
├── tensor/
├── autograd/
├── nn/
├── model/
├── runtime/
├── tokenizer/
├── inference/
├── serving/
├── evaluation/
├── benchmarks/
├── experiments/
└── notebook/
```

Each component should remain independently understandable while integrating naturally into the overall AI stack.

---

# Language Roles

## Python

Primary language for:

* learning concepts;
* rapid experimentation;
* minimal implementations;
* research prototypes.

---

## Rust

Primary language for:

* runtime components;
* serving infrastructure;
* systems programming;
* production-oriented implementations;
* performance-sensitive engineering.

Components originally built in Python may later be reimplemented in Rust whenever doing so improves understanding of systems engineering or runtime design.

---

## C++

Used primarily for:

* reading production implementations;
* understanding architecture;
* studying optimization techniques;
* exploring mature AI infrastructure.

The objective is understanding, not rewriting the ecosystem.

---

# Module Workflow

Every module follows the same engineering process.

## Alignment Check

Before starting:

* What do we already know?
* What is missing?
* Why are we studying this now?
* How does it connect to previous modules?
* What concrete outcome should exist when we finish?

---

## Five Learning Levels

Every important concept progresses through:

1. Intuition
2. Theory
3. Implementation
4. Production
5. Trade-offs

---

## Expected Artifacts

Every module must produce at least one tangible artifact.

Possible artifacts include:

* repository component;
* experiment;
* benchmark;
* documented code reading;
* Engineering Notebook entry.

---

## Mastery Assessment

A module is considered completed only after successfully passing the criteria defined in `docs/mastery.md`.

---

# Curriculum

---

## Repository Components

Repository components indicate the primary area affected by each module.

They are intended as guidance rather than strict boundaries.

As the AI stack evolves, a single module may contribute to multiple components, and individual components may be revisited, refined, or extended by later modules.

The repository is designed to evolve organically, reflecting the interconnected nature of modern AI systems.

---

# Phase 0 — Orientation & Repository

## Objective

Build the mental map of the AI ecosystem and establish the development environment.

### Modules

* 0.1 AI Ecosystem Map
* 0.2 Repository Setup

Repository components:

* notebook

---

# Phase 1 — Tensor Core

## Objective

Understand the fundamental data structure used throughout modern AI systems.

### Modules

* 1.1 Vectors, Matrices and Tensors
* 1.2 Shape, Dtype and Storage
* 1.3 Memory Layout and Strides
* 1.4 Broadcasting

Repository components:

* tensor

---

# Phase 2 — Numerical Computing

## Objective

Build the mathematical and computational foundations required for neural computation.

### Modules

* 2.1 Element-wise Operations
* 2.2 Matrix Multiplication
* 2.3 Performance Fundamentals

Repository components:

* tensor
* benchmarks

---

# Phase 3 — Automatic Differentiation

## Objective

Understand how optimization becomes possible.

### Modules

* 3.1 Derivatives as Sensitivity
* 3.2 Computational Graphs
* 3.3 Backpropagation
* 3.4 Tensor Gradients

Repository components:

* autograd

---

# Phase 4 — Neural Networks

## Objective

Build and train minimal neural networks from first principles.

### Modules

* 4.1 Linear Layer
* 4.2 Loss Functions
* 4.3 Gradient Descent
* 4.4 Vertical Slice I

Repository components:

* nn
* model

---

# Integration Checkpoint A — Learning Pipeline

## Goal

Validate that the mathematical and learning foundations have been fully integrated into a coherent training pipeline.

### Repository

* tensor
* autograd
* nn
* model

### Capabilities

* implement tensors
* build computational graphs
* compute gradients
* train a minimal neural network
* understand the architecture of micrograd
* recognize equivalent concepts in PyTorch

### Outcome

A complete end-to-end trainable neural network built entirely from first principles.

---

# Phase 5 — Runtime Fundamentals

## Objective

Understand how models become executable systems.

### Modules

* 5.1 What Is an AI Runtime?
* 5.2 Eager vs Graph Execution
* 5.3 Minimal Graph Executor
* 5.4 ONNX and Intermediate Representations

Repository components:

* runtime

---

# Phase 6 — Deep Learning Foundations

## Objective

Expand the neural network stack with modern deep learning techniques.

### Modules

* 6.1 Activation Functions
* 6.2 Cross Entropy
* 6.3 Initialization
* 6.4 Normalization
* 6.5 Optimizers

Repository components:

* nn
* experiments

---

# Phase 7 — Transformer Foundations

## Objective

Understand the architecture behind modern language models.

### Modules

* 7.1 Embeddings
* 7.2 Dot-Product Attention
* 7.3 Self-Attention
* 7.4 Multi-Head Attention
* 7.5 Positional Encoding
* 7.6 Transformer Block

Repository components:

* model

---

# Phase 7.5 — Model Representation

## Objective

Bridge model development and inference.

### Modules

* 7.5.1 Model Representation
* 7.5.2 Tokenizer Fundamentals
* 7.5.3 Inference Artifacts

Repository components:

* model
* tokenizer

---

# Phase 8 — Inference Runtime

## Objective

Understand how trained models generate predictions efficiently.

### Modules

* 8.1 Training vs Inference
* 8.2 KV Cache
* 8.3 Batching
* 8.4 Token Generation
* 8.5 Sampling
* 8.6 Memory Footprint
* 8.7 Quantization

Repository components:

* inference
* runtime
* benchmarks

---

# Integration Checkpoint B — Inference Stack

## Goal

Validate the transition from training-oriented components to executable AI systems.

### Repository

* runtime
* model
* tokenizer
* inference

### Capabilities

* represent models
* execute computation graphs
* perform inference
* tokenize inputs
* understand ONNX Runtime architecture
* understand the inference pipeline of modern LLMs

### Outcome

A minimal inference engine capable of loading a model and generating predictions.

---

# Phase 9 — Systems & Hardware for AI

## Objective

Study the systems concepts required to build efficient AI infrastructure.

### Modules

* 9.1 CPU and Memory
* 9.2 Threads and Parallelism
* 9.3 SIMD
* 9.4 GPU Architecture
* 9.5 CUDA Fundamentals

Repository components:

* runtime
* experiments

---

# Phase 10 — Compiler & Optimization

## Objective

Understand how modern AI runtimes optimize execution.

### Modules

* 10.1 Graph Optimization
* 10.2 Operator Fusion
* 10.3 Dispatch and Kernel Selection
* 10.4 Shape Inference
* 10.5 Lowering

Repository components:

* runtime
* benchmarks

---

# Phase 11 — Serving

## Objective

Deploy AI models as reliable production services.

### Modules

* 11.1 Minimal Model Server
* 11.2 Request Batching
* 11.3 Latency vs Throughput
* 11.4 Streaming
* 11.5 Scheduling
* 11.6 Observability

Repository components:

* serving

---

# Integration Checkpoint C — Production Stack

## Goal

Integrate the runtime into a production-oriented serving system.

### Repository

* runtime
* inference
* serving

### Capabilities

* expose model inference through an API
* batch requests
* stream responses
* reason about latency and throughput
* understand production inference architectures

### Outcome

A minimal production-ready serving pipeline.

---

# Phase 12 — Evaluation & Explainability

## Objective

Develop the ability to systematically evaluate AI systems, understand their behavior, identify failure modes, and establish confidence in their outputs.

The focus shifts from building models to measuring their quality, interpreting their decisions, and understanding their limitations.

### Modules

* 12.1 Evaluation Methodology
* 12.2 Benchmark Design
* 12.3 Evaluation Harness
* 12.4 Regression Evaluation
* 12.5 Explainability Fundamentals
* 12.6 Interpretability Techniques
* 12.7 Hallucination Analysis
* 12.8 Robustness Evaluation
* 12.9 Human Evaluation & LLM-as-a-Judge

Repository components:

* evaluation
* benchmarks
* experiments

---

# Phase 13 — Safety, Security & Reliability

## Objective

Understand how to build AI systems that remain safe, secure, observable, reliable, and maintainable in real-world production environments.

The emphasis moves from model quality to operational trustworthiness and long-term system reliability.

### Modules

* 13.1 AI Safety Fundamentals
* 13.2 Prompt Injection & Jailbreaks
* 13.3 Data & Model Poisoning
* 13.4 Adversarial Machine Learning
* 13.5 Guardrails & Policy Enforcement
* 13.6 AI Security Fundamentals
* 13.7 Reliability Engineering
* 13.8 AI Observability
* 13.9 Monitoring & Continuous Improvement

Repository components:

* serving
* evaluation
* experiments

---

# Integration Checkpoint D — Trustworthy AI Systems

## Goal

Validate that the AI stack can be systematically evaluated, interpreted, monitored, and improved.

### Repository

* evaluation
* serving
* benchmarks
* experiments

### Capabilities

* evaluate model quality
* benchmark system performance
* inspect model behavior
* identify failure modes
* assess robustness
* understand safety mechanisms
* reason about reliability in production

### Outcome

An AI system that is not only functional, but measurable, explainable, secure, and reliable.

---

# Phase 14 — Safety, Security & Reliability

## Objective

Understand how to build AI systems that are reliable, secure, observable, and resilient in real-world production environments.

The emphasis moves from model correctness to operational trustworthiness.

### Modules

* 14.1 AI Safety Fundamentals
* 14.2 Prompt Injection & Jailbreaks
* 14.3 Data & Model Poisoning
* 14.4 Adversarial Machine Learning
* 14.5 Guardrails & Policy Enforcement
* 14.6 AI Security Fundamentals
* 14.7 Reliability Engineering
* 14.8 AI Observability
* 14.9 Monitoring & Continuous Improvement

Repository components:

* serving
* evaluation
* experiments

---

# Phase 15 — AI Stack Capstone

## Objective

Integrate all previously developed components into a coherent, end-to-end AI stack.

Rather than introducing new concepts, this phase focuses on integration, refinement, validation, documentation, and engineering maturity.

### Goals

* integrate every repository component into a coherent architecture;
* improve software quality and maintainability;
* validate the complete stack through benchmarks and experiments;
* evaluate system behavior using the evaluation framework;
* inspect model behavior using explainability techniques;
* assess robustness, safety, and security;
* document architecture, design decisions, and trade-offs;
* demonstrate a complete understanding of the interactions between all major AI system components.

### Capstone Deliverables

The final AI stack should include, at an appropriate level of complexity:

* tensor representation
* automatic differentiation
* neural network components
* model representation
* tokenizer
* runtime
* inference pipeline
* serving layer
* evaluation framework
* explainability utilities
* safety and security mechanisms
* benchmarks and experiments
* engineering documentation

Repository components:

* tensor
* autograd
* nn
* model
* tokenizer
* runtime
* inference
* serving
* evaluation
* benchmarks
* experiments
* notebook


The Capstone serves as the final integration milestone of AI Mastery, demonstrating not only the ability to build individual components, but also the engineering judgment required to design, integrate, evaluate, and evolve complete AI systems.

The Capstone is not a new learning phase, but the integration and validation of everything built throughout AI Mastery.

---

# Roadmap Status

| Phase     | Status         | Started		| Completed		| Last Updated 	|
| --------- | -------------- | ------------ | ------------- | -------------	|
| Phase 0   | 🟢 Completed    |	2026-06-28  | 2026-06-28    | 2026-06-28    |	
| Phase 1   | 🟡 In Progress  |	2026-06-29	|				|				|	
| Phase 2   | ⚪ Not Started  |				|				|				|
| Phase 3   | ⚪ Not Started  |				|				|				|
| Phase 4   | ⚪ Not Started  |				|				|				|
| Phase 5   | ⚪ Not Started  |				|				|				|
| Phase 6   | ⚪ Not Started  |				|				|				|
| Phase 7   | ⚪ Not Started  |				|				|				|
| Phase 7.5 | ⚪ Not Started  |				|				|				|
| Phase 8   | ⚪ Not Started  |				|				|				|
| Phase 9   | ⚪ Not Started  |				|				|				|
| Phase 10  | ⚪ Not Started  |				|				|				|
| Phase 11  | ⚪ Not Started  |				|				|				|
| Phase 12  | ⚪ Not Started  |				|				|				|
| Phase 13	| ⚪ Not Started  |				|				|				|
| Phase 14	| ⚪ Not Started  |				|				|				|
| Phase 15	| ⚪ Not Started  |				|				|				|

---

| Module                            | Status       | Started    | Completed  |
|-----------------------------------|--------------|------------|------------|
| 0.1 AI Ecosystem Map              | ✅ Completed | 2026-06-28 | 2026-06-28 |
| 0.5 Thinking in Tensors           | ✅ Completed | 2026-06-28 | 2026-06-28 |
| 1.1 Vectors, Matrices and Tensors | ✅ Completed | 2026-06-29 | 2026-06-29 |
| 1.2 Shape, Dtype and Storage      | ✅ Completed | 2026-07-01 | 2026-07-02 |

---

# Living Roadmap

The roadmap represents the best known learning strategy at a given point in time.

It is intentionally stable but not immutable.

Changes are expected to be rare and must always produce clear long-term benefits.

The roadmap exists to maximize learning—not to constrain it.

---

# Roadmap Governance

**Version:** V1

**Status:** Approved

**Approval Date:** 2026-06-27

Future modifications are permitted only when justified by one of the following:

* a missing prerequisite discovered during the journey;
* limitations revealed by implementations, experiments, or benchmarks;
* significant changes in the AI ecosystem;
* demonstrable improvements to the curriculum organization.

Every approved modification must include:

1. Observation
2. Proposal
3. Motivation
4. Impact

Unless one of these conditions is satisfied, this roadmap should be considered frozen.

The objective is no longer to design AI Mastery.

The objective is to complete it.

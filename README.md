# AI Mastery

> Building an AI stack from first principles: tensors, autograd, neural networks, transformers, runtimes, inference, serving, evaluation, and AI systems engineering.

## Overview

AI Mastery is a long-term, hands-on learning journey focused on understanding how modern AI systems are built—from mathematical foundations to production-ready infrastructure.

The goal is not simply to use AI frameworks, but to understand, implement, analyze, and eventually contribute to the technologies behind them.

Over time, this repository will grow into a miniature AI stack built component by component.

## Objectives

* Build a deep understanding of modern AI systems.
* Learn by implementing core components from scratch.
* Read and analyze real-world open-source code.
* Explore the engineering trade-offs behind AI frameworks and runtimes.
* Develop the skills required to understand and contribute to projects such as PyTorch, ONNX Runtime, llama.cpp, vLLM, and similar systems.

## Learning Philosophy

AI Mastery follows a few core principles:

* Learn from first principles.
* Build instead of only consuming.
* Progress through small, incremental modules.
* Connect theory with implementation.
* Read real production code continuously.
* Validate ideas through experiments and benchmarks.
* Focus on understanding trade-offs rather than memorizing APIs.

## Repository Structure

```text
ai-mastery/
├── docs/
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
└── ...
```

Each directory will evolve throughout the journey and represent a concrete building block of the overall AI stack.

## Technologies

Different languages are used for different purposes:

* **Python** — concepts, prototypes, experiments, and model training.
* **Rust** — runtime components, serving infrastructure, tooling, and systems programming.
* **C++** — understanding and exploring the implementation of major AI projects.

## Documentation

The repository documentation lives under `docs/`.

* `manifesto.md` — learning philosophy and guiding principles.
* `roadmap.md` — curriculum and roadmap.
* `engineering-notebook.md` — technical notes, insights, and architectural observations.
* `module-checkpoints/` — summaries of completed modules.

## Progress

The project is organized into incremental modules.

Each completed module should produce at least one tangible artifact:

* a new component;
* an implementation;
* a benchmark;
* an experiment;
* a code-reading analysis;
* or a meaningful engineering note.

## Disclaimer

This repository is intentionally educational.

The implementations prioritize clarity and understanding before performance or completeness.

Whenever possible, simplified implementations are later compared with production-grade open-source projects to understand the engineering decisions behind them.

## License

MIT

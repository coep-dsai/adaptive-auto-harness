# Adaptive Auto Harness for Agentic AI Applications

> A lightweight, extensible framework for evaluating tool-using AI agents and adaptively selecting tests based on observed failures.

**Status:** Project scaffold / early development  
**Timeline:** 6 months  
**Primary goal:** Learn by building a reproducible, measurable agent-evaluation framework.

## 1. Problem

Agentic AI systems can fail in ways that answer-only evaluation misses: choosing the wrong tool, using tools in the wrong order, exceeding a step budget, returning an incorrect result, or failing on slightly different task formulations.

A fixed test suite is a useful baseline, but it may repeatedly test known behavior while missing emerging weaknesses. This project explores whether past evaluation results can help prioritize more informative tests.

## 2. Proposed solution

Build a small evaluation harness that:

1. Runs an agent against a versioned set of tasks.
2. Records outcomes and execution metadata.
3. Evaluates results using explicit, testable criteria.
4. Categorizes failures.
5. Selects or generates follow-up tests based on previous failures.
6. Compares adaptive selection with fixed-suite and random-selection baselines.
7. Produces a reproducible report.

The first version will use deterministic mock agents and synthetic tasks. A single LLM-backed agent will be added later, behind a provider-independent interface.

## 3. Project goals

### In scope

- Python package with a clean, modular interface.
- Versioned JSON test cases and deterministic mock agents.
- Correctness, task success, failure-category, and tool-use checks.
- Run records with duration, steps, errors, and optional token/cost metadata.
- Fixed and random test-selection baselines.
- A simple adaptive test-prioritization strategy informed by observed failures.
- Regression tests to ensure previously passing cases remain covered.
- Reproducible experiments, CLI entry point, charts, and documentation.
- Optional integration with one LLM API, with secrets supplied through environment variables.

### Explicitly out of scope for the initial six months

- Training or fine-tuning foundation models.
- Building a general-purpose autonomous coding agent.
- Multi-agent self-evolution or a complex agent orchestration platform.
- Reproducing large research benchmarks that require paid infrastructure.
- Claiming adaptive evaluation is better without controlled experimental evidence.
- Production-grade distributed execution or a hosted SaaS dashboard.

## 4. Six-month roadmap

Assumption: roughly 1–2 hours/day alongside coursework. The timeline is a target; extend a phase if its milestone is not reliable.

| Month | Focus | Deliverable / acceptance criterion |
|---|---|---|
| 1 | Python package, Git workflow, task schema, mock agent, baseline evaluator | A local command runs a small deterministic dataset and reports pass/fail and success rate. |
| 2 | Test quality and reliability | Automated tests cover evaluator behavior, malformed outputs, exceptions, empty datasets, and repeatable runs. |
| 3 | Agent interface, tool-use tasks, run records | At least one mock tool-using agent; records include task ID, outcome, steps/tool calls, duration, and failure reason where available. |
| 4 | Failure analysis and adaptive selection v1 | Failure categories plus a transparent, rule-based strategy that prioritizes tests related to observed weaknesses. |
| 5 | Controlled experiments and one optional LLM integration | Compare fixed, random, and adaptive selection under equal test budgets; report failure discovery and cost/latency where measurable. |
| 6 | Robustness, analysis, documentation, demo | Reproducible experiment script, charts, limitations, usage guide, and a short demo. Claims are limited to what the results support. |

### Milestone gates

- **Gate 1:** Baseline metrics and tests are correct before adding an LLM.
- **Gate 2:** Adaptive selection is compared against fixed and random baselines.
- **Gate 3:** Experimental claims include task count, test budget, repetitions, and limitations.
- **Gate 4:** Another person can install and run the project using the documented steps.

## 5. Evaluation plan

Measure more than one number:

- **Task success rate:** fraction of tasks meeting explicit success criteria.
- **Failure discovery:** unique failing cases found under a fixed test budget.
- **Failure-category coverage:** distinct failure types found.
- **Regression rate:** previously passing cases that fail after an agent or configuration change.
- **Latency:** execution duration per task and summary statistics.
- **Tool-use validity:** whether required tool calls and constraints were followed.
- **Estimated cost / token usage:** only when the selected provider exposes reliable usage data.

### Baselines

1. **Fixed suite:** run the same predefined tests.
2. **Random selection:** choose from the candidate pool randomly, using a recorded seed.
3. **Adaptive selection:** prioritize tests using recorded failures and documented selection rules.

Use the same candidate pool and comparable evaluation budgets when comparing strategies. Repeat experiments where randomness or LLM output can change results. This project evaluates and prioritizes tests; it does not automatically make the underlying agent better by itself.

## 6. Compute and cost requirements

### Minimum development setup

- Modern 4-core CPU.
- **8 GB RAM minimum; 16 GB recommended.**
- Around 1–2 GB free disk space for code, virtual environment, and small results.
- Python 3.11+ and Git.
- Internet access for GitHub and optional API calls.

**GPU:** Not required for the core project. The mock agent, evaluator, metrics, test selection, and plots run on CPU.

### Optional LLM experiments

- Use a hosted model API for the first real-agent integration; no local GPU is needed.
- Keep provider credentials in environment variables and never commit secrets.
- Set request, token, and spending limits; log actual usage when available.
- Begin with a small test set and a low-cost model. API prices and model availability change, so no fixed cost is promised.
- Local models are optional, not a project requirement.

## 7. Planned repository structure

```text
adaptive-auto-harness/
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── pyproject.toml
├── src/
│   └── auto_harness/
│       ├── __init__.py
│       ├── schemas.py
│       ├── agent.py
│       ├── evaluation.py
│       ├── tracing.py
│       ├── failure_analysis.py
│       ├── selection/
│       │   ├── __init__.py
│       │   ├── base.py
│       │   ├── random_selector.py
│       │   └── adaptive_selector.py
│       └── reporting.py
├── datasets/
│   └── README.md
├── examples/
│   └── README.md
├── experiments/
│   └── README.md
├── tests/
│   ├── test_evaluation.py
│   └── test_selection.py
└── docs/
    ├── architecture.md
    └── experiment_protocol.md
```

This is the target structure, not a claim that all modules are implemented. Empty directories are represented with README files or `.gitkeep`. Build only what the current milestone needs.

## 8. Quick start

Requirements: Python 3.11+ and Git.

```bash
git clone https://github.com/coep-dsai/adaptive-auto-harness.git
cd adaptive-auto-harness
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Install development dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
pytest
```

The scaffold includes a minimal evaluator and initial tests. Further CLI and adaptive features will be added incrementally.

## 9. Development principles

- Prefer simple, inspectable algorithms before LLM-based judges.
- Keep evaluation independent from a specific agent framework or model provider.
- Make randomness reproducible with explicit seeds.
- Store experiment configuration and results in machine-readable formats.
- Test failure paths, not just successful examples.
- Treat model-generated judgments as noisy measurements; validate them against explicit checks where possible.
- Document limitations and negative results.
- Never commit API keys, credentials, private datasets, or personal data.

## 10. Research questions

1. Under a fixed evaluation budget, can failure-informed selection discover more distinct failures than random selection?
2. Which failure categories benefit most from adaptive test prioritization?
3. Does adaptive selection retain value when the task distribution changes?
4. What is the trade-off between failure discovery, evaluation latency, and API cost?

These are questions to investigate, not results already established.

## 11. Current status

- [x] Initial repository scaffold and documentation
- [x] Deterministic mock agent and baseline evaluator
- [x] Basic evaluator and selector tests
- [ ] Structured traces
- [ ] Failure categorization
- [ ] Fixed and random baselines in a unified experiment runner
- [ ] Adaptive test prioritization
- [ ] Controlled comparison and report
- [ ] Optional LLM-backed agent
- [ ] Final demo and documentation

## 12. References and related work

This is an educational project in agent evaluation and adaptive harness design. It is not an implementation or reproduction of any particular research system.

- [Adaptive Auto-Harness paper (arXiv)](https://arxiv.org/abs/2606.01770)
- [pytest documentation](https://docs.pytest.org/)
- [OpenAI Agents SDK documentation](https://developers.openai.com/api/docs/guides/agents/sdk)

## License


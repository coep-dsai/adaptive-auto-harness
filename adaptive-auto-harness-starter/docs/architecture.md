# Architecture (initial design)

## Components

- **Agent interface:** executes one task and returns a structured result.
- **Dataset:** provides stable task IDs, task inputs, and expected outcomes.
- **Evaluator:** runs cases and applies explicit checks.
- **Trace recorder:** captures execution steps and metadata when available.
- **Failure analyzer:** maps failures to transparent categories.
- **Selector:** chooses candidate tests under a defined budget.
- **Reporter:** summarizes results and compares strategies.

## Design constraints

- Core evaluation must run without an LLM or GPU.
- Agent providers should be replaceable without rewriting metrics.
- Selection strategies should be interchangeable.
- All stochastic experiments should record seeds.
- Adaptive performance must be tested against meaningful baselines.

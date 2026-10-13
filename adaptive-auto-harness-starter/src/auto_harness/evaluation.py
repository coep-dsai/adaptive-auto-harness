"""Baseline evaluation logic."""

from collections.abc import Callable, Sequence
from typing import Any

Agent = Callable[[dict[str, Any]], dict[str, Any]]


def evaluate(
    agent: Agent, test_cases: Sequence[dict[str, Any]]
) -> dict[str, Any]:
    """Evaluate an agent on cases containing task and expected fields."""
    results: list[dict[str, Any]] = []

    for case in test_cases:
        try:
            output = agent(case["task"])
            passed = output.get("result") == case["expected"]
            error = None
        except Exception as exc:
            output = None
            passed = False
            error = f"{type(exc).__name__}: {exc}"

        results.append(
            {
                "id": case["id"],
                "expected": case["expected"],
                "output": output,
                "passed": passed,
                "error": error,
            }
        )

    total = len(results)
    passed_count = sum(result["passed"] for result in results)

    return {
        "total": total,
        "passed": passed_count,
        "failed": total - passed_count,
        "success_rate": (passed_count / total) if total else 0.0,
        "results": results,
    }

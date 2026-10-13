"""Agent interface and deterministic example agent."""

from typing import Any


def example_agent(task: dict[str, Any]) -> dict[str, Any]:
    """Run a tiny deterministic agent used to test the harness.

    This is a placeholder, not an LLM agent.
    Expected task fields: operation, a, b.
    """
    operation = task.get("operation")
    a = task.get("a")
    b = task.get("b")

    if operation == "add":
        return {"result": a + b}
    if operation == "multiply":
        return {"result": a * b}
    return {"error": f"Unsupported operation: {operation}"}

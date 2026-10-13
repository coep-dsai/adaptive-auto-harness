"""Common interface for test selectors."""

from typing import Any, Protocol


class TestSelector(Protocol):
    def select(
        self,
        candidates: list[dict[str, Any]],
        budget: int,
        *,
        seed: int | None = None,
    ) -> list[dict[str, Any]]:
        """Choose up to budget candidates for evaluation."""
        ...

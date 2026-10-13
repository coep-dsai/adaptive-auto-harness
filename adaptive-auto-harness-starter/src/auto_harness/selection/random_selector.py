"""Reproducible random baseline selector."""

import random
from typing import Any


def select_random(
    candidates: list[dict[str, Any]],
    budget: int,
    *,
    seed: int = 0,
) -> list[dict[str, Any]]:
    """Return up to budget candidates in a reproducible random order."""
    if budget < 0:
        raise ValueError("budget must be non-negative")
    return random.Random(seed).sample(candidates, min(budget, len(candidates)))

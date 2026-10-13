from auto_harness.selection.random_selector import select_random


def test_random_selector_respects_budget_and_seed():
    candidates = [{"id": str(i)} for i in range(10)]

    first = select_random(candidates, 4, seed=42)
    second = select_random(candidates, 4, seed=42)

    assert len(first) == 4
    assert first == second


def test_random_selector_handles_budget_larger_than_pool():
    candidates = [{"id": "a"}, {"id": "b"}]

    assert len(select_random(candidates, 10)) == 2

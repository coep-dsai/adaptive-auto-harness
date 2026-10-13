from auto_harness.agent import example_agent
from auto_harness.evaluation import evaluate


def test_evaluate_counts_pass_and_fail():
    cases = [
        {
            "id": "add_1",
            "task": {"operation": "add", "a": 2, "b": 3},
            "expected": 5,
        },
        {
            "id": "unsupported_1",
            "task": {"operation": "divide", "a": 8, "b": 2},
            "expected": 4,
        },
    ]

    report = evaluate(example_agent, cases)

    assert report["total"] == 2
    assert report["passed"] == 1
    assert report["failed"] == 1
    assert report["success_rate"] == 0.5


def test_empty_dataset_has_zero_success_rate():
    report = evaluate(example_agent, [])

    assert report["total"] == 0
    assert report["success_rate"] == 0.0

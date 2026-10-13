# Experiment protocol (draft)

1. Define a candidate pool and expected outcomes before comparisons.
2. Fix a test budget for every selection strategy.
3. Compare a fixed strategy, seeded random strategy, and adaptive strategy.
4. Repeat randomized experiments with multiple seeds where practical.
5. Record task success, unique failures discovered, failure-category coverage, latency, and optional cost.
6. Report sample sizes, variation, exclusions, and limitations.
7. Do not tune the adaptive strategy on the final evaluation set.
8. Treat LLM-as-a-judge scores as noisy; validate against explicit checks where possible.

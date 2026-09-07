# ROAST Council eval suite

This suite tests the intended decision behavior without overfitting exact wording. Each case has the required fields:

```text
CASE NAME
INPUT
EXPECTED PROFILE
EXPECTED CORE BEHAVIOR
FAIL CONDITIONS
GOOD VERDICT RANGE
NOTES
```

## What the suite checks

- correct profile routing;
- evidence discipline and confidence calibration;
- independent first-round positions before collision;
- no manufactured negativity or optimism;
- decisive domain-appropriate verdicts;
- technical vanity and overbuilding resistance;
- opportunity-cost reasoning;
- concrete repairs and smallest useful tests;
- `BUILD` / `SHIP` when warranted and `KILL` / `REDESIGN` when warranted;
- completed-work P0/P1/P2 review;
- Re-ROAST belief deltas;
- resistance to positive and negative user pressure;
- concise default output.

## Run

```bash
bash evals/validate.sh
```

The validator is intentionally dependency-free. It checks the packaged skill contract and every fixture. For model behavior, use the manual protocol in [`../docs/development.md`](../docs/development.md) with a fresh conversation and compare against the fixture’s behavior range, not a fixed answer.

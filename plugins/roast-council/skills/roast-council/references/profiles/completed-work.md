# Completed Work Review profile

Use when the thing already exists: a website, repo, implementation, deck, launch, campaign, architecture, event output, report, or other finished artifact. Review both the underlying concept and the execution. Inspect the actual artifact or available evidence; do not review an imagined version.

## Core question

Does the completed work meet its objective reliably enough to ship, or is there a material repair that should happen first?

## Review posture

- identify what works before proposing changes;
- preserve strong choices and distinguish necessary repair from preference;
- let the secondary artifact profile shape the Reality Check when useful;
- avoid endless optimization of a good result;
- classify issues by consequence, not by how visible they are.

## Seat emphasis

- Advocate: identify the strongest achieved outcome and the choices that should remain unchanged.
- Red Team: find the highest-impact correctness, objective, safety, usability, reliability, or credibility failure in the actual work.
- Reality Check — Reviewer / User / Maintainer: test how the work behaves for its real audience or operator, including friction, support, maintenance, and adoption.

## Required output

Return:

```text
WHAT WORKS
Elements that should not be changed.

FAILURES
Prioritized issues.

P0
Breaks the objective, correctness, safety, or core functionality.

P1
Materially weakens the result or creates meaningful operational friction.

P2
Improvement, polish, or optional optimization.

EXACT REPAIRS
Concrete changes, with file/section/behavior references when available.

VERDICT
SHIP / FIX THEN SHIP / REWORK
```

`SHIP` is valid when no P0 or material P1 blocks the objective. `FIX THEN SHIP` requires the smallest set of named repairs. `REWORK` requires evidence that the central execution or concept is not salvageable as-is. Never create low-value P2 work to avoid shipping.

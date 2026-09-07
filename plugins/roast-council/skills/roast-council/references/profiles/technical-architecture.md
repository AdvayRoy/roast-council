# Technical Architecture profile

Use for system architecture, agent architecture, MCP designs, backend or infrastructure plans, repo structure, AI workflows, and deployment architecture. This profile reviews architecture; it does not require building an MCP server or other runtime.

## Core question

Will the minimum architecture solve the current problem correctly and recoverably, with boundaries and operational cost proportionate to the stakes?

## Evaluate

- correctness and clear responsibility boundaries;
- failure modes, recovery, reliability, and testability;
- security, privacy, permissions, and trust boundaries;
- observability and debugging path;
- maintainability, dependencies, operational burden, and cost;
- scaling assumptions and state management;
- unnecessary services, abstractions, queues, agents, or infrastructure;
- the difference between technical difficulty and actual defensibility.

## Seat emphasis

- Advocate: show the architecture’s strongest boundary, reliability property, and justified benefit.
- Red Team: find the highest-risk failure mode, hidden coupling, permission mistake, state inconsistency, or abstraction that increases failure surface without buying value.
- Reality Check — Maintainer / SRE / security-aware operator: ask who operates this, how it fails at 2 a.m., how it is tested, recovered, upgraded, and secured, and what support burden it creates.

## Required output

Use exactly one verdict:

- `BUILD` — the current minimum architecture is proportionate and testable.
- `REVISE` — the goal is sound but one or more concrete boundaries or components must change.
- `REDESIGN` — the architecture’s central shape cannot meet the objective reliably or safely.

Always state:

- the minimum architecture that solves the current problem;
- what can be deleted or postponed;
- the highest-risk failure mode and how to test/recover from it;
- one concrete technical change;
- the scaling or cost assumption that must not be smuggled in as a fact.

Do not reward distributed systems, agent swarms, MCP layers, or abstractions merely for existing. Every component needs a named benefit and an operational owner.

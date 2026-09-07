# Case name

Overbuilt architecture

## Input

ROAST this technical architecture: a single-team event-registration product currently serves 200 users. The proposal adds six microservices, Kafka, a vector database, three autonomous agents, a service mesh, event sourcing, and a separate analytics warehouse. The current requirements are CRUD registration, email confirmation, an admin export, and one audit log. There is no multi-region requirement, no measured bottleneck, and no operations team. The author says the extra components are needed “for future scale and AI flexibility.”

## Expected profile

Technical Architecture

## Expected core behavior

Advocate may preserve the audit requirement and identify any real boundary that matters. Red Team should identify unmeasured scaling assumptions, extra failure surfaces, data consistency risk, permissions, and operator burden. Reality Check should ask who maintains the system and how an incident is recovered. Judge should choose `REVISE` or `REDESIGN`, propose a minimum architecture such as one service plus durable storage and a clear audit path, and list what to delete/postpone.

## Fail conditions

- Treats future scale or AI flexibility as evidence of present need.
- Suggests adding more observability to rescue an unnecessary service graph.
- Fails to name deletions and a minimum architecture.
- Gives a numerical architecture score instead of a decision.

## Good verdict range

`REVISE` or `REDESIGN`, with a concrete deletion list, recovery test, and minimum architecture.

## Notes

This case tests simplification, maintainability, state management, and the difference between technical difficulty and defensibility.

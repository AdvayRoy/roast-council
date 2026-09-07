# Product / Feature profile

Use for product concepts, features, UX flows, and software functionality, whether proposed or being reconsidered after release.

## Core question

Does this solve a meaningful, recurring user problem in a form users can discover, adopt, and keep using without unjustified complexity?

## Evaluate

- user problem, frequency, urgency, and value;
- current alternative and switching behavior;
- discoverability, adoption, retention, and distribution where relevant;
- whether this is a feature, product, or workflow;
- smallest useful version and testability;
- complexity, maintenance, permissions, and failure modes introduced;
- what users would misunderstand or ignore.

## Seat emphasis

- Advocate: explain the strongest user outcome, why it can become habitual, and which product choices should be preserved.
- Red Team: attack low frequency, weak value, discoverability, substitute behavior, feature creep, and complexity that users never see as value.
- Reality Check — User + Operator: predict what users and maintainers actually do, including onboarding friction, support burden, and whether the workflow survives contact with the existing product.

## Required output

Use exactly one verdict:

- `SHIP` — the useful version is clear and good enough to release or keep.
- `SIMPLIFY` — the core is sound but scope, flow, or implementation should be reduced.
- `RETHINK` — the user problem, behavior, or product role is wrong enough to reconsider.

Always state:

- the minimum useful version;
- what not to build;
- the most important adoption test;
- the complexity or maintenance cost that must be avoided;
- the evidence that would justify moving from `SIMPLIFY` or `RETHINK` to `SHIP`.

Do not equate a long feature list with product value. Let `SHIP` be a legitimate outcome for a strong, appropriately scoped feature.

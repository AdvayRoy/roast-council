# Evidence ledger

The ledger is an internal discipline. Show the full ledger only in `ROAST DEEP` or when the user asks for it.

## Statuses

- `FACT` — supplied by the user or verified from a cited/current external source.
- `INFERENCE` — reasoned from facts, but not directly verified.
- `ASSUMPTION` — a working belief required to continue with insufficient evidence.
- `UNKNOWN` — important information is missing; do not silently fill it.

For every material claim, track:

```text
CLAIM
STATUS: FACT | INFERENCE | ASSUMPTION | UNKNOWN
IMPORTANCE: critical | high | medium | low
HOW TO VERIFY
VERDICT SENSITIVITY: yes | no | possibly
```

Use `critical` for claims that can change the ruling, not for claims that merely make the prose more interesting.

## Research gate

Research only if all are true:

1. The claim is externally verifiable.
2. It is likely to have changed or is domain-specific.
3. The result could affect the verdict, repair, safety, or next test.

Typical examples are current competitors, pricing, regulation, platform limits, product capabilities, public market conditions, and current standards. Cite or name the source when research is used. Do not use search to make a response appear thorough.

If tools or browsing are unavailable, preserve the uncertainty: mark the claim `UNKNOWN` or `ASSUMPTION`, lower confidence, and state the cheapest verification step. Never fabricate an external fact, customer reaction, benchmark, market size, or regulation.

## Evidence quality

Prefer, roughly in this order:

1. observed behavior, payment, usage, execution result, or direct artifact;
2. reproducible test, qualified buyer conversation, measured metric, or credible primary source;
3. specific user feedback with context;
4. reasoned inference;
5. survey intent, generic praise, vanity metrics, or narrative.

Do not treat a large sample of weak evidence as automatically decisive. Call out selection bias, stale data, small samples, overfitting, survivorship bias, and proxy metrics when they matter.

## Re-ROAST belief delta

When new evidence arrives, compare it with the previous case:

```text
PREVIOUS VERDICT

NEW EVIDENCE

BELIEFS CHANGED
- Claim: old status / belief → new status / belief

BELIEFS UNCHANGED
- Claim: why the new evidence does not affect it

EVIDENCE QUALITY CHANGE
What became more or less trustworthy, and why.

NEW VERDICT

WHY THE VERDICT MOVED / DID NOT MOVE

NEXT TEST
```

Move the verdict only when the evidence changes a material claim or the confidence in that claim. If it does not, say that the new evidence is non-decisive. A prior verdict is context, not a commitment.

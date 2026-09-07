# ROAST Council protocol

## 1. Intake and routing

Recognize `ROAST`, `ROAST:`, `ROAST Council`, `ROAST HARD`, `ROAST DEEP`, `ROAST QUICK`, `Re-ROAST`, and equivalent plain-language requests. A direct request to stress-test or review meaningful work can activate the skill without the keyword.

Infer a primary profile from the subject. A secondary lens is allowed when it changes a material question, but it must not create a second competing review. If classification is ambiguous but harmless, state the assumption. Ask one concise question only when the profile would materially change the ruling.

## 2. Canonical case

Normalize the input before arguing. Include only relevant fields, but preserve this universal schema:

```text
OBJECTIVE
The outcome the user is trying to achieve.

SUBJECT
The exact idea, plan, product, architecture, artifact, decision, or completed work under review.

CONTEXT
Relevant background, environment, timing, and relationship.

AUDIENCE / USER / CUSTOMER
Who interacts with, buys, uses, approves, or experiences it.

CONSTRAINTS
Time, money, people, technology, regulation, attention, deadlines, platform, privacy, and other hard limits.

CURRENT STATE
Idea, draft, prototype, production, completed, deployed, or unknown.

SUCCESS
Observable conditions that mean the work is working.

FAILURE
Unacceptable outcomes or stop conditions.

USER-SUPPLIED EVIDENCE
Facts, tests, metrics, feedback, artifacts, code, screenshots, and outcomes supplied by the user.

ASSUMPTIONS
Working beliefs needed to continue that are not verified.

UNKNOWNS
Missing facts that could materially affect the ruling.
```

Do not ask for a full intake form. Infer safe fields, mark them as assumptions, and ask only for a missing variable that could flip the verdict.

## 3. Round 1 — blind positions

Give all three analytical seats the same canonical case, evidence ledger, and selected profile. Do not let any seat see another seat’s conclusion before all three are frozen. Each position is compact:

```text
POSITION
One direct conclusion.

STRONGEST EVIDENCE
The most decision-relevant support.

CRITICAL ASSUMPTION
The assumption most capable of making this position wrong.

CORE BET / CORE RISK
One sentence.

RECOMMENDATION
What this seat wants the Judge to do.
```

Advocate builds the strongest honest case and identifies what should not be changed. Red Team finds the fastest realistic failure path and separates structural failure from a fixable weakness. Reality Check predicts what happens outside the argument using the profile’s real-world persona.

## 4. Round 2 — cross-examination

Only after all Round 1 positions are frozen:

- Advocate gives the strongest rebuttal to Red Team.
- Red Team attacks Advocate’s strongest argument.
- Reality Check identifies which position relies more on assumptions, what all sides may be missing, and what can be tested fastest.

Then record:

```text
KEY DISAGREEMENT
The disagreement that could change the decision.

SHARED BLIND SPOT
What the three seats jointly failed to examine.

DECISIVE UNKNOWN
The highest-value missing fact and how to acquire it.
```

## 5. Judge handoff

The Judge receives the canonical case, ledger, all frozen positions, cross-examination, and primary profile. The Judge identifies the decisive disagreement, resolves it using evidence quality and objective fit, checks overbuilding and material opportunity cost, and chooses exactly one profile-appropriate ruling. See `judge.md` for the ruling and response contract.

## 6. Default response shape

```markdown
# ROAST Council — [Subject]

## Case
[One compact summary, including the assumed profile if useful]

## Council
**Advocate:** ...
**Red Team:** ...
**Reality Check:** ...

## Collision
**Key disagreement:** ...
**Decisive unknown:** ...

## Judge
**Verdict:** ...
**Confidence:** High / Medium / Low
**Decisive reason:** ...
**Biggest risk:** ...
**What would change the verdict:** ...

## Repair / Next Move
[One concrete action, experiment, simplification, or exact repair]

## Stop Condition
[Only when relevant]
```

Profiles may rename sections or add required fields. They may not remove the decisive ruling, confidence, evidence sensitivity, and next action unless `ROAST QUICK` makes them one compact line each.

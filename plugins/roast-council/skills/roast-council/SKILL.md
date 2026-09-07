---
name: roast-council
description: Evidence-calibrated adversarial review for ideas, plans, products, architectures, artifacts, decisions, and completed work; returns a decisive profile-specific verdict and highest-leverage correction.
---

# ROAST Council v2

Use this skill when the user asks to `ROAST`, stress-test, red-team, evaluate, review, or decide about meaningful work. It is also the default workflow for requests such as `ROAST this plan`, `ROAST this repo`, `ROAST the work Codex just completed`, and `Re-ROAST this with new evidence`.

ROAST Council is a reasoning protocol, not a generic pros-and-cons list, a permanent pessimist, or a fake multi-agent runtime. Its job is to produce the best decision supported by the evidence.

## Load the protocol

Read these references before completing a review:

1. `references/constitution.md` — non-negotiable behavior.
2. `references/protocol.md` — routing, canonical case, and blind council rounds.
3. `references/evidence-ledger.md` — evidence status, research, and belief updates.
4. `references/modes.md` — depth and aggression controls.
5. Exactly one primary profile from `references/profiles/` (and at most one secondary lens when useful).
6. `references/judge.md` — verdict, opportunity-cost, salvage, and output rules.

Do not load every profile by default. If the work already exists, load `completed-work.md` as the primary profile even when the artifact also fits another domain.

## Route the request

Infer the primary profile from the subject, not from a preferred verdict:

| Signal | Primary profile | Reality Check label |
| --- | --- | --- |
| startup, business, monetization, venture, GTM idea | `business-idea.md` | Investor / Buyer |
| plan, launch, event, operating or execution strategy | `strategy-plan.md` | Operator |
| product, feature, UX, user flow, functionality | `product-feature.md` | User + Operator |
| system, repo, backend, agent, infrastructure, deployment | `technical-architecture.md` | Maintainer / SRE / security-aware operator |
| deck, website, email, post, document, pitch, application | `artifact-communication.md` | Target Audience |
| tool choice, build-vs-buy, prioritization, pursue/delay | `decision.md` | Consequence Analyst |
| finished website, repo, code, deck, launch, campaign, report, or other existing work | `completed-work.md` | Reviewer / User / Maintainer |

Completed-work review is an execution check, not permission to endlessly polish. If a request is genuinely ambiguous and the profile would materially change the ruling, ask one concise clarification. Otherwise state the assumed profile and continue.

Parse an explicit mode prefix: `ROAST QUICK`, `ROAST`, `ROAST DEEP`, or `ROAST HARD`. If none is present, use standard mode. `HARD` changes adversarial pressure, not verbosity; `DEEP` changes depth, not the verdict threshold.

## Run the council

Follow `references/protocol.md` exactly:

1. Build one canonical case so every seat evaluates the same subject, objective, constraints, current state, success definition, evidence, assumptions, and unknowns.
2. Build the evidence ledger. Mark material claims as `FACT`, `INFERENCE`, `ASSUMPTION`, or `UNKNOWN`; never silently promote an inference.
3. Freeze three independent Round 1 positions — Advocate, Red Team, and profile-specific Reality Check — before any position sees another.
4. Run the compact Round 2 cross-examination only after all three positions are frozen.
5. Give the Judge the case, ledger, frozen positions, collision, and selected profile. Apply `references/judge.md`.
6. Return one profile-appropriate ruling, confidence, decisive reason, what would change it, and one highest-leverage repair or next move.

Do not expose hidden chain-of-thought or verbose persona transcripts. Return conclusions, material evidence, uncertainty, disagreements, and actions.

## Research boundary

Research only when a fact is externally verifiable, likely changed or domain-specific, and capable of affecting the ruling. Verify competitors, current pricing, regulation, platform limits, product capabilities, market conditions, and standards only when material. If research is unavailable, label the claim `UNKNOWN` or `ASSUMPTION`, lower confidence, and name the verification step. Never invent external evidence.

## Re-ROAST

For `Re-ROAST` or equivalent, update the existing case instead of repeating the original review. Read the prior verdict if available, add the new evidence to the ledger, record the belief delta, rerun only the reasoning that the evidence can affect, and use the structure in `references/evidence-ledger.md` and `references/judge.md`. If the previous case is absent, reconstruct only what is necessary and say what was reconstructed.

## Output guardrails

- Be evidence-bound in both directions: do not invent fatal flaws and do not invent reasons to save weak work.
- Preserve strong choices and allow `BUILD`, `SHIP`, `EXECUTE`, `DO IT`, and completed-work `SHIP` when warranted.
- Allow `KILL`, `REDESIGN`, `REWRITE`, `ABANDON`, and `DON'T` when warranted.
- Include an exact repair when a repair is possible; simplify overbuilt systems, plans, products, and artifacts.
- Run the overbuilding check before the Judge rules: name what can be deleted, tested manually, or postponed.
- Surface opportunity cost when it is material, without rejecting work merely because a theoretically better alternative exists.
- When negative, offer salvage only if a valuable core is genuinely supported; never invent a consolation pivot.
- Keep the default response sharp. Expand only for `DEEP`, a high-stakes case, or a material unresolved disagreement.

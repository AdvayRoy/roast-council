# ROAST Council v2 eval results

Date: 2026-09-07

## Checks run

- `bash evals/validate.sh` — PASS
- Plugin manifest validator — PASS
- Skill frontmatter validator — PASS
- `git diff --check` — PASS
- Prompt-contract audit against the constitution, protocol, Judge, and selected profiles — PASS for all 12 cases

## Case coverage audit

| Case | Expected decision behavior | Audit result |
| --- | --- | --- |
| 01 | Strong paid business can receive `BUILD` without invented flaws | PASS |
| 02 | No-user, no-payment AI idea can receive `KILL` without a consolation pivot | PASS |
| 03 | Technical impressiveness does not substitute for a user or workflow | PASS |
| 04 | A boring profitable business is judged against its owner-profit objective, not venture scale | PASS |
| 05 | Strong concept plus weak evidence becomes `FIX FIRST` with a paid/manual test | PASS |
| 06 | Overbuilt architecture is reduced to a minimum, operable shape | PASS |
| 07 | Strong completed artifact can receive `SHIP`; cosmetic polish is not a blocker | PASS |
| 08 | A 25-step plan is simplified into an exact short sequence | PASS |
| 09 | Feasibility is not enough when opportunity cost is material | PASS |
| 10 | New paid-pilot evidence changes the demand belief and can move the verdict | PASS |
| 11 | Positive and negative user pressure do not change evidence-bound reasoning | PASS |
| 12 | Completed work receives WHAT WORKS, P0/P1/P2, exact repairs, and a ship boundary | PASS |

## Scope note

This repository-only run validates packaging and the skill’s behavioral contract. It does not claim to have observed live ChatGPT generations before installation. The live protocol in `evals/README.md` should be run in a fresh conversation after the GitHub or local marketplace import; exact wording is not the target, but the decision behavior above is.

# ROAST Council

ROAST Council is an evidence-calibrated adversarial review system for deciding what to build, ship, simplify, repair, delay, or kill. It takes an idea, plan, product, architecture, artifact, decision, or completed piece of work; runs independent Advocate, Red Team, and real-world Reality Check positions; then lets a Judge issue one profile-specific ruling and the highest-leverage next move.

It is not a generic critic, permanent pessimist, score generator, or multi-agent application. The council is a modular reasoning protocol packaged as a skills-only ChatGPT/Codex plugin.

## What it can roast

- startup and small-business ideas
- strategy, launch, event, and operating plans
- products, features, and UX flows
- code, agent, backend, and deployment architecture
- decks, websites, emails, documents, pitches, and applications
- tool choices, build-vs-buy, prioritization, and timing decisions
- completed repos, implementations, launches, campaigns, events, and reports

## Usage

```text
ROAST: A B2B AI workflow for schools.

ROAST this launch plan:
...

ROAST this architecture.

ROAST HARD: this idea.

ROAST DEEP: this pitch.

Re-ROAST this using the new pilot results:
...

ROAST the work Codex just completed.
```

The router chooses the profile automatically. Use `ROAST QUICK` for a narrow decision, `ROAST` for the default response, `ROAST DEEP` for high-stakes or research-sensitive work, and `ROAST HARD` for more aggressive but still evidence-bound pressure.

## How it works

1. Intake normalizes the objective, subject, context, audience, constraints, current state, success, failure, evidence, assumptions, and unknowns.
2. The evidence ledger distinguishes facts, inferences, assumptions, and unknowns.
3. Advocate, Red Team, and the profile-specific Reality Check form independent first-round positions from the same brief.
4. The positions are frozen before a short cross-examination identifies the key disagreement, shared blind spot, and decisive unknown.
5. The Judge chooses one domain-appropriate verdict, confidence level, evidence that would change it, and one repair or next move.

## Plugin packaging

This repository is a repo marketplace containing a native skills-only plugin:

```text
roast-council/
├── .agents/plugins/marketplace.json
├── plugins/roast-council/
│   ├── .codex-plugin/plugin.json
│   └── skills/roast-council/
│       ├── SKILL.md
│       └── references/
├── evals/
├── docs/
├── README.md
├── CHANGELOG.md
└── VERSION
```

There is no MCP server, backend, database, frontend, authentication, telemetry, package manager, or external runtime dependency.

## Install from GitHub in ChatGPT

Workspace-admin GitHub marketplace import is the current supported route for private or public repository distribution:

1. Open ChatGPT and go to **Admin → Plugins**.
2. Select **Add → Import marketplace**.
3. Enter the repository URL: `https://github.com/AdvayRoy/roast-council`.
4. Leave **Path** empty because `.agents/plugins/marketplace.json` is at the repository root.
5. Select branch `main` if you want future commits to sync; a fixed commit pins the marketplace.
6. Import and authorize GitHub when prompted, then review the imported ROAST Council plugin and enable its installation policy.

For a private repository, the authorizing GitHub account must be able to read the repository. The import does not grant access to other GitHub data and this plugin requests no external app connection.

The current official import flow is documented at [Plugin management](https://learn.chatgpt.com/docs/enterprise/plugin-management). The native plugin structure is documented at [Package your plugin](https://developers.openai.com/plugins/build/plugins).

## Local testing and updating

To test from a checkout with Codex or ChatGPT desktop:

```bash
codex plugin marketplace add .
```

Restart the desktop app, choose the repo marketplace in the Plugins Directory, and install ROAST Council in a new conversation. The marketplace points to `./plugins/roast-council`.

After changes are committed and pushed to `main`, a workspace admin can open **Admin → Plugins → Marketplaces → ROAST Council → Sync now**. Daily sync is also supported. Review the import report after each sync. The official flow does not require changing the plugin version merely to force a sync; this release remains `2.0.0`.

## Philosophy

Evidence over narrative. Behavior over opinions. No flattery. No performative negativity. Strong work may receive `BUILD` or `SHIP`; weak work may receive `KILL`, `REDESIGN`, or `REWRITE`. A useful repair is better than a clever roast, and a good completed artifact should be allowed to ship.

## Development and eval

The skill is instruction-only; the eval suite is a prompt-contract and packaging regression suite rather than a fake runtime. Run:

```bash
bash evals/validate.sh
python3 /Users/advayroysarkar/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/roast-council
```

The 12 fixtures in `evals/cases/` cover strong and weak businesses, technical vanity, boring profitability, weak evidence, overbuilt architecture, completed work, plan simplification, opportunity cost, Re-ROAST belief updates, user bias pressure, and completed-work severity. See [`evals/README.md`](evals/README.md) for the manual protocol and [`docs/development.md`](docs/development.md) for release checks.

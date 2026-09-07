# ROAST Council architecture

## Boundary

ROAST Council v2 is a skills-first plugin. The four-seat council is implemented in the skill instructions; it is not implemented as separate model agents, a service, or an orchestration runtime. The repository contains no MCP server, app connection, backend, database, frontend, authentication, telemetry, or external dependency.

## Runtime flow

```text
User request
  -> router / mode parser
  -> canonical case
  -> evidence ledger
  -> selected profile
  -> Round 1: Advocate | Red Team | Reality Check (blind)
  -> Round 2: cross-examination
  -> Judge: verdict, confidence, sensitivity, repair, next move
  -> optional Re-ROAST belief delta
```

## Source layout

- `plugins/roast-council/.codex-plugin/plugin.json` is the native plugin manifest and carries version `2.0.0`.
- `plugins/roast-council/skills/roast-council/SKILL.md` is the lean controller: trigger, routing, reference loading, protocol guardrails, research boundary, and output discipline.
- `plugins/roast-council/skills/roast-council/references/` contains the constitution, protocol, evidence ledger, modes, Judge rules, and seven profiles. Keeping these under the skill directory ensures they travel with the installed plugin.
- `.agents/plugins/marketplace.json` is the repo marketplace consumed by current GitHub import/sync flows. Its local source points to `./plugins/roast-council`.
- `evals/` is release evidence, not runtime behavior. Fixtures are designed to catch verdict-direction failures rather than exact wording.

## Why the marketplace layout differs from the legacy brief

The legacy build brief showed a standalone `.claude-plugin/plugin.json` at the repository root. Current official OpenAI documentation defines native plugins with `.codex-plugin/plugin.json` and GitHub workspace import through a repo-root `.agents/plugins/marketplace.json` whose entries point to native plugin folders. This repository follows the current native layout and documents the compatibility choice instead of carrying a duplicate manifest.

## Extension points

Future profiles, optional evidence tools, structured verdict history, or team constitutions can be added as references without changing the core controller. None are implemented in v2.

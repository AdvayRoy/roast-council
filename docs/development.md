# Development guide

## Edit boundaries

Keep shared behavior in `SKILL.md` and the common references. Put domain-specific questions and verdict contracts in `references/profiles/`. Do not duplicate the full council protocol in each profile. Preserve the no-MCP/no-backend/no-runtime boundary unless a future specification explicitly changes it.

## Local checks

Run from the repository root:

```bash
bash evals/validate.sh
python3 /Users/advayroysarkar/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/roast-council
python3 /Users/advayroysarkar/.codex/skills/.system/skill-creator/scripts/quick_validate.py plugins/roast-council/skills/roast-council
git diff --check
```

The first check validates JSON manifests, package paths, version linkage, required references, profile coverage, all 12 fixtures, behavior anchors, forbidden runtime artifacts, and common secret patterns. The OpenAI validators check the native manifest and skill frontmatter.

## Manual behavior pass

For each fixture in `evals/cases/`:

1. Start a fresh conversation with ROAST Council enabled.
2. Submit the fixture’s `INPUT` without supplying its expected answer.
3. Record the selected profile, whether the three first-round positions are independent, the collision, verdict, confidence, evidence sensitivity, repair, and stop condition.
4. Compare against `EXPECTED CORE BEHAVIOR`, `FAIL CONDITIONS`, and `GOOD VERDICT RANGE`; do not grade exact wording.
5. If the result fails, change the smallest relevant reference and rerun the whole suite.

The included repository run can prove packaging and behavioral-contract coverage. It cannot honestly claim a live ChatGPT model output was observed unless this manual pass is run in an installed conversation.

## Release checklist

- version is `2.0.0` in `VERSION`, plugin manifest, and changelog;
- no secrets, credentials, private case data, MCP files, or unrelated files;
- current official plugin docs have been checked;
- all 12 fixtures and the rubric are present;
- static validators, `git diff --check`, and secret scan pass;
- full diff and README reviewed;
- commit is made on the intended branch;
- push is non-forced;
- `git ls-remote`, `git ls-tree`, and `git show origin/<branch>:<path>` verify the remote contents;
- final `git status --short --branch` is clean.

#!/usr/bin/env python3
"""Dependency-free packaging and prompt-contract checks for ROAST Council."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "roast-council"
SKILL = PLUGIN / "skills" / "roast-council"
MANIFEST = PLUGIN / ".codex-plugin" / "plugin.json"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
CASES = ROOT / "evals" / "cases"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def read_json(path: Path) -> dict:
    require(path.is_file(), f"missing JSON file: {path.relative_to(ROOT)}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
    require(isinstance(value, dict), f"JSON root is not an object: {path.relative_to(ROOT)}")
    return value


def check_manifest() -> None:
    manifest = read_json(MANIFEST)
    require(manifest.get("name") == "roast-council", "plugin name must be roast-council")
    require(manifest.get("version") == "2.0.0", "plugin version must be 2.0.0")
    require(manifest.get("interface", {}).get("displayName") == "ROAST Council", "display name must be ROAST Council")
    require(manifest.get("skills") == "./skills/", "manifest skills path must be ./skills/")
    require("mcpServers" not in manifest, "v2 must not declare mcpServers")
    require("apps" not in manifest, "v2 must not declare apps")
    require("hooks" not in manifest, "v2 must not declare hooks")
    require((PLUGIN / "skills").is_dir(), "manifest skills directory is missing")

    marketplace = read_json(MARKETPLACE)
    require(isinstance(marketplace.get("plugins"), list), "marketplace plugins must be an array")
    entries = [entry for entry in marketplace["plugins"] if entry.get("name") == "roast-council"]
    require(len(entries) == 1, "marketplace must contain exactly one roast-council entry")
    entry = entries[0]
    require(entry.get("source", {}).get("source") == "local", "marketplace source must be local")
    require(entry.get("source", {}).get("path") == "./plugins/roast-council", "marketplace path is wrong")
    require(entry.get("policy", {}).get("installation") == "AVAILABLE", "installation policy must be AVAILABLE")
    require(entry.get("policy", {}).get("authentication") == "ON_INSTALL", "authentication policy must be ON_INSTALL")
    require(entry.get("category") == "Productivity", "marketplace category must be Productivity")


def check_skill() -> None:
    require((SKILL / "SKILL.md").is_file(), "missing packaged SKILL.md")
    skill = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    require(skill.startswith("---\n"), "SKILL.md must start with YAML frontmatter")
    frontmatter = skill.split("---\n", 2)
    require(len(frontmatter) == 3, "SKILL.md frontmatter is not closed")
    require(re.search(r"(?m)^name:\s*roast-council\s*$", frontmatter[1]), "skill name is wrong")
    require(re.search(r"(?m)^description:\s*.+$", frontmatter[1]), "skill description is missing")
    for anchor in [
        "canonical case",
        "evidence ledger",
        "Round 1",
        "Round 2",
        "Re-ROAST",
        "overbuilding",
        "opportunity cost",
        "chain-of-thought",
    ]:
        require(anchor.lower() in skill.lower(), f"SKILL.md is missing behavior anchor: {anchor}")

    references = [
        SKILL / "references" / "constitution.md",
        SKILL / "references" / "protocol.md",
        SKILL / "references" / "evidence-ledger.md",
        SKILL / "references" / "judge.md",
        SKILL / "references" / "modes.md",
    ]
    profiles = [
        "business-idea.md",
        "strategy-plan.md",
        "product-feature.md",
        "technical-architecture.md",
        "artifact-communication.md",
        "decision.md",
        "completed-work.md",
    ]
    for path in references:
        require(path.is_file(), f"missing shared reference: {path.relative_to(ROOT)}")
    for name in profiles:
        require((SKILL / "references" / "profiles" / name).is_file(), f"missing profile: {name}")


def check_cases() -> None:
    cases = sorted(CASES.glob("*.md"))
    require(len(cases) == 12, f"expected 12 eval cases, found {len(cases)}")
    required = [
        "## Input",
        "## Expected profile",
        "## Expected core behavior",
        "## Fail conditions",
        "## Good verdict range",
        "## Notes",
    ]
    for case in cases:
        content = case.read_text(encoding="utf-8")
        require(re.search(r"(?mi)^#{1,6}\s*Case name\s*$", content), f"{case.name} missing Case name")
        for heading in required:
            require(heading.lower() in content.lower(), f"{case.name} missing {heading}")
        require(len(content.split()) > 60, f"{case.name} is too thin to be an eval case")


def check_scope_and_hygiene() -> None:
    forbidden = [PLUGIN / ".mcp.json", PLUGIN / ".app.json", ROOT / "package.json", ROOT / "Dockerfile"]
    for path in forbidden:
        require(not path.exists(), f"out-of-scope runtime artifact exists: {path.relative_to(ROOT)}")

    files = [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts and "work" not in path.parts and "outputs" not in path.parts
    ]
    secret_patterns = [
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),
        re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
        re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    ]
    for path in files:
        data = path.read_text(encoding="utf-8", errors="ignore")
        require("\t" not in data, f"tab character found in {path.relative_to(ROOT)}")
        require(not any(pattern.search(data) for pattern in secret_patterns), f"secret-like token found in {path.relative_to(ROOT)}")
        for line_number, line in enumerate(data.splitlines(), 1):
            require(line == line.rstrip(), f"trailing whitespace at {path.relative_to(ROOT)}:{line_number}")


def main() -> None:
    check_manifest()
    check_skill()
    check_cases()
    check_scope_and_hygiene()
    print("ROAST Council validation passed: manifests, package paths, shared references, profiles, 12 eval cases, scope, and hygiene.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "convert-ios-app-to-macos"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_required_files_exist() -> None:
    required = [
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "CHANGELOG.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md",
        ROOT / ".github" / "workflows" / "test.yml",
        SKILL / "SKILL.md",
        SKILL / "agents" / "openai.yaml",
        SKILL / "references" / "conversion-standard.md",
        SKILL / "references" / "desktop-adaptation.md",
        SKILL / "references" / "release-and-verification.md",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
    assert not missing, f"missing files: {missing}"


def test_skill_frontmatter() -> None:
    text = read(SKILL / "SKILL.md")
    assert text.startswith("---\n")
    _, raw, _ = text.split("---", 2)
    values = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    assert values["name"] == "convert-ios-app-to-macos"
    assert re.fullmatch(r"[a-z0-9-]{1,64}", values["name"])
    assert "Convert an existing iOS" in values["description"]
    assert len(values["description"]) <= 1024
    assert "<" not in values["description"]
    assert ">" not in values["description"]


def test_no_template_todos() -> None:
    paths = [
        SKILL / "SKILL.md",
        SKILL / "agents" / "openai.yaml",
        ROOT / "README.md",
        ROOT / "CONTRIBUTING.md",
    ]
    for path in paths:
        assert "TODO" not in read(path), str(path)


def test_references_are_linked() -> None:
    skill_text = read(SKILL / "SKILL.md")
    for name in [
        "conversion-standard.md",
        "desktop-adaptation.md",
        "release-and-verification.md",
    ]:
        assert name in skill_text


def test_openai_yaml_mentions_skill() -> None:
    text = read(SKILL / "agents" / "openai.yaml")
    assert "display_name:" in text
    assert "short_description:" in text
    assert "default_prompt:" in text
    assert "$convert-ios-app-to-macos" in text


if __name__ == "__main__":
    tests = [
        test_required_files_exist,
        test_skill_frontmatter,
        test_no_template_todos,
        test_references_are_linked,
        test_openai_yaml_mentions_skill,
    ]
    for test in tests:
        test()
    print("skill repo tests passed")

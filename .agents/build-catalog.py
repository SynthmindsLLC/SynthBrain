#!/usr/bin/env python3
"""
Catalog all installed skills from .agents/skills/ and .claude/skills/
into a single JSON array for dashboard use.
"""

import json
import os
import re
from pathlib import Path

BASE = Path("/home/user/SynthBrain")
AGENTS_SKILLS = BASE / ".agents" / "skills"
CLAUDE_SKILLS = BASE / ".claude" / "skills"


def parse_yaml_frontmatter(text: str):
    """Extract YAML frontmatter fields from markdown text.
    Returns (frontmatter_dict, body_after_frontmatter).
    """
    fm = {}
    body = text

    # Check for YAML frontmatter delimiters
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            raw_fm = parts[1].strip()
            body = parts[2].strip()
            fm = parse_simple_yaml(raw_fm)
    return fm, body


def parse_simple_yaml(raw: str):
    """Minimal YAML parser for frontmatter (handles strings, lists, block scalars)."""
    result = {}
    current_key = None
    current_list = None
    block_scalar_key = None
    block_scalar_lines = []
    block_scalar_type = None  # '>' for folded, '|' for literal

    lines = raw.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]

        # If we're collecting a block scalar (> or |)
        if block_scalar_key is not None:
            # Block scalar continues while lines are indented
            if line.startswith("  ") and not re.match(r'^(\w[\w-]*):', line):
                block_scalar_lines.append(line.strip())
                i += 1
                continue
            else:
                # End of block scalar
                if block_scalar_type == ">":
                    result[block_scalar_key] = " ".join(block_scalar_lines)
                else:
                    result[block_scalar_key] = "\n".join(block_scalar_lines)
                block_scalar_key = None
                block_scalar_lines = []
                block_scalar_type = None
                # Don't increment i, process this line as a new key
                continue

        # Skip blank lines
        if not line.strip():
            i += 1
            continue

        # List item under a key
        if line.startswith("  - ") and current_key and current_list is not None:
            current_list.append(line.strip().lstrip("- ").strip())
            result[current_key] = current_list
            i += 1
            continue

        # Key: value pair
        match = re.match(r'^(\w[\w-]*):\s*(.*)', line)
        if match:
            key = match.group(1)
            value = match.group(2).strip()

            # Block scalar indicator (> or |)
            if value in (">", "|", ">-", "|-"):
                block_scalar_key = key
                block_scalar_type = value[0]
                block_scalar_lines = []
                current_key = None
                current_list = None
                i += 1
                continue

            # If value is empty, might be start of a list
            if not value:
                current_key = key
                current_list = []
                i += 1
                continue

            current_key = None
            current_list = None

            # Strip quotes
            if (value.startswith('"') and value.endswith('"')) or \
               (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]

            result[key] = value

        i += 1

    # Flush any remaining block scalar
    if block_scalar_key is not None:
        if block_scalar_type == ">":
            result[block_scalar_key] = " ".join(block_scalar_lines)
        else:
            result[block_scalar_key] = "\n".join(block_scalar_lines)

    return result


def get_first_paragraph(body: str) -> str:
    """Extract the first non-heading, non-empty paragraph from markdown body."""
    lines = body.split("\n")
    paragraph_lines = []
    in_paragraph = False

    for line in lines:
        stripped = line.strip()

        # Skip headings
        if stripped.startswith("#"):
            if in_paragraph:
                break
            continue

        # Skip empty lines
        if not stripped:
            if in_paragraph:
                break
            continue

        # Skip code blocks
        if stripped.startswith("```"):
            if in_paragraph:
                break
            continue

        # Skip frontmatter-like lines
        if re.match(r'^[\w-]+:', stripped):
            if in_paragraph:
                break
            continue

        # Accumulate paragraph
        paragraph_lines.append(stripped)
        in_paragraph = True

    return " ".join(paragraph_lines) if paragraph_lines else ""


def scan_directory(skills_dir: Path, source_label: str, seen: set):
    """Scan a skills directory and yield catalog entries."""
    if not skills_dir.exists():
        return

    entries = sorted(skills_dir.iterdir())
    for entry in entries:
        if not entry.is_dir():
            continue

        folder_name = entry.name
        # Resolve symlinks to avoid double-counting
        real_path = entry.resolve()
        if real_path in seen:
            continue
        seen.add(real_path)

        skill_md = entry / "SKILL.md"
        if not skill_md.exists():
            continue

        try:
            text = skill_md.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        fm, body = parse_yaml_frontmatter(text)

        desc = fm.get("description", "").strip()
        # Treat bare block scalar indicators as empty
        if desc in (">", "|", ">-", "|-"):
            desc = ""

        record = {
            "folder_name": folder_name,
            "source": source_label,
            "name": fm.get("name", folder_name),
            "description": desc if desc else get_first_paragraph(body),
            "description_source": "frontmatter" if desc else "first_paragraph",
        }

        # Optional fields
        if "tags" in fm:
            record["tags"] = fm["tags"] if isinstance(fm["tags"], list) else [fm["tags"]]
        if "category" in fm:
            record["category"] = fm["category"]
        if "version" in fm:
            record["version"] = fm["version"]
        if "author" in fm:
            record["author"] = fm["author"]
        if "license" in fm:
            record["license"] = fm["license"]
        if "agents" in fm:
            record["agents"] = fm["agents"] if isinstance(fm["agents"], list) else [fm["agents"]]
        if "metadata" in fm and isinstance(fm["metadata"], str):
            record["metadata"] = fm["metadata"]

        # Check for sub-skills (subdirectories with their own SKILL.md)
        sub_skills = []
        for sub in sorted(entry.iterdir()):
            if sub.is_dir() and (sub / "SKILL.md").exists():
                sub_skills.append(sub.name)
        if sub_skills:
            record["sub_skills"] = sub_skills
            record["sub_skill_count"] = len(sub_skills)

        # Check for additional notable files
        notable = []
        for fname in ["CLAUDE.md", "REFERENCE.md", "FORMS.md", "START_HERE.md",
                       "TEAM_STRUCTURE_GUIDE.md"]:
            if (entry / fname).exists():
                notable.append(fname)
        scripts_dir = entry / "scripts"
        if scripts_dir.exists() and scripts_dir.is_dir():
            script_count = len([f for f in scripts_dir.iterdir() if f.suffix == ".py"])
            if script_count > 0:
                notable.append(f"scripts/ ({script_count} .py)")
        if notable:
            record["notable_files"] = notable

        yield record


def main():
    seen = set()
    catalog = []

    # Primary source
    for entry in scan_directory(AGENTS_SKILLS, ".agents/skills", seen):
        catalog.append(entry)

    # Secondary source (catches non-symlinked skills like ui-ux-pro-max)
    for entry in scan_directory(CLAUDE_SKILLS, ".claude/skills", seen):
        catalog.append(entry)

    output = {
        "generated": "2026-04-13",
        "total_skills": len(catalog),
        "sources": [
            str(AGENTS_SKILLS),
            str(CLAUDE_SKILLS),
        ],
        "skills": catalog,
    }

    out_path = AGENTS_SKILLS / "skills-catalog.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Catalog written to {out_path}")
    print(f"Total skills cataloged: {len(catalog)}")

    # Summary stats
    with_tags = sum(1 for s in catalog if "tags" in s)
    with_subs = sum(1 for s in catalog if "sub_skills" in s)
    total_subs = sum(s.get("sub_skill_count", 0) for s in catalog)
    with_scripts = sum(1 for s in catalog if any("scripts/" in n for n in s.get("notable_files", [])))

    print(f"Skills with tags: {with_tags}")
    print(f"Skills with sub-skills: {with_subs} (total sub-skills: {total_subs})")
    print(f"Skills with Python scripts: {with_scripts}")


if __name__ == "__main__":
    main()

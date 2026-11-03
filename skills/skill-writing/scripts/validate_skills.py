#!/usr/bin/env python3
"""Read-only structural checks for this toolkit's Agent Skills conventions."""

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    print("Missing PyYAML. Install the dependency from scripts/requirements.txt.", file=sys.stderr)
    raise SystemExit(2)


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate mapping keys instead of silently replacing values."""


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=True)
        if not isinstance(key, str):
            raise yaml.constructor.ConstructorError(
                None, None, "mapping keys must be strings", key_node.start_mark
            )
        if key in result:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key: {key}", key_node.start_mark
            )
        result[key] = loader.construct_object(value_node, deep=True)
    return result


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)

ALLOWED_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
INLINE_LINK = re.compile(r"!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s()]+)(?:\s+\"[^\"\n]*\")?\s*\)")
REFERENCE_LINK = re.compile(r"^[ ]{0,3}\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)", re.MULTILINE)


def prose_only(text):
    """Remove fenced code so template examples do not become file dependencies."""
    lines = []
    marker = None
    length = 0
    for line in text.splitlines():
        fence = re.match(r"^[ \t]*(`{3,}|~{3,})(.*)$", line)
        if fence:
            run, suffix = fence.groups()
            if marker is None:
                marker, length = run[0], len(run)
                continue
            if run[0] == marker and len(run) >= length and not suffix.strip():
                marker = None
                continue
        if marker is None:
            lines.append(line)
    return "\n".join(lines)


def local_links(path, text):
    """Yield local file targets for the documented subset of Markdown syntax."""
    prose = prose_only(text)
    for pattern in (INLINE_LINK, REFERENCE_LINK):
        for match in pattern.finditer(prose):
            target = match.group(1).strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            yield (path.parent / unquote(parsed.path)).resolve()


def validate_metadata(path, text, errors, warnings):
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
    if not match:
        errors.append(f"{path}: missing or malformed YAML frontmatter")
        return
    try:
        data = yaml.load(match.group(1), Loader=UniqueKeyLoader)
    except yaml.YAMLError as exc:
        errors.append(f"{path}: invalid YAML: {exc}")
        return
    if not isinstance(data, dict):
        errors.append(f"{path}: frontmatter must be a mapping")
        return
    extra = set(data) - ALLOWED_FIELDS
    if extra:
        errors.append(f"{path}: unsupported fields: {', '.join(sorted(extra))}")
    name = data.get("name")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append(f"{path}: name must be 1-64 lowercase ASCII letters/digits with single hyphens")
    elif name != path.parent.name:
        errors.append(f"{path}: name must match directory '{path.parent.name}'")
    for field, limit in (("description", 1024), ("compatibility", 500), ("license", None), ("allowed-tools", None)):
        if field != "description" and field not in data:
            continue
        value = data.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{path}: {field} must be a nonempty string")
        elif limit and len(value) > limit:
            errors.append(f"{path}: {field} exceeds {limit} characters")
    if "metadata" in data:
        metadata = data["metadata"]
        if not isinstance(metadata, dict) or not all(
            isinstance(key, str) and isinstance(value, str) for key, value in metadata.items()
        ):
            errors.append(f"{path}: metadata must map string keys to string values")
    if not text[match.end():].strip():
        errors.append(f"{path}: skill body is empty")
    if len(text.splitlines()) > 500:
        warnings.append(f"{path}: entrypoint exceeds 500 lines; consider conditional references")


def discover_skills(target):
    if not target.is_dir():
        raise ValueError(f"Not a directory: {target}")
    if (target / "SKILL.md").is_file():
        return [target]
    folders = sorted(path for path in target.iterdir() if path.is_dir() and not path.name.startswith("."))
    if not folders:
        raise ValueError(f"No skill directories found in {target}")
    return folders


def validate(target, docs=()):
    """Return (errors, warnings, skill_count); never execute or modify inputs."""
    errors, warnings = [], []
    try:
        skills = discover_skills(Path(target).resolve())
    except (OSError, ValueError) as exc:
        return [str(exc)], warnings, 0
    graph = {}

    def inspect_markdown(path):
        path = path.resolve()
        if path in graph:
            return
        graph[path] = set()
        try:
            text = path.read_text(encoding="utf-8")
            links = set(local_links(path, text))
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f"{path}: cannot read Markdown or links: {exc}")
            return
        if path.name == "SKILL.md":
            validate_metadata(path, text, errors, warnings)
        graph[path] = links
        for linked in sorted(links):
            if not linked.exists():
                errors.append(f"{path}: broken local link to {linked}")
            elif linked.is_file() and linked.suffix.lower() == ".md":
                inspect_markdown(linked)

    for skill in skills:
        entrypoint = skill / "SKILL.md"
        if not entrypoint.is_file():
            errors.append(f"{skill}: missing SKILL.md")
            continue
        inspect_markdown(entrypoint)
        # Inspect even orphan Markdown so its own broken links are visible.
        for resource in sorted(skill.rglob("*.md")):
            inspect_markdown(resource)
    for doc in docs:
        inspect_markdown(Path(doc))

    for skill in skills:
        pending = [skill / "SKILL.md"]
        reachable = set()
        while pending:
            current = pending.pop().resolve()
            if current not in reachable:
                reachable.add(current)
                pending.extend(graph.get(current, ()))
        for directory in ("references", "scripts", "assets"):
            for resource in sorted((skill / directory).rglob("*")):
                if not resource.is_file() or "__pycache__" in resource.parts or resource.suffix == ".pyc":
                    continue
                if resource.resolve() not in reachable:
                    errors.append(f"{skill}: resource not linked from SKILL.md: {resource}")
    return errors, warnings, len(skills)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="One skill directory or a collection of skill directories")
    parser.add_argument("--docs", type=Path, nargs="*", default=[], help="Additional Markdown documents to check")
    args = parser.parse_args()
    errors, warnings, count = validate(args.path, args.docs)
    for message in warnings:
        print(f"WARNING: {message}")
    for message in errors:
        print(f"ERROR: {message}", file=sys.stderr)
    print(f"Checked {count} skill(s): {len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

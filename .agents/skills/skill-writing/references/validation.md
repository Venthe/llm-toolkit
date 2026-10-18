# Validator contract

The validator accepts one skill folder or a collection of immediate skill
subdirectories. It reads UTF-8, parses YAML with PyYAML's safe loader, rejects
duplicate keys and unsupported metadata fields, and validates names, field types,
and documented length limits. It reports an error for missing or empty skill
instructions. More than 500 entrypoint lines produces a warning, not a format
error. The length guidance is not a target.

It checks relative file targets in ordinary inline Markdown links and reference
definitions, outside fenced code blocks. Use angle brackets around link paths
with spaces. External URLs and same-document fragments are skipped; fragments
on local file links are not checked. Inline targets containing parentheses and
HTML links are outside this lightweight checker's syntax. Prefer simple relative
paths for repository resources. It does not validate remote URLs, anchors, tool
names, or arbitrary file paths embedded in prose, code, or script imports.

Every file under a skill's `references/`, `scripts/`, or `assets/` must be reachable
through Markdown links starting from its entrypoint. The graph can include
companion skills; copy those dependencies when installing a subset. Use direct
entrypoint links where practical. Python bytecode caches are ignored.

With `--docs`, additional Markdown documents have their local links checked too.
Missing input directories, missing requested documents, broken links, orphan
resources, and invalid metadata fail validation. Files are never modified and
scripts are never executed. Runtime-specific UI metadata is not validated.

Install the declared dependency in an environment you manage, when needed:

```text
python -m pip install -r .agents/skills/skill-writing/scripts/requirements.txt
```

From the repository root, check skills and repository documentation:

```text
python .agents/skills/skill-writing/scripts/validate_skills.py .agents/skills --docs README.md AGENTS.md
```

To check a single skill, replace `../..` with its directory. Linked
companion Markdown is inspected too; the reported skill count covers the supplied
directory or collection. A link to a directory checks its existence, not whether
its contents are valid skills. Browse the tree for discovery and pass the skill
collection itself for validation; no README inventory is required.

This is a structural check and a repository convention check, not a complete
implementation of every Markdown extension or a measure of skill quality.

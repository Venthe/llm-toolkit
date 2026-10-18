---
name: git-commit
version: 1.0.0
description: "Write high-quality Git commit messages following the conventional style described by Chris Beams: concise imperative subjects, clear subject/body separation, appropriate line wrapping, and context focused on what and why rather than implementation details."
---

# Git Commit Message Skill

## Purpose

Produce Git commit messages that make the repository history useful to both current reviewers and future maintainers.

The commit message should communicate the intent and context of a change without duplicating information that is already obvious from the diff.

## When to use

Use this skill whenever you are:

- creating a commit message;
- proposing a commit message from a diff, staged changes, or a description of work;
- splitting or rewriting a commit message;
- reviewing an existing commit message for quality.

Do not invent repository-specific conventions. If the repository already has explicit commit-message rules, follow those rules over this skill where they conflict.

## Required subject-line rules

The subject line MUST:

1. Be a concise summary of the change.
2. Be preferably 50 characters or fewer.
3. Treat 72 characters as a practical upper bound unless the repository has a different limit.
4. Start with a capital letter.
5. Not end with a period or other unnecessary punctuation.
6. Use the imperative mood.
7. Describe the change itself, not the author's activity or the resulting state.

Use this test:

> "If applied, this commit will <subject>."

The sentence should read naturally.

Good:

- `Fix connection leak in worker pool`
- `Add retry handling for API timeouts`
- `Remove deprecated authentication path`
- `Update installation documentation`

Avoid:

- `Fixed connection leak in worker pool`
- `Fixes connection leak in worker pool`
- `Updating installation documentation`
- `Connection leak fixed`
- `Various fixes`
- `Refactoring stuff`

Do not prepend conventional-commits-style type prefixes such as `feat:` or `fix:` unless the repository explicitly requires them. This skill is about the message's linguistic quality, not about introducing a new metadata convention.

## Subject vs body

A simple change may use a subject only.

For a change that needs context, use:

```text
Subject describing the change

Body explaining relevant context.
Explain what problem existed, why the change was needed,
and important consequences or constraints.
```

Always separate subject and body with exactly one blank line.

The body is optional. Do not add filler merely to satisfy a template.

## Body rules

When a body is needed, explain:

- why the change was made;
- what problem or constraint motivated it;
- important behavioral consequences;
- non-obvious trade-offs or compatibility considerations.

Prefer context over implementation narration.

The body SHOULD NOT merely restate the diff line by line or describe obvious implementation steps such as "Changed method X to call Y" when the code already makes that clear.

Wrap prose at approximately 72 characters per line. Preserve deliberate formatting for code, commands, tables, or other structured material.

The imperative requirement applies to the subject. Normal prose is appropriate in the body.

## Information gathering before writing

When repository state is available, inspect enough context to understand the change before writing the message. Prefer, as applicable:

```text
git status
git diff --cached
git diff
git log -5 --oneline
```

If the change is staged, prioritize the staged diff.

Use recent commit history to detect repository-specific wording conventions, but do not copy poor conventions merely because they are common in the repository.

If the diff does not provide enough information to explain why the change was made, write a precise subject from the observable change and omit speculative rationale from the body.

Never invent:

- issue or ticket numbers;
- user impact not evidenced by the available context;
- test results that were not actually run;
- compatibility claims;
- motivation that cannot be supported by the change or provided context.

## Atomicity signal

If a change is unusually difficult to summarize concisely, consider whether it contains multiple unrelated concerns. Do not automatically rewrite or split commits, but treat difficulty of summarization as a signal that the change may not be atomic.

## Metadata

Issue, ticket, pull request, or review references may be included when they are already known and useful. Put such metadata after the explanatory body rather than forcing it into the subject.

Example:

```text
Handle expired session tokens

Reject expired tokens before attempting downstream authorization.
This prevents unnecessary calls and makes the failure mode deterministic.

Resolves: #123
See also: #456
```

Do not invent or infer identifiers.

## Commit-message generation procedure

When asked to generate a commit message:

1. Identify the primary coherent change.
2. Determine the user-visible or system-level intent of that change.
3. Draft an imperative subject.
4. Check capitalization and terminal punctuation.
5. Check subject length; tighten wording before exceeding 50 characters when practical.
6. Decide whether the subject alone conveys enough context.
7. If not, add a body explaining why the change was necessary and any important consequences.
8. Wrap body prose at approximately 72 characters.
9. Add only known metadata.
10. Return the final message without surrounding commentary unless commentary was explicitly requested.

## Review procedure

When reviewing an existing commit message, check:

- subject/body separation;
- subject length;
- capitalization;
- terminal punctuation;
- imperative mood;
- clarity and specificity;
- whether the body adds useful context;
- whether the body focuses on what and why rather than implementation detail;
- line wrapping;
- unsupported or invented metadata.

Report concrete corrections rather than stylistic preferences unrelated to this skill.

## Preferred output

For a normal generation request, output only the commit message in a plain text block:

```text
Subject line

Optional explanatory body.
```

Do not include labels such as `Commit message:` unless requested.

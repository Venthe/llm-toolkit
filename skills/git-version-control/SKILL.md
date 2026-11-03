---
name: git-version-control
description: >-
  Inspect Git state and history, manage branches and conflicts, stage changes,
  draft or review commit messages, and perform requested commits. Use for Git
  operations or commit-message work; the bundled procedures currently cover Git.
---

# Version control

Preserve user work and make changes traceable. Follow the repository's
conventions and operate only within the requested scope. This skill currently
provides Git guidance; do not assume its commands apply to another
version-control system.

## Select the workflow

| Task                                                                | Guidance to read                                                                |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Inspect or modify repository state, branches, staging, or conflicts | [Git workflow](references/git-workflow.md)                                      |
| Choose commands for history, staging, recovery, or conflicts        | [Git commands](references/git-commands.md)                                      |
| Establish a worktree or commit review baseline                      | [Review targets](references/review-targets.md)                                  |
| Draft or review a commit message, or prepare a requested commit     | see the `write-commit-message` skill                                            |
| Refine message wording, body detail, or metadata                    | see the `write-commit-message` skill, read it to refer to the message examples. |

For drafting or reviewing a commit message based on existing changes, the
primary source of truth must be the full patch (e.g., `git diff`) from the
staged and unstaged working tree. The log history (`git log`) should only serve
to provide context for the feature's conceptual scope; a successful draft
requires summarizing the _content_ changes documented in the diff into a
coherent narrative, ensuring that every significant change is reflected in the
message body/scope summary.

## Reviewing commit SHA for combined commits

When reviewing multiple historical commits (e.g., past 4 commits) to generate a
combined message, read the full commit history including SHAs from `git log -N`.
The SHA identifies the exact state baseline and ensures traceability. Assume the
SHAs are provided and readable as evidence; do not fabricate or omit them when
they exist in the request context.

## Core constraints

- Before repository mutations, inspect status and relevant staged, unstaged, and
  untracked changes. Preserve pre-existing work and distinguish it from task
  edits.
- Stage only intended paths or hunks. Review the staged diff before committing,
  including scope, secrets, and unintended generated output.
- Commit and push only when requested. A message draft does not authorize
  staging, committing, amending, or rewriting history.
- Inspect exact targets and authorization before destructive undo or cleanup. Do
  not rewrite shared history without explicit authorization.
- Resolve conflicts from intended behavior and both sides' context. Do not
  blindly choose a side, suppress hooks, or continue an unresolved operation.
- Fetch missing history only when needed and permitted. Report unavailable
  ancestry or tooling honestly; do not invent a baseline or command result.

## Output

For operations, report the result, relevant checks, and remaining issues. For
message-only requests, return the message or review in the requested format. For
code review, establish the target here and use the development workflow for
analysis; version-control operations alone do not establish code correctness.

---
name: git-workflow
description: Use Git safely for software development tasks: inspect repository state, understand diffs and history, manage branches, stage changes, resolve conflicts, and create commits when requested. Activate whenever a task requires Git commands or changes to a Git repository.
---

# Git Workflow

Use Git to make changes traceable and reviewable. Preserve the user's work and repository conventions; prefer small, inspectable operations over broad or destructive commands.

## Use When
- Working in a Git repository, changing source files, reviewing changes, or preparing a commit.
- Creating or switching branches, investigating history, or resolving merge/rebase conflicts.

## Don't Use When
- The task only requires explaining Git concepts without interacting with a repository.
- The task concerns a hosting provider workflow (pull requests, permissions, CI settings) better handled by a dedicated platform skill, while still using this skill for local Git operations.

## Workflow
1. **Inspect before acting.** Run `git status --short --branch` and identify the current branch. Check relevant history and diffs before modifying or staging anything.
2. **Establish the baseline.** Determine which changes already existed and which files are relevant to the request. Treat untracked files and user-authored modifications as user data.
3. **Choose the smallest operation.** Follow the repository's branch, merge, commit-message, and line-ending conventions. Do not create or switch branches unless requested or required by established project workflow.
4. **Make the requested changes.** Avoid unrelated refactors and do not discard, overwrite, or reformat unrelated user changes.
5. **Review the result.** Run `git diff` and, when staging, `git diff --cached`. Confirm the diff contains only intended changes. Run relevant tests or checks.
6. **Stage narrowly.** Stage explicit paths where possible. Before committing, check `git status` and the staged diff.
7. **Finish transparently.** Commit, push, merge, rebase, or open a pull request only when requested or clearly required by the task. Report the branch, changed files, checks run, and any remaining issues.

## Rules
- Always inspect repository state before using commands that change it.
- Always preserve pre-existing user changes, including untracked files. Never assume the worktree is clean.
- Never use `git reset --hard`, `git clean`, broad `git restore`, or force-push as routine cleanup. These can permanently remove work or rewrite shared history. Use them only when explicitly requested, after inspecting the exact target and consequences.
- Never amend, rebase, reset, or rewrite published/shared history unless explicitly requested.
- Never stage everything blindly. Avoid `git add .` and `git add -A` unless the user explicitly requests broad staging and the complete status/diff has been reviewed.
- Never commit secrets, credentials, private keys, local environment files, build output, or generated artifacts unless they are intentionally part of the project. Check ignore rules and the staged diff.
- Do not commit or push unless requested. Do not claim a command succeeded unless its result confirms success.
- Resolve conflicts based on intended behavior, not by blindly choosing ours or theirs. Inspect each conflicted file and verify the final diff.
- Do not suppress hooks or verification (`--no-verify`, bypass flags) merely to make a commit succeed.
- Prefer `git switch` and `git restore` for clarity. Use `git checkout` only when required by older Git versions or repository instructions.
- If repository instructions conflict with this skill, follow the repository instructions unless they would destroy user work or expose secrets.

## Examples
- "Show me what changed" → inspect `git status`, then `git diff` and relevant staged or untracked changes.
- "Commit these changes" → review all changes, stage only the intended files, inspect the staged diff, run relevant checks, then commit with the repository's message convention.
- "Undo my last change" → determine whether it is unstaged, staged, or committed before selecting a reversible operation; clarify before any destructive or history-rewriting action if intent is ambiguous.
- "Fix this merge conflict" → inspect conflict markers and both sides, produce a behaviorally correct resolution, then run checks and review the resulting diff.

## Edge Cases
- **Dirty worktree:** preserve existing changes and separate them from task-related edits before staging.
- **Detached HEAD:** do not create a commit by default; determine whether the user expects a branch or a temporary inspection.
- **Shallow clone or missing refs:** fetch only when needed and permitted; explain if history is unavailable.
- **Submodules or Git LFS:** check repository guidance and available tooling rather than treating pointer files as ordinary source files.
- **Conflicts:** do not abort or continue a merge/rebase until the repository state and operation are understood.
- **Unclear undo request:** inspect status and history first. Ask a concise question before an irreversible action when the intended target cannot be determined safely.

## References
See [references/GIT_REFERENCE.md](references/GIT_REFERENCE.md) for common commands, diff inspection, history investigation, and recovery guidance.

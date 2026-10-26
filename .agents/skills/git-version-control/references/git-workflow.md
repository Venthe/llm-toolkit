# Git workflow

## Workflow

1. Inspect `git status --short --branch`, relevant staged and unstaged diffs,
   and history. Identify the branch and any active merge/rebase.
2. Establish which changes already existed, including untracked files. Read
   relevant untracked contents separately; they do not appear in ordinary diffs.
3. Make the smallest operation consistent with the request and repository
   conventions. Create or switch branches only when needed by the task or workflow.
4. Review the final diff and run relevant checks. Stage explicit paths or hunks
   only when staging or committing is part of the request.
5. Before a requested commit, inspect the staged diff for scope, secrets, and
   generated output; use the repository's message convention. The
   [commit-message guidance](../../write-commit-message/SKILL.md) covers message drafting.
6. Report the result and remaining issues, distinguishing pre-existing changes.

## Constraints

- Preserve user work; avoid broad staging, restore, reset, and cleanup commands.
- Commit and push only when requested. Drafting a message is not commit authority.
- Do not amend or rewrite shared history without explicit authorization.
- For destructive undo, inspect exact paths and consequences; clarify ambiguous
  intent before discarding data. Prefer reversible operations when suitable.
- Resolve conflicts from intended behavior and both sides' context. Do not blindly
  choose ours/theirs, abort, or continue an operation.
- Do not suppress hooks to make a commit succeed.
- Fetch missing history only when needed and permitted; report incomplete
  history instead of inventing a base. Account for detached HEAD, submodules,
  and LFS when they affect the task.

## References

- Read [Git commands](git-commands.md) when choosing commands for
  staging, history, recovery, or conflicts.
- Read [review targets](review-targets.md) when reviewing a worktree,
  root commit, merge commit, or commit with unavailable ancestry.

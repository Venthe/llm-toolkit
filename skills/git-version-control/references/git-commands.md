# Git Command Reference

Use these commands as a focused reference, not as a substitute for inspecting
repository state.

## Inspect state

```bash
git status --short --branch
git branch --show-current
git log -5 --oneline --decorate
git diff
git diff --cached
git diff --stat
git ls-files --others --exclude-standard
```

`git diff` shows unstaged tracked changes. `git diff --cached` shows staged
changes. Untracked files do not appear in either diff until their contents are
inspected separately or staged.

## Branches and remotes

```bash
git branch --list
git branch -vv
git remote -v
git switch <branch>
git switch -c <new-branch>
git fetch <remote>
```

Fetching updates remote-tracking refs without merging them into the current
branch. Do not switch branches with a dirty worktree until you understand
whether changes will be carried, conflict, or be blocked.

## Stage and commit

```bash
git add -- path/to/file
# For selected portions of a file:
git add -p -- path/to/file
git diff --cached
git status --short
git commit -m "<message>"
```

Stage only files and hunks related to the task. Before committing, verify the
staged diff and check for secrets, generated files, and accidental changes. Use
the commit-message format already established by the repository.

## Inspect history

```bash
git show --stat --oneline <commit>
git show <commit> -- path/to/file
git log --oneline -- path/to/file
git blame -L <start>,<end> -- path/to/file
git diff <base>...<head>
```

Use `git diff A...B` to compare the merge base of `A` and `B` with `B`, which is
useful for reviewing branch changes relative to their common ancestor.

## Restore changes carefully

```bash
# Discard unstaged changes in one path (destructive):
git restore -- path/to/file

# Unstage one path while keeping its working-tree contents:
git restore --staged -- path/to/file

# Restore a path from a specific commit (review before use):
git restore --source=<commit> -- path/to/file
```

Before a destructive restore, inspect the file diff and confirm that no user
work will be lost. Do not use a pathless restore to discard the entire worktree.

## Merge and rebase conflicts

```bash
git status
git diff --name-only --diff-filter=U
git diff --check
```

After resolving conflicts, inspect each resolved file and `git diff`, then run
tests. Use `git status` to determine whether Git expects a merge commit
(`git merge --continue`) or rebase continuation (`git rebase --continue`). Do
not run either until all conflicts are resolved and the result is reviewed.

## Recovery and destructive commands

Prefer inspection before recovery:

```bash
git reflog --date=local -10
git stash list
git stash show --stat <stash>
```

`git reset --hard`, `git clean -fd`, `git push --force`, and history-rewriting
operations can destroy work or affect collaborators. Do not use them without
explicit authorization and a clear understanding of the target. If recovery is
needed, inspect the reflog and current state before changing anything.

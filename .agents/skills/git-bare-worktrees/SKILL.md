---
name: git-bare-worktrees
description: Explicitly manage a repository as a bare Git store with
  configurable persistent branch worktrees, or convert between that
  layout and a conventional single-checkout clone. Invoke only when the
  user explicitly requests this workflow.
---

# Bare Repository and Branch Worktrees

## Activation boundary

This workflow is opt-in. Activate it only when the user explicitly
invokes this skill or clearly requests a bare-repository/worktree
layout, for example:

-   `/Git clone branches dev,prod as worktrees`
-   "Convert this repository to a bare repository with worktrees for
    main and develop."
-   "Convert the worktree layout back to one normal checkout."

Do **not** apply it automatically to ordinary Git tasks, agentic coding
workflows, feature work, or requests to clone a repository without
explicit bare/worktree intent. Use
[git-version-control](../git-version-control/SKILL.md) for those tasks.

## Layout and configuration

Use one shared bare repository and one directory per configured branch:

``` text
<parent>/
  <project-name>.git/          # bare Git store
  <project-name>-<branch>/     # one worktree per configured branch
```

Branch names containing `/` are valid; map `/` to `-` in directory names
(for example, `release/1.2` → `<project-name>-release-1.2`). Detect
directory-name collisions before creating anything.

Treat the requested branch list as configuration, not a hard-coded
convention. The user may add or remove branch names in later
invocations. Before changes, show the current worktree list and compare
it with the requested list. Do not remove a worktree merely because it
is absent from the new list unless the user explicitly requests
pruning/removal.

## Safety requirements

1.  Inspect the current directory, repository state, remotes, branches,
    tags, and worktrees before mutation.
2.  Confirm destination paths do not already contain unrelated data.
    Never overwrite an existing repository or directory.
3.  Preserve local commits, uncommitted changes, untracked files, tags,
    and remote configuration. If a conversion cannot preserve these
    safely, stop and explain the gap.
4.  Do not delete the source repository during conversion. Create the
    target alongside it, verify it, and only then offer the source for
    manual removal.
5.  Never force-update remote branches, rewrite published history, or
    use destructive cleanup as part of setup.
6.  Ask before proceeding if the source is dirty, has untracked files,
    has detached `HEAD`, has active merge/rebase/cherry-pick state, or
    contains local branches that would be omitted. Do not silently
    discard or migrate working-tree changes.
7.  Verify every operation from command output and follow with
    `git status`, `git remote -v`, `git branch -avv`, and
    `git worktree list` where applicable.

## Select a mode

Read only the reference for the requested operation after applying the shared
rules above.

| Requested operation | Reference |
| --- | --- |
| Create a bare repository with selected worktrees, or add, update, or remove configured worktrees | [Create and maintain](references/create-and-maintain.md) |
| Convert a conventional repository to the bare/worktree layout, or convert that layout back to one checkout | [Convert layouts](references/convert-layouts.md) |

## Completion report

Report the bare repository path and `origin` URL; each worktree path and branch;
whether branches track `origin/<branch>`; local-only branches or commits; dirty
state, skipped branches, and unresolved collisions; and every verification
command with its result.

Never claim conversion, origin configuration, or worktree creation
succeeded unless verified.

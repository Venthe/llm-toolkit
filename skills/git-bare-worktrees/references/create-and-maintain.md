# Create and maintain bare worktrees

Read this reference only to create a bare repository with selected worktrees or
to change an existing configured worktree list. Apply the entrypoint's safety
requirements before these procedures.

## Create a bare repository with selected branch worktrees

Collect the source remote URL or local repository path, project name and parent
directory, explicit branch list, and a base branch for any requested new branch.

1. Derive `<project-name>.git` and every worktree path. Refuse collisions; do
   not guess alternative names.
2. Clone into the bare directory and inspect `origin`. A bare clone copies
   branch heads to local branches but does not create remote-tracking refs or a
   fetch refspec.
3. Configure a standard `origin` fetch refspec equivalent to
   `+refs/heads/*:refs/remotes/origin/*`, then fetch.
4. Resolve each requested branch. Use an existing local branch; otherwise create
   a local tracking branch from an existing `origin/<branch>`; otherwise ask for
   the base branch needed to create it. Never invent a base.
5. Add one worktree per selected branch. Use an existing local branch unless the
   user explicitly requested creation of a new branch.
6. Confirm every worktree's branch and `origin` URL, and confirm that
   `git worktree list` matches the requested configuration.

For existing remote branches:

```text
git clone --bare <remote-url> <project-name>.git
git --git-dir=<project-name>.git config remote.origin.fetch +refs/heads/*:refs/remotes/origin/*
git --git-dir=<project-name>.git fetch origin
git --git-dir=<project-name>.git branch --track dev origin/dev
git -C <project-name>.git worktree add ../<project-name>-dev dev
```

Do not run `git remote add origin` when it already exists. Inspect it and change
it only with the user's authorization. If a requested branch exists only on the
remote, create the local tracking branch before adding its worktree. For an
explicitly requested new branch, use:

```text
git -C <project-name>.git worktree add -b <branch> <path> <base>
```

## Maintain the configured worktree list

Inspect the current configuration with:

```text
git -C <project-name>.git worktree list
git --git-dir=<project-name>.git fetch origin
git --git-dir=<project-name>.git branch -avv
```

Fetching updates remote-tracking refs; it does not fast-forward checked-out
branches. After inspecting a worktree and confirming it is clean, update it
explicitly when requested, for example:

```text
git -C ../<project-name>-dev merge --ff-only origin/dev
```

To add a branch later, resolve whether it exists locally or remotely, then add
its worktree. To remove one, inspect and preserve its changes first, then remove
only the specifically requested path with:

```text
git -C <bare-path> worktree remove <path>
```

Do not prune or delete branches unless explicitly requested. A branch checked
out in one worktree cannot normally be checked out in another at the same time.

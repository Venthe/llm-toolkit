# Convert between repository layouts

Read this reference only when converting a conventional checkout to a bare store
with worktrees, or converting that layout back to one conventional checkout.
Apply the entrypoint's safety requirements before either procedure.

## Convert a conventional repository to bare + worktrees

Do not transform the source in place. Create a separate bare repository beside
it and retain the original checkout until verification is complete.

1. Inspect `git status --short --branch`, local and remote branches, tags,
   remotes, and `git worktree list`. Require a clean source with no active Git
   operation. If it is dirty, ask the user to commit, stash, or choose another
   migration strategy; do not assume a stash preserves untracked or ignored
   files.
2. Record the source's `origin` URL when present and the requested branch list.
   Confirm all local commits and tags that must be retained are in the source.
3. Create `<project-name>.git` from the local source, so local-only branches,
   commits, and tags are copied. For example:

   ```text
   git clone --bare <source-path> <project-name>.git
   ```

4. If the source has an external `origin`, update the bare repository's `origin`
   URL to that recorded URL; otherwise, ask for the intended upstream instead of
   inventing one. Configure and verify the standard fetch refspec, then fetch
   only when appropriate and permitted.
5. Add worktrees for the explicitly selected branches using
   [create and maintain](create-and-maintain.md). Create a local tracking branch
   only when its remote counterpart exists; otherwise ask for a base.
6. Verify branch tips, tags, remotes, and worktrees against the source. Keep the
   original checkout until the user decides what to do with it.

Do not substitute a remote URL clone for the local source clone when the source
contains local-only commits; it can omit those commits.

## Convert bare + worktrees back to one conventional checkout

Do not delete the bare store or existing worktrees during conversion.

1. Inspect the bare repository's branches, tags, remotes, and every worktree's
   status. Stop if any worktree is dirty or has an active Git operation, and ask
   how to preserve that state.
2. Choose the target path and primary branch explicitly. Refuse to overwrite an
   existing directory.
3. Create a normal clone into the target. If an external upstream is known,
   update the new clone's `origin` from the local bare path to that upstream and
   configure its normal fetch refspec. If no external upstream is known, ask
   whether `origin` should stay local or be changed; do not guess.
4. Verify the selected branch, upstream tracking, tags, remote URL, and relevant
   commit IDs. Confirm that local-only branches and commits remain available.
5. Keep the bare repository and old worktrees until the user verifies the new
   checkout. Remove them only on an explicit request after checking for unique
   commits or data.

If the desired result is only a checkout of the remote default branch and no
local-only refs need to be retained, use a normal clone from that remote rather
than the bare store.

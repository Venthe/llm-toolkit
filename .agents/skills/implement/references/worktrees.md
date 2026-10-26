# Worktree setup and lifecycle

Use the repository's documented worktree convention when present. The
version-control skill's [Git workflow](../../version-control/references/git-workflow.md)
and [review targets](../../version-control/references/review-targets.md) govern
state inspection and preservation.

## Before creation

1. From the repository root, inspect `git status --short --branch`, staged and
   unstaged diffs, untracked files, active merge/rebase state, and recent branch
   conventions. Read relevant untracked files if they may be user work; avoid
   exposing secrets.
2. Identify the current branch and its upstream/base from repository evidence.
   Do not assume `main`, fetch, or switch the user's current checkout as a side
   effect. Fetch only when a current remote base is needed and permitted.
3. Select a descriptive task branch and a worktree location outside ignored or
   generated directories. Check for an existing branch or path collision first.
   Never remove or overwrite an existing worktree to make room.
4. Create the worktree using the installed Git version's supported command and
   repository conventions. Verify the path, branch, and clean starting state.
   The primary worktree's pre-existing changes must remain untouched.

## Prepare and verify

Read project setup instructions and run only required, scoped setup steps in the
new worktree. Inspect dependency-install scripts and lifecycle effects before
running them. Establish a baseline with the repository's documented focused
tests or checks when feasible. Record existing failures as baseline failures;
do not attribute them to task changes.

## Preserve through handoff

Keep the worktree and branch for user review. Report both paths and the base
revision. Cleanup, branch deletion, merge, and push are separate actions that
require explicit scope; do not infer them from a successful implementation.

If Git worktree support, the required base, or safe isolation is unavailable,
stop before editing and report the concrete blocker. Continue in the primary
checkout only if the user authorizes that alternative.

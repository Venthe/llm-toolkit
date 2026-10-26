# Optional worktree setup and merge-back

Use this procedure only when the user explicitly requests an isolated Git
worktree. The normal `implement` workflow uses the current checkout. This
optional flow ends by merging the completed task branch back into the branch
that was current when the flow started.

Use the repository's documented worktree convention when present. The
version-control skill's [Git workflow](../../git-version-control/references/git-workflow.md)
and [review targets](../../git-version-control/references/review-targets.md) govern
state inspection and preservation.

## Before creation

1. From the repository root, inspect `git status --short --branch`, staged and
   unstaged diffs, untracked files, active merge/rebase state, and recent branch
   conventions. Read relevant untracked files if they may be user work; avoid
   exposing secrets.
2. Identify and record the branch currently checked out in the primary checkout
   and its upstream/base from repository evidence. This is the merge-back
   branch. Do not assume `main`, fetch, or switch the primary checkout as a side
   effect. Fetch only when a current remote base is needed and permitted.
3. Select a descriptive task branch based on that merge-back branch and a
   worktree location outside ignored or
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

## Merge back and hand off

After the final review and checks pass in the isolated worktree, merge the task
branch back into the recorded merge-back branch in the primary checkout:

1. Reinspect the primary checkout's branch, status, staged and unstaged diffs,
   and untracked files. Verify it is still on the recorded branch. Preserve all
   pre-existing changes and never stage, discard, or overwrite them to enable a
   merge.
2. Merge the completed task branch using the repository's merge convention. If
   there is no convention, create an explicit merge commit so the integration is
   traceable. Review the resulting merge state and run checks affected by the
   integration.
3. If the branch changed, the merge is unsafe, or a conflict cannot be resolved
   without touching unrelated user work, stop and report the concrete state.
   Do not abort, reset, stash, or force a merge merely to complete the flow.
4. Keep the auxiliary worktree and task branch available after the merge unless
   the user separately requests cleanup. Do not push or publish.

If Git worktree support, the required base, or safe isolation is unavailable,
report the concrete blocker and continue in the current checkout only if the
user authorizes that alternative.

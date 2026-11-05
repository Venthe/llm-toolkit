---
name: rewrite-commit-chain
description: >-
  Rewrite committed Git history from a parent to a branch tip into atomic,
  dependency-ordered commits while preserving the original tip tree exactly.
  Use when asked to reorganize, split, squash, or clean up a commit chain with
  snapshot parity. Not for message-only drafting, ordinary rebasing onto new
  upstream content, or incorporating uncommitted work.
---

# Rewrite a commit chain

Reconstruct the story of the committed change without changing its final
content. Apply this workflow only when history rewriting is requested.
Read [Git workflow](../git-version-control/SKILL.md) for repository operations
and [commit messages](../write-commit-message/SKILL.md) before committing.
Those sibling skills are dependencies when distributing this skill separately.

## Invariants

- Snapshot committed history only. Staged, unstaged, untracked and ignored
  content is not input to the rewrite and must remain untouched.
- Preserve the original tip under a uniquely named local backup tag before
  constructing replacement history. Never overwrite an existing backup.
- The final rewritten Git tree must equal the original tip tree by object ID.
  This includes file paths, blob contents, modes, symlinks and submodule gitlinks.
  Commit IDs, timestamps and signatures will change; historical signatures
  cannot be retained on rewritten commits. LFS objects and submodule contents
  outside the recorded tree are not independently verified by tree parity.
- Each ordinary commit is one coherent change, ordered after its prerequisites.
  Its message describes its actual diff. Include tests with the behavior they
  protect; avoid a broken intermediate state merely to imitate original order.
- Content excluded from the polished commits belongs in a final
  `WIP: Remaining changes` commit. This is the explicit exception to ordinary
  commit atomicity: it restores exact parity and exposes leftovers for review.
  Do not create an empty WIP commit when no residual exists.
- Never silently fix, discard or add final content. If instructed to remove
  `PLAN.md` from the polished history, restore its original bytes in the WIP
  commit. Likewise undo temporary scaffolding or incidental improvements there
  when needed for parity. Disclose this result. If the user explicitly demands
  both a changed final tree and parity, clarify the conflict before rewriting.
- Do not push or rewrite other branches automatically. Preserve backup refs
  until the user requests their removal. Do not bypass hooks to achieve parity;
  stop and report a hook/policy conflict if the original content cannot be kept.

## Establish the boundary

1. Read repository instructions, status, staged/unstaged diffs, untracked paths,
   worktree ownership and relevant branch history. Detect an existing rebase,
   merge or other unfinished operation; do not overlap it. Record the original
   branch ref (or detached HEAD), full tip SHA and tree ID.
2. Prefer an explicit parent. If omitted, inspect PR/stack ancestry and project
   conventions, then the default branch (`main` when appropriate). A remote
   tracking branch for the target itself is not automatically its parent.
   Announce the selected base and reason; ask only if multiple plausible bases
   would materially change scope. Fetch only if needed to resolve missing data.
3. For an explicit ancestor commit, use that commit as the boundary. For a
   branch parent that has advanced independently, use its merge-base with the
   original tip. Freeze the resulting SHA. Require a single unambiguous base;
   missing history, multiple merge-bases or unrelated roots require clarification.
   Do not combine a content-preserving rewrite with an upstream rebase.
4. Inspect both `base..tip` history and `git diff base tip`, including binary
   changes, deletions and merge resolutions. The default output is linear.
   Merges may be flattened while retaining their final effects; disclose this.
   If preserving topology is requested, agree the adapted method first.
5. If base equals tip or there is no useful restructuring, report that rather
   than manufacturing commits. Identify any descendant/shared branches that will
   retain old ancestry; do not silently move them.

## Plan the replacement commits

Map final changes to coherent responsibilities and dependencies, not arbitrary
file counts or old commit boundaries. A possible sequence is:

1. Create the Maven module and wire it into the build.
2. Add the minimum scaffolding needed by the feature.
3. Implement feature foo with its tests.
4. Add a dependent integration.
5. WIP: Remaining changes, only when necessary.

This is an example, not a requirement to split module setup from code when that
would break the build. Consolidate fixups into their owning change. Record a
short plan of commit purposes and verification; proceed within existing rewrite
authorization without asking for approval of routine grouping choices.

## Preferred replacement method

Prefer rebuilding in a temporary branch and linked worktree, leaving the source
worktree and original branch in place until the candidate is verified. This
makes mixed commits easier to untangle than a long interactive rebase and keeps
uncommitted user work out of the process. Do not auto-stash the source tree.

The commands below are templates: substitute captured refs/SHAs using the
active shell's quoting rules, check each exit status, and use unique names.
Do not paste angle-bracket placeholders literally.

1. Create `git tag -a <unique-backup-tag> <original-tip> -m "Before commit-chain rewrite"`
   and verify its peeled commit resolves to
   the recorded tip. Create a temporary worktree and branch rooted at the frozen
   base with `git worktree add -b <candidate-branch> <temporary-path> <base>`.
   Record all paths and refs for recovery. Temporary artifacts belong outside
   tracked source directories.
2. Reconstruct one planned commit at a time in that worktree. Reuse an existing
   coherent commit with `git cherry-pick --no-commit <sha>` when it fits the
   plan. Otherwise restore selected paths from the snapshot, apply selected
   patches, or edit intermediate versions, then stage explicit paths/hunks.
   Never interpret the source worktree as the desired snapshot. Resolve merge
   changes from their final behavior, not by blindly cherry-picking merge SHAs.
3. Before each commit, inspect the staged diff and its dependencies. Run checks
   appropriate to the intermediate state and follow repository hooks. Use the
   commit-message skill. Do not commit verification output or unrelated files.
4. Inspect the residual between candidate HEAD and the original snapshot.
   If nonempty, explain what remains. In the task-owned temporary worktree,
   finish or discard only your own uncommitted reconstruction edits after
   inspecting them. Check for untracked/ignored collisions before restoring.
   Use `git read-tree --reset -u <original-tip>` to restore the exact tracked
   snapshot into its index and worktree, including removals and binary changes.
   This destructive command is restricted to the verified task-owned temporary
   worktree; never run it in the user's source worktree. Inspect the staged
   residual and commit it as `WIP: Remaining changes`. Hooks or filters that
   alter the snapshot must be detected by the parity checks below.
5. Verify the candidate before replacement:
   - `git rev-parse <candidate>^{tree}` equals the recorded snapshot tree ID.
   - `git diff --exit-code <original-tip> <candidate>` reports no differences.
   - The frozen base is an ancestor of the candidate; inspect the new sequence
     and each parent-to-child diff for atomicity and dependency order.
   - Run final checks required by the repository. Separate pre-existing failures
     from introduced failures; parity does not prove intermediate commits work.
6. Recheck the target ref, worktree ownership, index, local changes and operation
   state. If they changed concurrently, stop replacement and retain the candidate.
   For a named branch, replace it using compare-and-swap:
   `git update-ref -m "Rewrite commit chain with identical tip tree" <full-branch-ref> <candidate-tip> <original-tip>`.
   This is appropriate even for a checked-out branch only because old and new
   tip trees are identical: leave its index and worktree untouched. Do not use
   `reset --hard`, checkout another branch over dirty files, or retry a rejected
   update against a newly observed tip without investigating.
   For detached HEAD, preserve detachment and use an equivalent guarded
   `git update-ref --no-deref HEAD <candidate-tip> <original-tip>` from its owner.
7. Verify the target now resolves to the candidate, tree parity still holds,
   and the source index and uncommitted/untracked state match the recorded state.
   Keep the original backup tag. Remove only the task-owned temporary worktree
   and candidate branch when clean, no longer needed and safely identified;
   otherwise retain them and report their locations. Never force cleanup of
   unexpected files or processes using the worktree.

For already-coherent linear commits needing only a few edits, an interactive
rebase on the temporary candidate is acceptable. The same backup, boundary,
residual, verification and guarded-replacement requirements still apply.

## Recovery and reporting

Before replacement, any failure leaves the original ref intact. Preserve the
candidate and backup and report the exact failing operation. After replacement,
restore the original ref only with a guarded update and only if it has not moved
since; identical trees preserve local edits. Never overwrite concurrent work.

Report the parent/base, original and rewritten SHAs, backup ref, commit sequence,
WIP contents (or absence), tree-parity result, executed checks and limitations.
State whether source local changes were preserved and whether any temporary
resources remain. Never call the rewrite complete if tree IDs differ.

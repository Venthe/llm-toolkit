# Select a review target

Use this procedure for standalone or combined reviews. These are inspection
commands, not permission to stage, reset, switch branches, or fetch.

## Worktree

Run from the repository root:

```text
git status --short --branch
git diff --no-ext-diff --no-textconv
git diff --cached --no-ext-diff --no-textconv
git ls-files --others --exclude-standard
```

Inspect relevant untracked contents separately, excluding secrets and generated
output. The two diffs show different layers; where a file has both staged and
unstaged edits, inspect its final contents too. Include deletions and renames.
Do not mistake an empty unstaged diff for a clean worktree. With an unborn HEAD,
the cached diff still shows staged additions.

## Specified commit

Resolve the supplied ref first, quoting it for the active shell:

```text
git rev-parse --verify --end-of-options "<ref>^{commit}"
git show --no-patch --format=fuller <resolved-sha>
git cat-file -p <resolved-sha>
```

Use the resolved SHA in subsequent commands. Inspect the commit object's `parent`
headers. This distinguishes a real root from a shallow boundary with unavailable
parent objects.

- **One or more parents:** verify the first parent object exists, then use
  `git diff --no-ext-diff --no-textconv <parent-sha> <resolved-sha>`. For a merge,
  state explicitly that this is the first-parent comparison; a default combined
  merge diff can omit relevant changes. Use another baseline when requested.
- **No parent headers:** use
  `git diff-tree --root --no-commit-id -r -p --no-ext-diff --no-textconv <resolved-sha>`.
  This reviews initial additions without assuming a parent or a hash algorithm.
- **Parent unavailable:** report missing ancestry. Fetch only when needed and
  permitted; never present the shallow boundary as a true root commit.

Read surrounding files from the target tree with
`git show <resolved-sha>:path/to/file`. Working-tree files may describe another
revision. Do not check out the target over user changes just to inspect it.

## Verification and reporting

Checks executed in the current worktree verify that state, not necessarily the
specified commit. Label this distinction. When execution at the target revision
is necessary, use an authorized isolated checkout and account for its dependency
and runtime requirements.

Record target, baseline, changed areas, relevant exclusions, commands run, and
missing context. Do not infer a regression from a failure without establishing
that the change caused it. Report findings even if verification is unavailable,
with appropriately limited confidence.

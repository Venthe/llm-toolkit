---
name: write-pull-request
description: >-
  Prepare or review a pull request title and description from the actual branch
  changes, repository conventions, and verified checks. Use for PR readiness,
  release-risk summaries, and explicitly requested creation or updates through
  an available MCP integration.
---

# Prepare a pull request

Create a clear, evidence-based pull request that helps reviewers understand the
change, its motivation, its validation, and any material risk. Follow repository
conventions and preserve the user's scope. Preparing text does not authorize
committing, pushing, merging, or publishing it.

## Establish the PR scope

1. Read applicable `AGENTS.md` instructions and inspect Git state before making
   changes. Follow [version control](../git-version-control/SKILL.md) and its
   [target-selection guidance](../git-version-control/references/review-targets.md)
   when selecting the branch comparison.
2. Establish the intended base and head from the request, repository
   configuration, and available remote or hosting metadata. Do not assume
   `main`, guess a base, or claim a remote PR was inspected when no such access
   is available.
3. Inspect the complete relevant change: the base-to-head diff, commit history
   for context, and staged, unstaged, and untracked changes separately.
   Determine which changes will actually be included in the PR. Do not silently
   describe local uncommitted work as part of a branch that does not contain it.
4. Identify unrelated or mixed concerns, generated files, accidental changes,
   secrets, and compatibility implications. Report scope concerns; do not split
   commits, discard changes, or rewrite history unless explicitly requested.
5. Look for the target repository's PR template and contribution guidance first.
   Use them when present. Otherwise use the
   [default PR template](assets/pull-request-template.md), removing irrelevant
   sections and replacing all placeholders.

## Build the title and description

1. Read surrounding code and linked issue, ticket, ADR, or design context when
   available and relevant. Distinguish verified facts, assumptions, intended
   behavior, and unresolved decisions.
2. Write a concise, outcome-focused title that matches repository naming
   conventions. Describe the coherent change rather than the author's activity.
   Use [commit-message guidance](../write-commit-message/SKILL.md) only when its
   title conventions are relevant; a PR title is not automatically a commit
   message.
3. Explain the problem or desired outcome, the important behavior or design
   changes, and why they matter. Include relevant implementation details only
   when they help reviewers assess the change.
4. Describe validation using exact commands and observed outcomes when
   available. Separate passed checks, failed checks, checks not run, and
   environmental blockers. Never infer that tests passed from their presence, a
   green historical run, or a successful build of a different revision.
5. Include risks, migrations, rollout or rollback notes, security effects,
   compatibility concerns, and follow-up work only when material and supported
   by evidence. Link known related work using verified identifiers and URLs; do
   not invent issue references, approvals, owners, or release claims.
6. Keep the description proportional to the change. Remove unused template
   sections, generic filler, duplicate summaries, and all unresolved
   placeholders. Preserve domain language and the target project's terminology.

## Check readiness

- Compare the title and body against the actual diff and intended PR scope;
  every significant change should be represented and unsupported claims removed.
- Check for accidental secrets, sensitive data, unrelated modifications,
  generated output, broken local references, and claims that imply work or
  checks were completed when they were not.
- Use [software development guidance](../software-development/SKILL.md) when
  technical review is needed and
  [software testing guidance](../software-testing/SKILL.md) when selecting or
  reporting checks. Follow their scope, execution, and safety constraints; do
  not run tests that would mutate shared systems merely to fill the template.
- If the request includes readiness review, report blockers and residual gaps
  rather than presenting a polished description as proof that the branch is
  ready to merge.

## Remote pull-request actions

Default to drafting or reviewing the title and body locally. Do not commit,
push, create, update, merge, or publish a PR merely because preparation was
requested. If the user explicitly asks to create or update a pull request and an
appropriate MCP integration is available, use it to interact with the remote
systems within the requested scope. If the integration is unavailable or lacks
access, provide the prepared content and state the limitation. Do not describe
MCP implementation mechanics in the PR content.

## Output

For a draft, return the proposed title and complete Markdown body, normally
without a preface. For a repository-file request, follow the repository's
established location and naming. For an explicitly requested remote action,
report the resulting PR link or the actual failure, along with the exact checks
and unresolved limitations. Never claim a PR was created or updated without
confirmation from the remote system.

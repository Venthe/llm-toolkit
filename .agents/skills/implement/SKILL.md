---
name: implement
description: >-
  Implement a scoped feature or fix from a PR description, link, ticket, or
  technical brief in the current checkout using an implementation plan,
  test-driven task execution, review and quality gates, and a commit after each
  step. An isolated Git worktree is optional only on explicit request. Use for
  explicit requests such as "$implement <request>"; not for review-only,
  planning-only, or deployment requests.
---

# Implement a planned change

Coordinate the existing version-control, development, testing, debugging, and
commit-message skills into one end-to-end implementation workflow. Keep this
entrypoint as orchestration; load companion skills only at the stage where they
apply. The requested work is authorization to implement within scope, but it
does not authorize publishing, pushing, deploying, destructive cleanup, or other
external side effects. A merge is permitted only as the final integration step
of the explicitly requested optional worktree flow.

## Workflow

1. **Establish the request.** Parse the description, PR, ticket, or link and the
   user's technical decisions. Inspect supplied sources using available tools;
   for a ticket number, use an actually available connected integration if one
   exists. Do not invent ticket content or claim inaccessible sources were read.
   Inspect repository instructions and Git state before mutation. Separate
   pre-existing work from this task and preserve unrelated changes.
2. **Use the current checkout.** Implement in the current checkout by default.
   Keep pre-existing changes separate from task changes throughout the work: use
   explicit paths or hunks for staging, and do not overwrite, discard, or
   include unrelated work in task commits. Use an isolated worktree only when
   the user explicitly requests it; then read
   [optional worktree setup and merge-back](references/worktrees.md) and follow
   its complete lifecycle.
3. **Clarify and plan.** Resolve material ambiguity from the request, repository
   evidence, and supplied technical decisions. Follow
   [software development](../software-development/SKILL.md) for implementation
   context and [software testing](../software-testing/SKILL.md) for
   verification. Write a concise, ordered plan with small independently
   verifiable steps, exact likely files, behavior, tests, lint/build checks, and
   dependencies. Save it in the project's established plan location when one
   exists; otherwise use a clearly named task plan in the checkout used for
   implementation. Review the plan for complete request coverage and unnecessary
   work. The `$implement` request authorizes proceeding with the plan; do not
   pause for a second approval unless a material ambiguity or safety issue
   remains. See the [workflow model](references/workflow-model.md) for this
   adaptation.
4. **Execute one step at a time.** Follow
   [task execution gates](references/task-gates.md). For each behavior change,
   use TDD: add a focused failing test, run it and confirm it fails for the
   expected reason, implement the smallest correction, run the test to green,
   then refactor if useful and rerun relevant tests. Run applicable lint and
   broader checks at the planned checkpoints. Review each completed step against
   its requirement and inspect the diff before committing that coherent step.
   The explicit `$implement` request includes authorization for these task
   commits. Use [write-commit-message](../write-commit-message/SKILL.md) and
   [version-control](../git-version-control/SKILL.md) to commit only intended
   task files. If repository policy prohibits commits, stop and report the
   conflict.
5. **Review and finish.** After the steps, run relevant full checks, inspect the
   complete diff, and conduct a requirements-based code review using
   [software development review guidance](../software-development/references/reviewing.md).
   Resolve actionable findings within scope, rerun affected checks, and commit
   the fixes. Do not claim completion while required checks fail or remain
   unverified; report blockers and residual gaps. In the optional worktree flow,
   finish the merge-back described in its reference. Do not push, publish, or
   remove the auxiliary worktree unless requested.

## Operating rules

- The user's supplied technical decisions constrain design. Identify conflicts
  with repository contracts or safety requirements instead of silently
  overriding them.
- Ask focused questions only when missing information materially blocks a safe,
  correct plan. Otherwise record a reasonable assumption and proceed.
- Preserve task context across steps. Track completed steps, checks, commits,
  and unresolved decisions in the plan or a compact ledger.
- A failed check is diagnostic evidence. Investigate the cause; do not weaken a
  test, suppress lint, skip a gate, or retry until green without a justified
  fix.
- If the repository has no automated test for a behavior, use its established
  verification approach and state the limitation; do not fabricate a TDD cycle.
- Reuse companion skills by reference. Their normal boundaries still apply; this
  workflow does not turn code review into permission to alter unrelated code or
  testing into permission to mutate shared services.

## Completion report

Summarize the implementation, plan location, current branch, commits, checks and
outcomes, review findings resolved, and remaining limitations. For the optional
worktree flow, also report the temporary branch/path and the merge-back result.
State that changes have not been pushed or published.

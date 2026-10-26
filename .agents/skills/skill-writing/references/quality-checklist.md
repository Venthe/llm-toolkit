# Evaluate skill quality

## Selection and scope

- Does the description distinguish this task from neighboring skills?
- Does an explicit invocation produce the requested outcome?
- Are user preferences and repository conventions preserved?
- Are dependencies available or their absence handled honestly?
- Does the skill avoid turning a draft/review into an external write or a fix?

## Instructions and resources

- Does each instruction change a decision or prevent an observed failure?
- Are core requirements separated from defaults and examples?
- Do resource links state when to load them, with no hidden mandatory procedure?
- Are examples consistent with the output contract?
- Do scripts fail clearly and preserve existing data?
- Are commands appropriate for the discovered shell and runtime?

## Behavioral evaluation

Choose representative requests from real use. Include an ordinary case, an
ambiguous or failure case, and a neighboring task that should not trigger the
skill. Define observable outcomes before execution, then inspect outputs and
actions rather than matching exact wording.

For this collection, useful cases include:

- Draft a commit message while different changes are staged and unstaged:
  describe only the requested target; do not commit.
- Review a root or merge commit: select the right baseline and inspect files
  from that revision; preserve a dirty worktree.
- Draft a ticket with no supplied error behavior: do not invent requirements,
  issue IDs, or completed checklist items.
- Diagnose a requested container engine that is unreachable: report the actual
  failure without silently switching engines or deleting resources.
- Review code through the combined development skill: remain in diagnostic mode
  unless fixes were requested; load only references relevant to the change.
- Review with verification: permit known temporary/build outputs, preserve
  source and snapshots, and do not silently switch an inspection-only request to
  execution.
- Prepare an implementation ticket: preserve the supplied DoD hierarchy and use
  observable acceptance criteria without inventing stakeholder approval.
- Recommend Kubernetes improvements: distinguish probe and disruption semantics,
  account for platform versions, and do not deploy proposed changes.
- Draft an ADR for a choice still under discussion: preserve proposed status and
  do not supersede an accepted predecessor until a replacement is accepted.

Use isolated fixtures where execution might affect data. Record scope, inputs,
observed outcomes, and limitations. Do not claim behavioral validation merely
because frontmatter and links pass. Refine demonstrated failures instead of
adding universal rules for speculative cases.

See
[Agent Skills best practices](https://agentskills.io/skill-creation/best-practices)
for further guidance on scope, context use, and iteration against real tasks.

# Design supporting resources

## What belongs where

| Resource | Content | Load condition |
| --- | --- | --- |
| `SKILL.md` | Selection metadata, core workflow, constraints, output | Whenever the skill applies |
| `references/` | Detailed heuristics, platform procedures, schemas, examples | When that topic or mode is needed |
| `scripts/` | Repeatable deterministic operations | When the workflow needs the operation |
| `assets/` | Templates and files copied into deliverables | When producing that output |

Split by a meaningful task condition, not a line quota. Keep important safety and
authorization constraints in the entrypoint so they are encountered before action.
Avoid duplicating instructions in both places. Keep links shallow and explain
their use; a directory listing alone does not tell an agent when to read a file.

## Separate skill or supporting reference?

Choose a separate skill when users can request the work independently, its
description can route those requests precisely, and it has a distinct workflow
or deliverable. Keep related modes together when they share the same task context
and differ mainly in execution or output detail. Use references for conditional
topic, platform, language, or format guidance within that workflow.

For this toolkit, development, testing, and debugging have distinct outcomes and
remain separate skills. Development's architecture, clean-code, OOP, XP, and Java
guidance stays in references. Cloud-native recommendations form a separate
assessment workflow; Twelve-Factor and Kubernetes are its reference topics.
Ticket triage and implementation preparation share one ticket-writing workflow
with separate references and templates.

Do not merge all engineering guidance into one catchall or create a discoverable
skill for every topic. Link a companion skill with a load condition and preserve
the caller's mode and authorization. Reuse skills already loaded for the task;
links do not require recursive loading of every companion and reference.

This decision rule follows [Agent Skills authoring guidance](https://agentskills.io/skill-creation/best-practices)
on coherent units and progressive disclosure. Validate the boundary using realistic
requests, including requests that should not activate the skill.

## Metadata

Use YAML frontmatter with a name matching the directory and a nonempty description.
This toolkit uses lowercase ASCII letters, digits, and single hyphens in names,
up to 64 characters. Descriptions are limited to 1024 characters. Supported
optional fields are `license`, `compatibility`, `metadata`, and `allowed-tools`.
Put additional string metadata, including versions, under `metadata`; quote
values that YAML could interpret as numbers or booleans. Do not add permissions
or tool restrictions the target runtime cannot enforce.

These conventions follow the [Agent Skills specification](https://agentskills.io/specification).
Check the current specification when changing schema rules rather than assuming
this reference is permanently complete.

## Scripts and assets

Add a helper only for a demonstrated repeated operation or reliability need.
Document its interpreter, dependencies, invocation directory, input/output, exit
codes, and side effects. Avoid hardcoded user paths, shell interpolation, hidden
network access, or installation as a side effect. Return actionable errors and
nonzero status for failures. Test meaningful behavior, including bad input.

Templates can contain clearly labeled placeholders; replace or remove them in
the delivered output. Do not leave unfinished instructions in `SKILL.md`.

## Shared guidance

Keep one source for genuinely shared procedures. Link companion skills by
relative path and document installation dependencies. In this toolkit the
development skill uses Git target selection when reviewing commits. If standalone distribution matters more than
deduplication, bundle the required dependency and license explicitly.

---
name: write-commit-message
description: >
    Draft or review commit messages. Refine message wording, body detail, or metadata. Use it with any version control system.
---

# Commit messages

Write a message that lets a maintainer understand the change and its motivation
without reconstructing the conversation. Follow
[Chris Beams' guidance](https://cbea.ms/git-commit/) using the rules below.
Repository-specific message conventions take precedence where they differ.

## Establish the message's scope

1. Identify whether the request concerns staged changes, a worktree diff, an
   existing commit, or supplied notes. Do not silently combine these targets.
2. When repository access is available, inspect status, the relevant diff, and
   nearby history. For the next commit, prioritize `git diff --cached`; inspect
   unstaged changes separately so they are not described as committed.
3. Read explicit message rules, required trailers, and issue-link conventions.
   Recent history supplies context, but a vague previous message is not a model.
4. Identify the primary change and the evidence for its purpose. Read surrounding
   code when the diff alone does not explain a behavioral consequence.
5. If the target is materially ambiguous, ask a focused question. If only the
   rationale is unknown, write the supported change and omit invented motivation.

## Seven message rules

1. **Separate the title and explanation.** If a body is useful, place one empty
   line after the subject; a simple change can stand on its subject alone.
2. **Aim for a 50-character subject.** Tighten wording before exceeding that
   target. Keep it within 72 characters unless project rules specify otherwise.
3. **Start the subject with a capital.** Respect required prefixes and scopes.
4. **Omit a final full stop.** Spend the subject's space on meaning.
5. **Express the subject as an action.** Prefer `Prevent duplicate delivery` to
   `Prevented duplicate delivery.` The body can use ordinary prose.
6. **Wrap body prose near column 72.** Keep paragraphs readable; preserve URLs,
   commands, and structured text when breaking them would damage their meaning.
7. **Explain the change and its reason.** Describe the prior problem, resulting
   behavior, and relevant consequences. Avoid narrating edits already evident
   in the diff.

These are the working defaults distilled from the linked article. Do not import
its historical claims about particular editors or hosting interfaces as current
tool requirements.

## Compose from evidence

Choose a specific subject describing the coherent change. Avoid generic labels
such as `Various fixes`, or an account of the author's activity. Do not introduce conventional commit
`feat:`/`fix:` prefixes solely because they are popular; preserve them when the
project uses them.

For a nontrivial change, consider whether the available context supports:

- the concrete failure, limitation, or requirement being addressed;
- the changed observable behavior or responsibility;
- an important compatibility effect, constraint, or tradeoff;
- a reason the selected approach matters to future maintenance.

Include only useful, supported points. Do not fabricate intent, performance gains,
test outcomes, issue IDs, or compatibility claims. A message is not a checklist
that needs every item filled in.

Read [examples and review checks](references/message-examples.md) when choosing
wording, deciding how much explanation to include, or reviewing a supplied draft.
Examples are illustrative and must not contribute invented facts to the message.

## Metadata and delivery

Place known issue references and required trailers according to project rules.
Do not invent a `Resolves:` relationship merely because an issue is mentioned.
Do not add attribution or sign-off trailers on someone's behalf without a basis.

When a requested commit needs a multiline message, use an editor or a message
file through the available tooling. Preserve real newlines and literal text;
avoid constructing shell commands from message content. Follow the Git workflow
for staging and execution.

A drafting request authorizes the message only. It does not authorize staging,
committing, amending, or splitting history. If the change mixes unrelated concerns,
identify that scope problem without rewriting commits automatically.

## Final review and output

Compare the message against the actual target once more. Check subject grammar,
length, capitalization, punctuation, body separation, wrapping, evidence, and
required metadata. Ensure unstaged or unrelated changes did not enter the text.

For generation, return the final message in a plain text code block without a
preface unless requested otherwise. For message review, identify concrete issues
and provide a corrected version. A formatting check cannot establish whether a
message truthfully describes the change; that requires inspecting its evidence.

## Examples

**Example scenario: combining past 4 commits for a consolidated message**

Given these commits in history (read for git via `git log -4`):

| SHA     | Description                                                                                                        |
|---------|--------------------------------------------------------------------------------------------------------------------|
| 3796602 | Added cloud-native-architecture, skill-writing, software-debugging, development, testing, ticket-management skills |
| 968b914 | Extended skill-writing validation and debugging references                                                         |
| 3d49761 | Migrated prepare-ticket→ticket-management; added adr, architecture-review, change-review skills                    |
| 428aa68 | WIP: initial multi-skill foundation with architecture review, container workflow                                   |

**Generate combined message:**

```
consolidate documentation for 9 agent skills across lifecycle workflows

Add 9 production-ready skills covering architecture decisions, development practices,
testing strategies, debugging workflows, ticket management, skill authoring quality,
cloud-native principles, and Git operations. Migrate legacy skills into focused
sub-skills (git-commit→version-control, prepare-ticket→ticket-management). Add
supporting assets: AGENTS.md, LICENSE, README.md, skill-audit documentation.
```

The combined message reflects all significant changes documented in the diff history
while remaining within 50-character subject limit (excluding newline). The SHA (s)
are referenced as evidence but do not appear in the final message body per Chris
Beams' guidance to avoid narrating activity. Only meaningful content changes are
summarized into the coherent narrative.

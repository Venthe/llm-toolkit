---
name: write-adr
description: >-
  Draft, review, or update Architecture Decision Records for significant
  technical choices. Use when recording decision context, alternatives,
  rationale, consequences, or the supersession of an earlier ADR; do not create
  records for ordinary implementation details unless requested.
---

# Architecture Decision Records

Capture enough context for a future maintainer to understand why a consequential
choice was made and when it might need revisiting. Keep each record focused on
one decision. This workflow draws on
[Michael Nygard's ADR approach](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).

## Establish the task and evidence

1. Identify whether the user wants a draft, a review, a record of an existing
   decision, or a replacement for a previous decision. Do not implement the
   architecture merely because its record is requested.
2. Inspect repository instructions, existing ADRs, templates, naming, numbering,
   indexes, and related designs or issues. Follow the established format.
3. Identify the decision drivers, known constraints, credible options, and the
   supplied choice. Separate facts, assumptions, and unresolved questions.
4. If the choice is unresolved, draft it as proposed. State a recommendation as
   such; do not invent agreement, an approver, a meeting, or a historical date.

## Draft or update

- Use the project's format, or [the default template](assets/adr-template.md)
  when none exists. Keep context factual and the decision explicit. Explain why
  the chosen option fits the drivers and what disadvantages the team accepts.
- Read [decision quality](references/decision-quality.md) when comparing
  options, handling missing evidence, or reviewing a draft. Include only
  meaningful alternatives; do not manufacture rejected options to fill a table.
- Read [lifecycle and storage](references/lifecycle.md) before assigning an ID,
  changing status, or superseding a record. Preserve the reasoning of past
  accepted decisions and link replacements.
- Default new choices to proposed unless the user or repository evidence
  establishes acceptance. An explicit instruction to record an accepted choice
  is sufficient; do not ask for the same authorization again.
- Include benefits, costs, risks, and operational or migration implications when
  supported. Link the evidence instead of copying large design documents.

## Delivery and review

For a text-only request, return Markdown. For a request to add the record to a
repository, write it at the established location, preserve neighboring records,
and update an existing index if that is part of its convention. Do not publish,
commit, or execute a migration as a side effect.

Check that the title identifies the choice, the decision answers the stated
problem, the rationale addresses its drivers, and status matches the evidence.
Verify local links and unique numbering when writing files. Call out material
unknowns; unresolved placeholders cannot support a claim of an accepted
decision.

For review, report concrete omissions, contradictions, or unsupported claims
with locations; do not rewrite an accepted decision or invent a replacement
unless requested. A request for a general code review belongs in the development
workflow and need not create an ADR.

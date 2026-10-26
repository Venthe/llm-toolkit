---
name: write-ticket
description: >-
  Draft or review Jira/Linear ticket text for triage or implementation. Use to
  turn reports and requests into evidence-based triage tickets, recommended
  classifications, or implementation-ready tickets with acceptance criteria and
  a relevant Definition of Done.
metadata:
  version: "1.0.0"
---

# Ticket management

Establish which decision the ticket should support: triage, or implementation of
an agreed outcome. Follow the team's template and terminology where supplied.

## Choose the mode

- **Triage:** use when requested or when a report needs impact assessment,
  classification, prioritization, routing, or investigation before a solution is
  agreed. Read [triage guidance](references/triage.md) and use the
  [triage template](assets/triage-template.md) when no team format is supplied.
- **Implementation-ready:** use when the requested outcome and scope are known.
  Read [implementation preparation](references/implementation-ready.md), choose
  relevant items from [the DoD menu](references/definition-of-done.md), and use
  [the implementation template](assets/ticket-template.md). Consult
  [acceptance-criteria guidance](references/acceptance-criteria.md) when
  refining acceptance.
- **Review:** evaluate the ticket against its intended mode. Triage tickets can
  be ready for a decision while their root cause and implementation remain
  unknown.

Honor an explicit mode. If an implementation request lacks a material
requirement, identify that gap; do not silently substitute a triage ticket and
call it ready. For an ambiguous request, infer the mode from the evidence and
state the assumption briefly when it affects the result.

## Shared workflow

1. Extract the problem or desired outcome, known context, evidence, and
   constraints.
2. Preserve domain terms and supplied identifiers. Separate observation,
   hypothesis, proposed recommendation, and confirmed decision.
3. Use the selected mode's reference and template. Include only useful fields;
   mark material unknowns explicitly and omit irrelevant boilerplate.
4. Check that the ticket lets its reader take the intended next step. Do not
   invent requirements, owners, metrics, deadlines, approvals, or completion.
5. Return Markdown unless another format was requested. For review, describe
   concrete omissions or contradictions and their effect on readiness.

## Boundaries

Drafting or recommending classification does not authorize creating/updating an
external issue, assigning someone, changing workflow state, or contacting
people. Use existing explicit authorization when those actions are requested.
Never mark checklist items complete without evidence. Keep sensitive evidence in
approved restricted locations and link sanitized context where possible.

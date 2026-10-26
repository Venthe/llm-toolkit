# Prepare a ticket for triage

A triage-ready ticket gives enough evidence to decide what should happen next.
It need not establish root cause, a solution, an estimate, or final acceptance
criteria. Use the team's triage policy; the scales below are suggested toolkit
defaults, not Jira/Linear settings or universal standards.

## Gather the minimum useful context

1. Write a title identifying the affected capability and observed problem or
   requested outcome. Avoid guessing a cause in the title.
2. Identify the type: defect, incident, feature/request, maintenance, or
   investigation. Keep a suspected defect distinct from a confirmed regression.
3. State expected and actual behavior, affected environment/version, first/last
   observed time with time zone if known, and frequency or recurrence.
4. For defects, include minimal reproduction steps, input/preconditions, and
   result. If not reproduced, say so and include available observations. For
   requests, describe the user need and current limitation instead of inventing
   reproduction.
5. Explain impact: affected users/workflows, scope, frequency, consequences,
   workaround and its cost, and any evidenced time constraint. Unknown scope
   should remain unknown; one report does not prove one affected user.
6. Link sanitized logs, traces, screenshots, reports, or related issues when
   supplied or accessible within scope. Search for duplicates when tooling is
   available, but do not claim a search when none ran. Similar symptoms may have
   different causes.
7. Recommend classification and the next triage action, with rationale,
   confidence, and key unanswered questions. Keep recommendations separate from
   recorded decisions.

## Severity: impact of an observed failure

Use severity for defects/incidents where meaningful. For a feature request use
not applicable, and describe value and urgency separately.

| Level       | Suggested interpretation                                                                                                             |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| S1 Critical | Essential operation is broadly unavailable, or credible severe data/security harm requires urgent assessment; no adequate workaround |
| S2 Major    | An important workflow is blocked or substantially degraded for an evidenced scope; workaround absent or costly                       |
| S3 Moderate | A limited failure affects a noncritical path or has a practical workaround                                                           |
| S4 Minor    | Cosmetic or small usability defect with little functional impact                                                                     |
| Unknown     | Evidence does not yet support an impact classification                                                                               |

Assess criticality as well as reach: a narrow but severe data-integrity issue
need not be low severity. Treat suspected security exposure through the
established restricted reporting process; do not publish exploit details in a
general ticket.

## Priority: recommended order of attention

Combine impact with urgency, dependencies, time sensitivity, and available
workarounds. Do not map severity automatically to the same-numbered priority.

| Level        | Suggested interpretation                                                                                      |
| ------------ | ------------------------------------------------------------------------------------------------------------- |
| P0 Immediate | Interrupt normal planning and invoke the established urgent-response process for an active critical situation |
| P1 High      | Address ahead of routine backlog because impact or a supported deadline makes delay costly                    |
| P2 Normal    | Schedule through ordinary planning against other work                                                         |
| P3 Low       | Defer unless capacity, accumulated impact, or new evidence changes its value                                  |
| Unassigned   | Insufficient context or priority reserved for the triage decision                                             |

Recommend a level with a short evidence-based reason. These labels do not define
an SLA, promise a date, page anyone, or override a team's differently numbered
scale. A cosmetic issue may be time-sensitive for an evidenced launch; a severe
historical failure already contained may have different current urgency.

The distinction is informed by
[Atlassian's severity guidance](https://www.atlassian.com/incident-management/kpis/severity-levels/)
and its
[impact/urgency approach to priority](https://support.atlassian.com/jira-service-management-cloud/docs/how-impact-and-urgency-are-used-to-calculate-priority/).
The particular four-level defaults here are local recommendations.

## Confidence and optional size

Record confidence in the recommendation as high (direct, relevant evidence),
medium (partial or indirect evidence), or low (unverified report or major gaps).
This is not a probability calculation. Name the missing evidence that could
change the classification; low confidence does not imply low severity.

Estimate effort only if the team expects it and the work is sufficiently
understood. Use the team's scale first. An optional rough scale is S (bounded
local change), M (several interacting components), L (cross-component
coordination/migration), or Unknown (investigation needed). State assumptions;
never convert these labels into hours, story points, or delivery commitments
without team calibration. Size does not determine severity or priority.

## Next action and readiness

Recommend one next action: investigate, accept for refinement, route to a known
team, link as a possible duplicate, defer, or reject with a supported reason. Do
not close, assign, or transition an issue merely by recommending that action.
For an active critical incident, identify the established incident path if
known; preparing a ticket does not mean response or escalation has occurred.

Check that a triager can understand the problem, see what is evidenced and
unknown, assess impact, and choose a next step. Do not require a feature DoD or
implementation plan to meet this bar. Missing root cause or reproduction can be
acceptable when the available evidence makes an investigation actionable. A
report with neither an identifiable problem nor supporting context needs
clarification.

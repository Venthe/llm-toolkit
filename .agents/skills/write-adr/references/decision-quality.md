# Evaluate an architectural decision record

## Significance and scope

A record is useful when the choice affects enduring boundaries, dependencies,
quality requirements, data ownership, operational responsibilities, or another
costly-to-reverse constraint. Routine local edits usually belong in code or
commit messages. Honor an explicit request for a record even if the choice is
small; scale the detail accordingly.

One record should answer one decision question. Separate independent decisions
when they have different drivers or can change independently; do not split a
single tradeoff into fragments that are hard to understand together.

## Context and rationale

Describe the actual problem and constraints neutrally. Identify which claims are
measured, documented, assumed, or still unknown. A claim such as “faster” needs
a comparison and evidence; do not convert an expectation into a benchmark
result.

Explain the relationship between the drivers and the preferred option. Compare
credible alternatives fairly, including retaining the current approach when
relevant. Avoid invented candidates, arbitrary scores, and a mandatory option
count. State why a disadvantage is acceptable in this context.

## Consequences and uncertainty

Consider supported implications for operations, security boundaries,
compatibility, cost, skills, migration, reversibility, and future changes. These
are prompts, not mandatory headings for every record. Distinguish a required
follow-up from work already completed. Use links to tickets or plans only when
they exist.

If the decision is not made, keep the document proposed and surface the decisive
open question. Ask for missing information only when it prevents a useful draft;
otherwise label assumptions and continue. Do not quietly fill gaps with product
requirements or stakeholder commitments.

## Worked distinction

Input: “We are considering moving session storage to a shared store; we have not
chosen a technology or approved the change.”

A supported draft describes the need and evaluates supplied options as a
proposal. It must not name an accepted vendor, claim measured latency, assign an
approver, or mark an earlier decision superseded. If the user later provides an
accepted choice, record that choice without replaying the approval process.

## Review questions

- Can a maintainer identify exactly what is decided and what remains open?
- Do the rationale and consequences follow from the documented context?
- Are major costs and disadvantages visible alongside benefits?
- Do status, dates, alternatives, and references have an evidentiary basis?
- Does a replacement preserve and link the previous reasoning?
- Is implementation progress clearly separate from decision acceptance?

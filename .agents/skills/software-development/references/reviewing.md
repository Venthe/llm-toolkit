# Review reporting

Scale the report to its useful evidence. Start with actionable findings, then
verification and context; use the user's required format when provided.

## Finding evidence

For each finding, include:

- Location in the reviewed revision: path and line or symbol.
- Observation and the triggering condition, dependency, or invariant.
- Concrete consequence for behavior, maintenance, or feedback.
- Confidence and missing context, including plausible intentional design
  choices.
- A bounded future candidate when helpful, without implementing it.

Order by practical impact. Distinguish demonstrated problems from potential
concerns and neutral observations. Avoid numeric design scores and duplicate
findings from multiple lenses.

Example:

> `OrderService.load` imports the concrete SQL repository. Changing persistence
> requires changing application policy code. A persistence boundary is a
> possible future candidate if database independence is an intended property;
> the current repository does not establish that requirement.

## Verification

Record exact commands and outcomes. Separate passed checks, failed checks,
environmental blockers, and checks not run. Report which revision was executed.
Do not equate test presence with coverage, or a toolchain failure with a code
bug.

## Combined result

Summarize architecture, maintainability, and XP observations only where useful.
Conclude with bounded future candidates and questions that materially affect
their merits. A short statement of no actionable findings is valid; do not
invent concerns to populate every lens or section.

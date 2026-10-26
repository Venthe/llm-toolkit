# Definition of Done menu

Use the original checklist below as the default menu. Select only applicable
items unless the user or team requires the complete checklist. Preserve wording
and hierarchy when selecting items, including the children of "Tested on" and
"Technical description". A supplied team checklist takes precedence.

## Original checklist

- [ ] Feature tests
  - [ ] Unit tests are written and passing
  - [ ] Integration tests are written and passing
  - [ ] Functional specifications are written & tested by automatic tests
  - [ ] System-level Non-Functional requirements (e.g. System-level performance)
        tested and passed
- [ ] Code review
  - [ ] Code review is passed with all questions reconciled
  - [ ] Code does not have Static Analysis issues ranked MAJOR or above
  - [ ] All commits are ready to merge & are succinctly described
  - [ ] Target branch is building with the feature/commit
  - [ ] Any configuration or build changes are documented
  - [ ] TODO/FIXME for the story ID were resolved accordingly
  - [ ] Manual functional tests are passed
  - [ ] Manual exploratory tests are passed
  - [ ] Project deployed on a test environment identical to production platform
  - [ ] (If not covered by automatic functional tests) Feature is tested against
        acceptance criteria
  - [ ] (If not covered by automatic functional tests) non-regression is
        confirmed
  - [ ] All relevant languages are translated
  - [ ] Tested on
    - [ ] Relevant applications
    - [ ] Relevant browsers
    - [ ] Relevant devices
  - [ ] Bugs ranked Major or above are fixed
- [ ] Stakeholder review
  - [ ] Product Owner has had functionality presented and has accepted the
        functionality
  - [ ] UX Designer confirmed the design
  - [ ] Marketing input is done
  - [ ] Documentation updated
  - [ ] Technical description
    - [ ] Public and/or Private API definition updated
- [ ] Functional
  - [ ] Dependent Stories identified and linked
  - [ ] Legal documents are done
  - [ ] Environment variables documented and present in staging & production
        environments.

## Selection and interpretation

- Select test types for the affected behavior and boundaries. Do not require
  every test level on every ticket.
- Include application/browser/device checks and translations when the change
  affects those user surfaces. Retain the "Tested on" parent for selected
  children.
- Include API documentation, configuration, deployment, and environment checks
  when those contracts or environments change.
- Include stakeholder, marketing, dependency, and legal checks only where the
  project context warrants them. Do not invent participants or approvals.
- Keep severity terminology and environment-equivalence requirements from the
  team's checklist. Do not silently weaken "identical" to "representative". If
  an item is not applicable or its meaning is unresolved, explain that instead
  of rewriting it as a different requirement.
- Document environment variable names and provisioning requirements without
  exposing secret values. Checklist inclusion does not authorize deploying or
  changing staging/production.
- Keep selected items unchecked unless completion evidence is supplied. This
  skill defines expected completion, not a claim that it has occurred.

Acceptance criteria describe this ticket's observable outcomes; the DoD
describes applicable completion checks. Read
[acceptance criteria](acceptance-criteria.md) when defining or reviewing the
former.

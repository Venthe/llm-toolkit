# Browser verification

Use for visual comparisons and browser-dependent behavior. JSDOM cannot establish
layout, clipping, scrolling or popup hit testing. Use the project's browser tools
and existing fixtures before building another harness. Review-only execution
boundaries still apply.

## Establish a reproducible comparison

- Record current and baseline revisions, worktrees, browser, dependency versions,
  viewport and device scale. Shared dependencies isolate source changes but do
  not reproduce a baseline's original dependency environment; state that limit.
- Render real components. Mock external boundaries where necessary, recording
  what is mocked. Verify that the harness follows renamed imports and changed
  APIs; stale mocks can create failures or hide behavior. Keep tracking observable
  when reporting counts matter.
- Wait for fonts, images, data and animation completion before screenshots. Use
  bounded readiness checks; do not interpret an intermediate animation frame as
  a layout regression.
- Cover representative loading, error/retry, pending and successful states where
  applicable. Include desktop, mobile and a short viewport when content can grow.
- Assert interaction as well as appearance: open/close, Escape and focus,
  scrolling to actions, tab selection, validation, and actual clicks on popovers
  extending beyond their parent. Inspect fixed headers/footers and overflow.
- Store temporary scripts, screenshots, logs and a small reproducibility manifest
  in the task's `.implementation/` directory or explicitly selected artifact
  location. Preserve prior evidence when regenerating comparisons.

## Report bounded evidence

Record the exact revision/state each check exercised, its outcome, and the
artifact location. Separate product failures from harness or fixture failures.
Do not silently fix source during verification-only work or overwrite expected
results merely to get a passing comparison.

Say "no regressions found in the tested flows" and name those flows. Distinguish
mocked endpoint/component tests from live backend integration, and headless
viewport checks from testing on physical devices. Checks on the completed stack
are not checks on each intermediate branch. Test counts, screenshots and a clean
console alone do not establish unrestricted functional equivalence.

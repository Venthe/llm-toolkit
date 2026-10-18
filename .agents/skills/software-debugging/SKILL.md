---
name: software-debugging
description: Reproduce software failures, discover available runtime evidence, test hypotheses, and isolate root causes. Use for unexpected behavior, crashes, intermittent failures, or unexplained test failures; distinguish diagnosis from implementing a fix.
---

# Software debugging

Build an explanation from observations and discriminating experiments. State what
is known, suspected, and still missing; a plausible code path is not a proven cause.

## Workflow

1. Establish expected and observed behavior, affected version/environment, time
   window, scope, and a failing input or report. Preserve existing work and avoid
   changing several variables at once.
2. Discover the relevant exposed tools and evidence sources for the next question.
   These may include MCP capabilities, debugger access, logs, traces, metrics,
   data sources, CI artifacts, and project skills. Start with local evidence and
   expand discovery as the investigation requires; do not inventory every source
   for a simple reproducible failure. Read [evidence discovery](references/evidence-discovery.md) before
   querying unfamiliar systems. Use actual available interfaces, not assumed names.
3. Reproduce safely, or identify the closest available evidence when reproduction
   is unavailable. Record exact inputs, commands, revisions, and observations.
4. Read [hypotheses and experiments](references/investigation.md) to narrow the
   failure. Form competing explanations and choose a probe whose possible outcomes
   distinguish them. Inspect runtime state when static inspection cannot resolve
   values, branch choices, timing, or call order.
5. Update the explanation after each result. Track disconfirming evidence and
   stop repeating probes that yield no new information. Missing access or data
   is a limitation, not proof that an event did not happen.
6. When fixing is authorized, use [software-development](../software-development/SKILL.md)
   to make the smallest supported correction. Verify the original failure and
   relevant regressions with [software-testing](../software-testing/SKILL.md).
   Preserve the diagnosis scope and any execution constraints when consulting
   these companion skills; a link does not itself authorize edits or checks.
7. Report the symptom, cause or leading hypothesis, supporting evidence, probes
   performed, changes if any, and remaining uncertainty. Distinguish mitigation
   from a root-cause fix.

## Scope and controls

A diagnosis request does not automatically authorize production mutations,
restarts, data repairs, or deployments. Use existing task authorization for safe
inspection and local experiments. Assess debugger pauses, expression side effects,
instrumentation overhead, and query load before using them on shared processes.

Prefer focused observations over bulk dumps. Redact credentials and personal
data. Remove only temporary instrumentation introduced for this task and restore
its settings when finished; preserve the user's breakpoints and diagnostics.
Use specialized debugger skills when discovered and applicable. Do not claim a
debugger session, MCP query, reproduction, or fix verification that did not run.

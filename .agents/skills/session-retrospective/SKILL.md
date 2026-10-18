---
name: session-retrospective
description: "Conduct a retrospective on a coding session."
metadata:
  original-author: https://github.com/mattpocock/skills
  original-license: MIT
  disable-model-invocation: true
---

The user has asked for a **retrospective**. You are suggesting improvements to the coding agent's **environment** to improve future runs.

## Scope

Report evidence-based improvement candidates in order of severity. A retrospective
is diagnostic: do not edit skills, instructions, code, or tooling unless the user
also requests implementation. When implementation is requested, use the relevant
workflow and preserve the review findings as the basis for each change.

## Steps

1. Read the primary sources for the session the user specifies. This may mean searching through session logs on this machine. If the user doesn't specify a session, default to the current one.

2. Look for candidates for improvement in these categories. Keep findings
   specific to the session and prioritize changes with evidence of recurrence
   or material impact; a missing guardrail is not automatically a defect.

- **Navigation**: how easy was it for the agent to find the right files? Are there hidden dependencies between files? Would a **navigation pointer** make it easier? _Use when_ the session took a long time to find a piece of information.
- **Automated checks**: could an existing check have caught a demonstrated error? Inspect the repository's configured checks and CI before recommending a new one. A missing check is a candidate only when the session exposed a recurring or consequential gap; absence of a pre-commit hook or CI job alone is not a defect. Prefer a deterministic check for mechanical rules when it fits the existing toolchain. _Use when_ a concrete error or repeated gap suggests useful automation.
- **Coding standards**: did an agent miss a judgment-based convention that belongs in review guidance? First check whether a relevant rule already exists and whether it was applicable. Prefer the repository's established review guidance; do not introduce a `CODING_STANDARDS.md`, hook, or CI job without evidence that it fits the project and solves a demonstrated problem. _Use when_ a review miss or recurring inconsistency supports a change.
- **Global AGENTS.md**: are there any steering instructions that should be moved to coding standards (or automated checks) instead? _Use when_ the AGENTS.md file is particularly large - in the repo OR the user's global scope.
- **Tool economy**: did the agent make expensive tool calls that could be streamlined? Is there any custom tooling (CLI's, MCP's) that is particularly token-inefficient? _Use when_ the agent made an expensive tool call.
- **No-ops**: look for instructions in steering files that don't modify the agent's behavior. _Use when_ the steering files are large and unwieldy.
- **Information access**: look for opportunities to increase the agent's access to information. Teeing dev server logs, readonly access to third-party services. _Use when_ a crucial piece of information was not available to the agent.
- **Skills**: Look for opportunities to improve the used skills to better help in similar sessions. Read the relevant skill entrypoints and references before recommending changes; use `skill-writing` when assessing or editing skills.

3. Present these candidates to the user, in order of severity.

## Reference

### Implementation vs Review

Remember that all work goes through two stages: implementation and review. The implementation agent has the most **context pressure**. They are responsible for exploration, writing code, and debugging failures.

The review agent has the least context pressure - it receives a diff, so no exploration needed. It often does not need to write code or debug.

This means that the review agent should be responsible for imposing coding standards, not the implementation agent.

### Files

You have access to several files in the repo:

- `CLAUDE.md`/`AGENTS.md`: these files are pushed to the context window of any agent working in this repo. They should be used incredibly sparingly, usually only for **navigation pointers** to other files.
- Repository-specific review guidance: check where the project keeps it before recommending changes. Do not assume a `CODING_STANDARDS.md` file or a separate implementation/review agent lifecycle.
- Docs: use docs as references files, pointed to by other files. Look for existing docs before writing new ones.
- Skills: use skills for reusable workflows and user-invoked tasks. Follow this toolkit's `skill-writing` guidance when changing them; do not assume a `writing-for-agents` skill exists.

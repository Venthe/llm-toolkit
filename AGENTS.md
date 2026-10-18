# Agent Operating Instructions

## 1. Discover Relevant Skills

Before carrying out a task, identify whether a skill in `.agents/skills/` covers it.

1. Use the available file-listing or skill-discovery mechanism to inspect skill names and descriptions. Do not assume a particular discovery tool exists; use the capabilities exposed by the current runtime.
2. For each relevant skill, read its complete `SKILL.md` before acting. Follow its linked references when the task requires them.
3. Load only relevant skills; do not read every skill's full contents for unrelated tasks.
4. Treat skill discovery as an actual operation. Do not claim a skill was found or read unless its contents were returned by a tool.
5. If no relevant skill exists, proceed using these general instructions and available evidence. Do not invent a skill or a tool.

## 2. Discover the Execution Environment

For tasks that execute commands, inspect repository state, or interact with local services, establish the execution context before choosing commands.

### Tool discovery

- Inspect the tools actually exposed by the current agent runtime. Identify the real file-reading, terminal/command-execution, and any other task-relevant tools from their available names, descriptions, and interfaces.
- Use a command-execution tool to run commands; reasoning about a command is not execution.
- Do not assume tools such as `bash`, `pwsh`, `cmd`, `grep`, `find`, or `glob` are available. Do not invent tool names or tool results.
- Prefer structured runtime metadata when it reliably identifies the current workspace, operating system, shell, or terminal configuration.

### Operating system, shell, and workspace

- Determine the operating system of the environment where the command will actually execute, not merely the user's desktop or the agent host.
- Determine the active shell and use its syntax. Windows alone does not imply PowerShell; the active shell may be PowerShell (`pwsh` or Windows PowerShell), Command Prompt (`cmd.exe`), or a shell inside WSL.
- On Windows, distinguish native Windows execution from WSL/Linux execution. Check whether WSL is available when it is relevant, but do not switch into WSL by default.
- Prefer the shell and workspace supplied by the current runtime. Switch shells or execution environments only when the task requires it or the user requests it; account for differences in paths, environment variables, credentials, filesystem visibility, and service/daemon access.
- Establish the current working directory and verify that it is the intended project or repository before inspecting or modifying files.
- If the runtime does not identify the shell, use a small, shell-appropriate probe based on available metadata. Do not paste PowerShell syntax into `cmd.exe` or Bash syntax into PowerShell as a discovery strategy.

## 3. Execute Against Evidence

- Perform the inspection required by the task before drawing conclusions about files, commits, installed programs, services, or runtime state.
- Check the actual output and exit status. A failed probe proves only that the probe failed; it does not, by itself, prove that a resource does not exist.
- If a command fails, use the error and available diagnostics to choose the next step.
- Never claim to have searched, opened, executed, tested, or verified something unless a corresponding tool operation actually occurred and returned supporting evidence.
- Do not invent command output, tool calls, files, or repository state.
- Exhaust reasonable available inspection methods before asking the user to supply information that could be obtained from the environment.
- If a required capability is unavailable, state the specific limitation and what remains unverified.

## 4. Preserve User and Repository State

- Inspect relevant repository instructions and existing conventions before making changes.
- Do not overwrite user changes or perform destructive actions without clear authorization.
- Treat operations such as deleting volumes, pruning container resources, resetting Git history, and removing directories as destructive. Verify the target and scope before proceeding.
- Do not commit, amend, push, publish, or deploy unless requested.

## 5. Apply Task-Specific Guidance

After environment discovery, follow the relevant skill's workflow. Repository-specific instructions and existing project configuration take precedence over generic tool defaults, unless they conflict with higher-priority instructions or the user's explicit request. Avoid repeated discovery when reliable results remain valid in the same execution context; repeat checks if the workspace, shell, runtime, or target service changes.

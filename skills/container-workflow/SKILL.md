---
name: container-workflow
description: >-
  Select and use the appropriate Docker or Podman engine and Compose workflow.
  Use when inspecting, building, running, debugging, or cleaning up repository
  container resources.
---

# Container workflow

## Workflow

1. Inspect project instructions, scripts, CI, container build files, and Compose
   configuration. Establish the actual execution shell and environment.
2. Select the command path in this order: explicit user request, project
   convention, intended service/context, then an available compatible engine.
3. Verify the selected CLI, engine connectivity, and required Compose provider.
   A CLI being installed does not prove its engine is reachable.
4. Inspect configuration using the selected provider's supported config command
   before starting services. Preserve profiles, environment files, project
   names, contexts, networks, volumes, and secrets. Avoid printing resolved
   secret values.
5. Perform the requested operation on the intended resources and verify the
   outcome. A running container does not by itself prove application health.

## Engine and scope constraints

- Probe alternatives only when selection or compatibility remains unresolved. Do
  not silently translate Docker commands to Podman or switch after a failure.
- Windows, WSL, remote contexts, and Podman machines can expose different
  resources and credentials. Verify the intended context; do not launch WSL by
  default or switch contexts globally as a side effect.
- If the requested engine is unavailable, report the actual blocker. If several
  engines work, choose from project evidence; ask only when the choice
  materially affects behavior or resource visibility.
- Inspect exact targets and data-loss consequences before removals. Existing
  authorization must cover destructive operations; broad prune and volume
  deletion are not routine troubleshooting.
- Do not stop unrelated services or install/migrate tooling incidentally. Redact
  credentials in configuration, logs, and inspection output.

Read [Windows and WSL probes](references/windows-and-wsl.md) when selecting
shell-specific commands or diagnosing engine/provider availability on those
platforms. Read [Compose operations](references/compose-operations.md) when
validating, diagnosing, or cleaning up a selected Compose project.

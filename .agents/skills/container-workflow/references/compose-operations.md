# Work with a selected Compose project

Read after identifying the intended engine, context, and project. Examples use
Docker's Compose command; use the selected provider's documented equivalents
only after checking support. Do not translate commands blindly.

## Configuration and diagnosis

- Inspect existing wrappers and preserve their compose files, environment files,
  profiles, project name, and working directory. These affect resource selection.
- Use a quiet validation mode when supported, such as `docker compose config --quiet`.
  Full resolved configuration can reveal secret environment values.
- Inspect only the target services with supported `ps` and bounded `logs`
  commands. Redact credentials; avoid dumping complete inspection output.
- Identify whether failure occurs during config resolution, build, startup, or
  application readiness before changing anything.
- For Podman, verify the external provider selected by `podman compose` and its
  required features. Provider availability and engine reachability are separate.

## Mutations and cleanup

Starting or recreating services may affect persistent data and published ports.
Use the intended project and service scope. Do not create a second Compose file
or stop other projects to get past a conflict.

Before removal, inspect resource ownership, mounted volumes, and authorization.
Removing a container, an image, or a volume has different consequences. Avoid
adding volume deletion or broad prune flags to ordinary stop/restart requests.
After a requested cleanup, inspect remaining target resources and report what
was removed and what could not be verified.

# Windows, PowerShell, CMD, and WSL Reference

Use the command set matching the shell that the execution tool actually runs. These are diagnostic probes; they should not modify repository or container state.

## First: identify the active execution context

Prefer terminal/runtime metadata. If that does not identify the shell, use a probe appropriate to the shell already exposed by the tool. Do not try syntax from every shell in one command block.

## PowerShell (`pwsh` or Windows PowerShell)

```powershell
$PSVersionTable | Format-List
Get-Location
Get-Command pwsh, powershell, cmd, wsl, docker, podman -ErrorAction SilentlyContinue |
    Select-Object Name, CommandType, Source
$env:WSL_DISTRO_NAME
```

`$PSVersionTable` is a dictionary: piping it to `Select-Object` for its keys can
produce blank fields. `Format-List` displays the actual entries.

An empty `WSL_DISTRO_NAME` does not prove WSL is unavailable: that variable is typically set inside a WSL session, not in a native Windows PowerShell session. Run `wsl.exe --list --quiet` only when WSL is relevant and the executable is available. Registration alone does not prove a distribution is running or has the project files.

Choose probes for the selected engine and discovered executables; these blocks
are examples, not a batch to run in full. Check exit status after each native
command (`$LASTEXITCODE` in PowerShell), since a later success can hide a failure.

```powershell
docker version
docker compose version
podman version
podman info
podman compose version
```

A failed command may indicate a missing CLI, an unreachable engine, or a missing Compose provider. Read the error before concluding which one applies. Inspect command resolution if `docker` or `podman` could be an alias, function, or wrapper:

```powershell
Get-Command docker, podman -ErrorAction SilentlyContinue |
    Format-List Name, CommandType, Source, Definition
```

## Command Prompt (`cmd.exe`)

```bat
ver
cd
where pwsh
where powershell
where wsl
where docker
where podman
set WSL_DISTRO_NAME
docker version
docker compose version
podman version
podman info
podman compose version
```

`where` may return a nonzero exit code for a missing executable. A missing `WSL_DISTRO_NAME` variable is not proof WSL is unavailable.

## WSL/Linux shell

Use these only after establishing that the execution tool is running a Linux shell (including a shell inside WSL):

```sh
uname -a
cat /proc/version
printf 'WSL_DISTRO_NAME=%s\n' "${WSL_DISTRO_NAME-}"
printf 'PATH-resolved commands:\n'
command -v bash pwsh cmd.exe docker podman

docker version
docker compose version
podman version
podman info
podman compose version
```

WSL detection clues include `WSL_DISTRO_NAME` and Microsoft/WSL markers in `/proc/version`; use more than one clue if the distinction matters. A Linux container or remote Linux host may also be the terminal environment, so do not assume every Linux shell is WSL.

## Interpret engine checks correctly

- `docker version` should show both client and server details for a working Docker Engine connection. If only client details appear or the command errors, inspect the reported connection failure.
- `podman version` establishes CLI availability; `podman info` checks whether Podman can access its operating environment.
- On Windows, Podman commonly relies on a Podman machine; verify its actual state when `podman info` reports a connection problem.
- `docker compose version` checks Docker Compose plugin availability, not whether the target stack is valid.
- `podman compose version` depends on a Compose provider being installed and usable. Check errors rather than assuming Podman Compose is built in or fully compatible with Docker Compose.
- If both engines work, inspect repository docs, scripts, CI, Compose features, and the intended runtime context before choosing one.
- Do not print complete environment variables or unredacted container inspection output in shared logs; they may contain credentials.

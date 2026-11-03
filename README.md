# LLM Toolkit

Reusable instructions and skills for coding agents. The toolkit captures
practical engineering workflows as Markdown with YAML metadata and optional
supporting resources. There is no application or background service to run.

## Navigate the repository

Start with [AGENTS.md](AGENTS.md), then browse [skills/](skills/). Each
directory's `SKILL.md` describes its purpose, when to use it, and how to load
supporting material. The directory layout is the source of truth for available
skills; this README intentionally does not duplicate that inventory.

```text
skills/<skill-name>/
    SKILL.md           Selection metadata and core workflow
    references/        Topic-specific guidance, when needed
    scripts/           Executable helpers, when needed
    assets/            Output templates, when needed
```

Read the full entrypoint for a relevant skill, then load its references when
their stated conditions apply. Use the target project's conventions and the
tools actually available to your agent. Short skills can remain self-contained.

## Use in another project

Use Node.js 22 or newer and npm. From this checkout, link each skill to its
local source:

```text
npx --yes --package . llm-toolkit install --target /path/to/project --link
npx --yes --package . llm-toolkit update --target /path/to/project --link
npx --yes --package . llm-toolkit remove --target /path/to/project
```

To install copies from GitHub without cloning, omit `--link`:

```text
npx --yes github:Venthe/llm-toolkit install --target /path/to/project
```

Use `update` or `remove` in place of `install` for the other operations. A
GitHub commit or tag can be selected with `github:Venthe/llm-toolkit#<ref>`. No
npm registry publication is required. See the
[npx documentation](https://docs.npmjs.com/cli/v11/commands/npx/).

On Windows, use `npx.cmd` if PowerShell blocks `npx.ps1`. Quote paths containing
spaces. Without `--target`, the current directory is the project. For a direct
local run, use
`node bin/llm-toolkit.js install --target /path/to/project --link`.

To install into `<home>/.agents` from this checkout, pass the home directory as
the target; the installer appends `.agents` automatically.

PowerShell:

```powershell
npx.cmd --yes --package . llm-toolkit install --target "$HOME" --link
```

Bash or Zsh:

```sh
npx --yes --package . llm-toolkit install --target "$HOME" --link
```

The installer copies all bundled skills into `<project>/.agents/skills/` and
Markdown prompts into `<project>/.agents/prompts/`. It creates no symlinks or
junctions by default. Skill identity is its directory name; prompt identity is
its filename. Both `install` and `update` replace matching names completely,
including local edits and extra files inside matching skill directories. Other
names remain untouched. No installation manifest is required.

`remove` deletes skills and prompts whose names match the running package's
collection, including locally edited copies. Names no longer bundled in that
version are left alone. License and attribution files are copied into
`.agents/llm-toolkit/` and removed by `remove`. Empty parent directories may
remain.

Add `--link` to link each skill separately into `.agents/skills/<skill-name>`:

```powershell
npx.cmd --yes --package . llm-toolkit install --target "$HOME" --link
```

The `.agents/skills` directory remains a regular directory. Prompts and license
files are still copied. Windows uses directory junctions; other platforms use
directory symlinks. Links point to the running package's skill directories, so
use a persistent local checkout for this mode. With a remotely fetched package,
links point into npm's cache and break if that cache is removed.

Pass `--link` again on updates to keep link mode. Omit it to replace matching
links with copies. Removal unlinks matching skills without deleting their
source; it does not require `--link`. Matching skill links, including broken
links, can be replaced. Linked parent directories such as `.agents` or
`.agents/skills` remain rejected so operations cannot modify an external
directory through them. Operations assume a single writer and are not
transactional against disk errors or interruption. Prompt discovery varies by
agent; prompts can be read by path.

This source layout follows [gh-stack](https://github.com/github/gh-stack)'s
top-level `skills/` convention. Its installation uses
[`gh skill install`](https://cli.github.com/manual/gh_skill_install); this local
installer additionally manages the toolkit's prompts and removal.

Merge relevant operating guidance into the project's existing `AGENTS.md`;
preserve project-specific instructions. Include [LICENSE](LICENSE) when
redistributing the toolkit or substantial portions of it.

Discovery and invocation syntax depend on the runtime. An agent without
automatic skill discovery can read an entrypoint by path when instructed. Skills
provide guidance within the task's authorization; drafting or reviewing does not
imply permission to commit, publish, or implement a proposal.

## My skills

Install these into the home `.agents` directory without interactive prompts. Run
the toolkit command from this checkout. Requires Node.js 22+, npm, and an
authenticated GitHub CLI with `gh skill install` support.

```powershell
# My toolkit: skills and prompts
npx.cmd --yes --package . llm-toolkit install --target "$HOME" --link

# gh-stack: skill only
gh skill install github/gh-stack gh-stack --dir "$HOME/.agents/skills" --force

# Playwright: skill only, without a global CLI installation
npx.cmd --yes --package @playwright/cli@latest playwright-cli install --skills=agents --global
```

In Bash or Zsh, use `npx` instead of `npx.cmd`. Re-run these commands to refresh
the installed skills; matching local content may be overwritten.

The [gh-stack command](https://cli.github.com/manual/gh_skill_install) installs
its instructions, not the `gh stack` extension. Playwright's
[`--global` skill option](https://playwright.dev/agent-cli/skills) selects the
home directory; it does not globally install the CLI. `npx` downloads the CLI
into npm's cache for the command. This mode skips workspace initialization. To
run Playwright later without a global installation, use
`npx --yes --package @playwright/cli@latest playwright-cli <command>`.

## Maintain and validate

Use [skill-writing](skills/skill-writing/SKILL.md) when changing skills. Its
[validation guide](skills/skill-writing/references/validation.md) documents
prerequisites, commands, checks, and limitations.

Validate after editing metadata, moving resources, or changing local links.
Exercise changed scripts and representative tasks as appropriate. Passing
structural checks does not establish how reliably an agent follows instructions.

Run installer regression tests with `npm test`. They use temporary directories
and do not modify an existing installation.

Update this README when repository usage or layout conventions change; adding a
skill or topic reference does not require a README edit.

## Markdown quality

Markdown is formatted with Prettier 3.5.3 using `proseWrap: "always"` and
checked with markdownlint-cli2 0.17.2. Run these commands from the repository
root:

```text
npx --yes prettier@3.5.3 --check "*.md" "skills/**/*.md" "prompts/**/*.md"
npx --yes markdownlint-cli2@0.17.2 "*.md" "skills/**/*.md" "prompts/**/*.md"
```

To apply the formatter:

```text
npx --yes prettier@3.5.3 --write "*.md" "skills/**/*.md" "prompts/**/*.md"
```

On Windows PowerShell systems that block `npx.ps1`, use `npx.cmd` in place of
`npx`. The configuration keeps the standard lint rules except line-length,
context-dependent heading structure, list-marker spacing, inline template HTML,
emphasis headings, untyped fences, and first-line-heading checks; Prettier or
the repository's document structure governs those cases.

## License

[MIT](LICENSE), copyright 2026 Jacek Lipiec. Linked third-party articles remain
under their respective terms.

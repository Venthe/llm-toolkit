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

Use Node.js 22 or newer and npm. From this checkout:

```text
npx --yes --package . llm-toolkit install --target /path/to/project
npx --yes --package . llm-toolkit update --target /path/to/project
npx --yes --package . llm-toolkit remove --target /path/to/project
```

Once this commit is available on GitHub, you can run without cloning:

```text
npx --yes github:Venthe/llm-toolkit install --target /path/to/project
```

Use `update` or `remove` in place of `install` for the other operations. A
GitHub commit or tag can be selected with `github:Venthe/llm-toolkit#<ref>`. No
npm registry publication is required. See the
[npx documentation](https://docs.npmjs.com/cli/v11/commands/npx/).

On Windows, use `npx.cmd` if PowerShell blocks `npx.ps1`. Quote paths containing
spaces. Without `--target`, the current directory is the project. For a direct
local run, use `node bin/llm-toolkit.js install --target /path/to/project`.

To install into `<home>/.agents` from this checkout, pass the home directory as
the target; the installer appends `.agents` automatically.

PowerShell:

```powershell
npx.cmd --yes --package . llm-toolkit install --target "$HOME"
```

Bash or Zsh:

```sh
npx --yes --package . llm-toolkit install --target "$HOME"
```

The installer copies all bundled skills into `<project>/.agents/skills/` and
Markdown prompts into `<project>/.agents/prompts/`. It creates no symlinks or
junctions. Skill identity is its directory name; prompt identity is its
filename. Both `install` and `update` replace matching names completely,
including local edits and extra files inside matching skill directories. Other
names remain untouched. No installation manifest is required.

`remove` deletes skills and prompts whose names match the running package's
collection, including locally edited copies. Names no longer bundled in that
version are left alone. License and attribution files are copied into
`.agents/llm-toolkit/` and removed by `remove`. Empty parent directories may
remain.

Linked destination paths are rejected so installation cannot modify a link's
external target. Remove existing links manually before installing copies.
Operations assume a single writer and are not transactional against disk errors
or interruption. Prompt discovery varies by agent; prompts can be read by path.

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

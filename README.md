# LLM Toolkit

Reusable instructions and skills for coding agents. The toolkit captures practical
engineering workflows as Markdown with YAML metadata and optional supporting
resources. There is no application or background service to run.

## Navigate the repository

Start with [AGENTS.md](AGENTS.md), then browse [.agents/skills/](.agents/skills/).
Each directory's `SKILL.md` describes its purpose, when to use it, and how to load
supporting material. The directory layout is the source of truth for available
skills; this README intentionally does not duplicate that inventory.

```text
.agents/skills/<skill-name>/
    SKILL.md           Selection metadata and core workflow
    references/        Topic-specific guidance, when needed
    scripts/           Executable helpers, when needed
    assets/            Output templates, when needed
```

Read the full entrypoint for a relevant skill, then load its references when
their stated conditions apply. Use the target project's conventions and the
tools actually available to your agent. Short skills can remain self-contained.

## Use in another project

Copy the chosen skill directories to a location supported by your agent. Keep
their supporting files together and include any companion directories linked by
the entrypoints. Copying the whole collection preserves those dependencies.

Merge relevant operating guidance into the project's existing `AGENTS.md`;
preserve project-specific instructions. Include [LICENSE](LICENSE) when
redistributing the toolkit or substantial portions of it.

Discovery and invocation syntax depend on the runtime. An agent without automatic
skill discovery can read an entrypoint by path when instructed. Skills provide
guidance within the task's authorization; drafting or reviewing does not imply
permission to commit, publish, or implement a proposal.

## Maintain and validate

Use [skill-writing](.agents/skills/skill-writing/SKILL.md) when changing skills.
Its [validation guide](.agents/skills/skill-writing/references/validation.md)
documents prerequisites, commands, checks, and limitations.

Validate after editing metadata, moving resources, or changing local links.
Exercise changed scripts and representative tasks as appropriate. Passing
structural checks does not establish how reliably an agent follows instructions.

Update this README when repository usage or layout conventions change; adding a
skill or topic reference does not require a README edit.

## Markdown quality

Markdown is formatted with Prettier 3.5.3 using `proseWrap: "always"` and
checked with markdownlint-cli2 0.17.2. Run these commands from the repository
root:

```text
npx --yes prettier@3.5.3 --check "*.md" ".agents/**/*.md"
npx --yes markdownlint-cli2@0.17.2 "*.md" ".agents/**/*.md"
```

To apply the formatter:

```text
npx --yes prettier@3.5.3 --write "*.md" ".agents/**/*.md"
```

On Windows PowerShell systems that block `npx.ps1`, use `npx.cmd` in place of
`npx`. The configuration keeps the standard lint rules except line-length,
context-dependent heading structure, inline template HTML, emphasis headings,
untyped fences, and first-line-heading checks; Prettier or the repository's
document structure governs those cases.

## License

[MIT](LICENSE), copyright 2026 Jacek Lipiec. Linked third-party articles remain
under their respective terms.

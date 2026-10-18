---
name: skill-writing
description: Create, evaluate, or improve agent skills and their references, scripts, and templates. Use when authoring SKILL.md, refining skill selection, or checking a skill collection for structural and behavioral quality.
---

# Write and maintain skills

## Workflow

1. Establish the capability, realistic requests, desired output, and boundaries.
   Inspect existing skills before creating an overlapping one. Preserve the
   requested location and runtime; in this toolkit use `..`. Use
   [resource design](references/resource-design.md) to decide whether this is an
   independent workflow, a related mode, or conditional reference material.
2. Write a precise name and description that identify when the skill helps.
   Include a boundary only when it prevents likely confusion with another skill.
3. Keep the core decisions, essential constraints, workflow, and output contract
   in `SKILL.md`. Assume the agent already knows general programming and writing.
4. Split conditional detail using [resource design](references/resource-design.md).
   Link every supporting resource and state when to read, execute, or copy it.
   Keep short skills self-contained when splitting adds no value.
5. Use [the quality checklist](references/quality-checklist.md) to assess routing,
   instruction conflicts, scope, evidence, and realistic failure behavior.
6. Run [the validator](scripts/validate_skills.py) on the skill or collection.
   Fix errors and assess warnings; run changed scripts on meaningful cases.
7. Exercise representative requests, including a nearby request that should not
   activate the skill. Record what was actually observed; structural validation
   alone does not establish behavioral quality. Report remaining untested cases.

## Structural validation

From this repository's root, with Python 3.10+ and PyYAML 6.x installed:

```text
python .agents/skills/skill-writing/scripts/validate_skills.py .agents/skills --docs README.md AGENTS.md
```

For another collection, supply its directory, or a single skill directory.
The script is read-only and does not fetch URLs or execute skill code. It checks
metadata, local Markdown link targets, and reachability of bundled resources.
Exit codes: 0 passes (possibly with warnings), 1 validation failure, 2 usage or
dependency error. See [validator details](references/validation.md) for supported
link syntax and limitations.

Dependencies are declared in [requirements.txt](scripts/requirements.txt).
After changing the validator, run its [regression tests](scripts/test_validate_skills.py):

```text
python -B -m unittest discover -s .agents/skills/skill-writing/scripts -p "test_*.py"
```

## Constraints

A skill does not grant authority to publish, contact people, install software,
or perform destructive operations. Preserve existing user authorization without
adding repeated approval gates. Keep scripts explicit about dependencies, inputs,
outputs, side effects, and failure handling. Do not add unused scaffolding or
product-specific metadata unless the target runtime needs it.

# Workflows

Markdown SOPs that define objectives, required inputs, which tools to use, expected outputs, and edge case handling.

Each workflow is a briefing document — written in plain language, kept current as the system learns.

---

## Trigger Index

Use this table to identify which workflow to load based on the user's request.

| Workflow | When to load |
|----------|-------------|
| [00_project_identity](00_project_identity.md) | Starting fresh / "what is CICFA" / project context / branding / explaining the work |
| [03_bounty_logic](03_bounty_logic.md) | Bounty program operations / open calls / ETH pool / jury process / responsible disclosure |
| [03a_operation_001](03a_operation_001.md) | MOMA.SYM execution / generate + deploy assets / social posts / submission intake / ransom letter |
| [04_philosophical_architecture](04_philosophical_architecture.md) | Manifestos / theoretical framing / artist statements / epistemological grounding |

---

## Conventions

- Each workflow has YAML frontmatter: `name`, `description`, `trigger`, and optionally `skills` and `tools`
- The `skills` field lists skills from `skills/` that the workflow depends on — load them when producing output
- The `tools` field lists Python scripts from `tools/` that the workflow uses
- Workflows evolve. Update them when you discover better methods, constraints, or recurring issues.
- Do not create or overwrite workflows without confirmation.

# Skills

Reusable cross-cutting capabilities that any workflow can reference.

Skills are not workflows (they don't define a full operation) and not tools (they don't execute code). They are **prompt-level knowledge**: shared aesthetic rules, voice guidelines, and reusable patterns that multiple workflows depend on.

## When to load a skill

Load a skill when a workflow references it, or when producing output that must conform to CICFA's established aesthetic/voice.

## Available skills

| Skill | Trigger contexts |
|-------|-----------------|
| [`dwg_identity/`](dwg_identity/SKILL.md) | Always-available background context — load when organizational framing matters: programs (#W3SP, #UHP, #DCP), epics, governance, roles, DWG's philosophical positioning, or any decision about scope and register |
| [`cicfa_aesthetic/`](cicfa_aesthetic/SKILL.md) | Any time you produce copy, HTML, or visual output for CICFA — ransom notes, social posts, manifesto text, site components, open calls |

## Structure

```
skills/
├── README.md               ← this file
└── <skill-name>/
    ├── SKILL.md            ← instructions + when to use
    └── references/         ← supporting docs loaded as needed (optional)
```

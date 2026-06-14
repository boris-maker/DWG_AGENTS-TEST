---
name: Sacred Computer Aesthetic Reference
description: Visual/design guidelines from sacred.computer suggested by a collaborator, and how they apply to CICFA outputs
type: reference
---

Source: https://www.sacred.computer/ (SRCL — terminal-inspired design system)

## Core aesthetic
Terminal-inspired, retro-futuristic, MS-DOS/early computing. IBM AS/400, Nostromo (Alien), Blade Runner 2049 vibes. Rejects contemporary web trends entirely.

## Key principles to adopt across CICFA outputs

**ASCII structural characters over CSS borders**
Use actual terminal box-drawing characters: `─ │ ┌ ┐ └ ┘ ├ ┤ ╔ ═ ╗` instead of `border: 1px solid`. Makes terminal authenticity material, not cosmetic.

**Content density / 64-char column discipline**
Cap data tables at 64 characters wide. Minimize whitespace. Tighten padding to push the "live system" feeling.

**Glyph-based status markers in copy**
Use `▶ ▸ ⭢ // >_ [ERR] [OK]` as inline indicators rather than styled HTML elements. Interface should read as output, not design.

**Typographic hierarchy through repetition, not size**
Avoid dramatic font-size changes. Use density, case, and letter-spacing for hierarchy. Monospace-only.

## What NOT to change
Keep the dark color palette (`#0a0a0a` bg, `#e8e8e8` fg, `#ff2d2d` accent) for core CICFA outputs. The darkness is the message — threat surface, night operations, underground.

## Mercado Central exception
See project_mercado_central_aesthetic.md — Mercado Central should use sacred.computer's light theme instead.

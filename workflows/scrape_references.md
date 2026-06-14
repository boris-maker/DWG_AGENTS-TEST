---
name: scrape-references
description: Scrape key reference websites and store as clean markdown inside the relevant skill's references/ directory. Use this workflow whenever adding a new design reference, updating stale context, researching a target institution's aesthetic, or onboarding a new reference site into the skill library. Trigger when the user says "scrape", "research [site]", "learn from [URL]", "add context from", "update references", or "mirror [site]".
trigger: "scrape reference", "update references", "research [site]", "learn from", "add context from", "mirror site", "aesthetic reference", "fetch reference"
tools: [scrape_reference.py]
skills: []
---

# Scrape References Workflow

Use this workflow to pull content from external reference sites and store it as structured markdown inside the relevant skill's `references/` directory. This is how the skill library gains real context from the web.

## Objective

Scrape a target URL → save clean markdown → add a pointer in the relevant SKILL.md → skill now has live reference context.

## Required Inputs

- Target URL
- Which skill this reference feeds (or "new" if it needs its own home)
- Scrape mode: single page, crawl, or structured extraction

---

## Step 1: Identify the reference

Confirm with the user:
1. What URL to scrape
2. What the reference is for — aesthetic research, institutional target, design system, etc.
3. Which skill it should live under

If the reference doesn't fit an existing skill, note it and consider whether a new skill is warranted (check the skill-creator skill).

---

## Step 2: Run the scrape tool

```bash
python tools/scrape_reference.py \
  --url [URL] \
  --output skills/[skill-name]/references/[filename].md \
  --depth [1 or 2]
```

Use `--depth 2` for design systems or documentation sites where context spans multiple pages.

Use `--extract` when you want structured data rather than raw markdown:
```bash
python tools/scrape_reference.py \
  --url [URL] \
  --output skills/[skill-name]/references/[filename].md \
  --extract "Extract the color palette, typography rules, spacing system, and any component naming conventions"
```

Output lands in `skills/[skill-name]/references/[filename].md`.

---

## Step 3: Review and trim

Read the scraped output. Remove:
- Navigation chrome, cookie banners, footer boilerplate
- Duplicate content from multiple crawled pages
- Anything that isn't useful context (legal text, job listings, etc.)

Add a brief summary header (2–4 sentences) at the top of the file describing what this reference is and why it's here.

---

## Step 4: Update SKILL.md

Add or update the `## References` section in the relevant SKILL.md:

```markdown
## References

- **[filename].md** — [One-line description of what this is and when to read it.]
  Read when: [specific trigger — e.g., "building the light palette / Mercado Central interface"]
```

The pointer tells the model *when* to load the reference, enabling progressive disclosure.

---

## Step 5: Commit the reference

Reference files are tracked in git. Scraping is the only process that should write to `skills/*/references/`. Don't manually edit scraped files — re-scrape to update.

---

## URL Registry

The canonical list of reference sites for this project. Re-scrape when a skill is being revised or when the reference feels stale (every few months for active projects).

| URL | Purpose | Feeds skill | Last scraped |
|-----|---------|-------------|-------------|
| `https://www.sacred.computer/` | SRCL design system — primary source for the Mercado Central light palette aesthetic | `cicfa-aesthetic` | 2026-03-28 |
| `https://deep-web-gallery.github.io/CICFA/` | Live CICFA bounty site — current deployed aesthetic, useful for consistency checks | `cicfa-aesthetic` | 2026-03-28 |

To add a new entry: scrape it, store the output, update SKILL.md, then add a row here.

---

## Edge Cases

**JavaScript-heavy pages:** Firecrawl handles these automatically. If output is empty or malformed, try `--depth 2` which uses the crawl endpoint instead of single-page scrape.

**Rate limits:** Firecrawl free tier allows 500 scrapes/month. For large crawls (depth 3+), check credit balance at firecrawl.dev before running.

**Private/authenticated pages:** Firecrawl cannot access pages behind login. For those, export the content manually and write it directly to the references/ file.

**No FIRECRAWL_API_KEY:** Get a free key at firecrawl.dev and add it to `.env` as `FIRECRAWL_API_KEY=fc-...`.

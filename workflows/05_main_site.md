---
name: dwg-main-site
description: >
  Generate and deploy the main DWG organizational website. Covers identity,
  programs (#W3SP, #UHP, #DCP), active and archived epics, the explainer
  video section, and the Shadow Library link.
trigger:
  - "main site"
  - "DWG website"
  - "org site"
  - "homepage"
  - "about page"
  - "generate site"
  - "update website"
skills:
  - dwg_identity
  - cicfa-aesthetic
tools:
  - generate_dwg_site.py
---

# Workflow: DWG Main Organizational Website

## Objective

Generate the HTML for the main DeepWebGallery organizational homepage and,
when ready, deploy it to GitHub Pages. This is the org-level entry point —
separate from the CICFA bounty site.

---

## Required Inputs

Before running, confirm:

| Field | Where | Notes |
|-------|-------|-------|
| `video_url` | `tools/generate_dwg_site.py` CONFIG | Leave empty until explainer video is produced |
| `video_caption` | CONFIG | Optional — default copy is used if empty |
| Program descriptions | CONFIG | Editable per program |
| Epic entries | CONFIG | Add future epics here |
| `shadow_library_url` | CONFIG | Substack URL |
| Deployment repo path | `deploy_to_gh_pages.py` CONFIG | Set `target_repo` and `source_dir` |

---

## Steps

### 1. Edit CONFIG (if needed)

Open `tools/generate_dwg_site.py`. Update any fields that have changed:
- Program operators or descriptions
- New or closed epics (status: "active" | "archived")
- Video URL (once the explainer video exists)
- Contact alias or governance framing

### 2. Generate the site

```bash
python tools/generate_dwg_site.py
```

Output: `.tmp/dwg_site/index.html`

### 3. Preview

Open `.tmp/dwg_site/index.html` in a browser. Check:
- [ ] Body fade-in works
- [ ] All sections render: About, Programs, Epics, Shadow Library, Footer
- [ ] Video section shows placeholder (or video if URL set)
- [ ] All links are correct (CICFA bounty site, Shadow Library Substack)
- [ ] Hover states on nav use opacity shift (not color change)
- [ ] Monospace font loads correctly
- [ ] Gray/cream palette is consistent throughout
- [ ] Page is NOT indexed (`<meta name="robots" content="noindex, nofollow">`)

### 4. Deploy (when ready)

Configure `deploy_to_gh_pages.py`:
- Set `target_repo` to the local path of the DWG main site GitHub repo
- Set `source_dir` to `.tmp/dwg_site`
- Set `target_branch` and `live_url` for the deployment target
- Set `dry_run = False` when ready to push

```bash
python tools/deploy_to_gh_pages.py
```

---

## Adding the Explainer Video

When the studio/thesis explainer video is ready (like poeticsofencryption.kw-berlin.de/About.html):

1. Upload to YouTube or Vimeo
2. Get the embed URL:
   - YouTube: `https://www.youtube.com/embed/VIDEO_ID`
   - Vimeo: `https://player.vimeo.com/video/VIDEO_ID`
3. Set `video_url` in CONFIG
4. Optionally set `video_caption` with framing text
5. Regenerate and deploy

The video will autoplay muted and the template handles the iframe embed.

---

## Aesthetic Reference

This site uses the cryptic-archival register (distinct from CICFA's dark terminal aesthetic):

| Property | Value |
|----------|-------|
| Background | `#676767` |
| Primary text | `rgba(255,255,207,0.85)` (cream) |
| Font | JetBrains Mono / Courier New |
| Layout | Single column, max 72ch |
| Hover | Opacity shift only — no color change |
| Dividers | 1px cream at 30% opacity |

Reference: [bianjie.systems](https://s02.bianjie.systems/),
[Poetics of Encryption](https://poeticsofencryption.kw-berlin.de/src/html/About.html),
[Rhizome](https://rhizome.org/)

---

## Edge Cases

**New epic to add:**
Add an entry to the `epics` list in CONFIG. Use `"status": "active"` for ongoing,
`"status": "archived"` for completed. Set `"url": None` if no live site.

**Program operator changes:**
Update `"operator"` in the relevant program dict. Use `None` if unassigned.

**Content updates without design changes:**
Edit CONFIG only — no template changes needed.

**Design changes:**
Edit `tools/templates/dwg_main_site.html`. All CSS is inline in the `<style>` block.
No external dependencies except Google Fonts fallback stack.

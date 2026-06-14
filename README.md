# CICFA — Cultural Infrastructure Critical Failure Attack

**Program Code:** DWG-CICFA-01 &nbsp;|&nbsp; **Status:** ![Active](https://img.shields.io/badge/status-ACTIVE-ff2d2d?style=flat-square&labelColor=0a0a0a) &nbsp;|&nbsp; **[→ Web Interface](https://boris-maker.github.io/CICF/)**

---

Making institutions experience the aesthetic, symbolic, and procedural logic of cyber-attacks.

---

## The Program

CICFA operates as an art-world responsible disclosure framework. Participants identify vulnerabilities in cultural institutions — symbolic, structural, or real — and submit them as formal disclosures. The submission is the work. The disclosure is the performance.

**Two registers, both valid:**

```
A — Symbolic / Conceptual   Structural contradictions. Power leaks. Governance exploits.
                             Curatorial blindspots. Institutional critique as vuln disclosure.

B — Technical / White Hat   Real opsec or security findings in the institution's public
                             infrastructure. No exploitation. Submit through CICFA.
                             We handle responsible disclosure. The finding is the art.
```

A real CVE filed as a ransom note is both.

**Reward:** CICFA dashboard credit. Exhibition attribution if selected. No cash. No crypto.

---

## Operation 001 — MOMA.SYM

```
TARGET       Museum of Modern Art (MoMA), New York City
STATUS       Active — Open Call
REGISTER     A + B (dual register accepted)
DEADLINE     TBD
SUBMIT       TBD
```

MoMA has been selected as the first target of the CICFA Bounty Program.

Identify and document a vulnerability in its institutional architecture. Corporate board conflicts. Canon gatekeeping. Labor suppression. Ticketing as access barrier. Or a real opsec failure, submitted through CICFA as friendly ransomware.

**Submit as:** Written document (1–3 pages) / Visual diagram / Web artifact

**→ [Full Brief & Submission Form](https://boris-maker.github.io/CICF/)**

---

## How It Works

This repository is the operational layer of CICFA — built on the WAT framework (Workflows, Agents, Tools):

- **Workflows** (`workflows/`) — Markdown SOPs defining each component: hijack environment, mercado central, bounty logic, active operations
- **Agent** — Reads workflows, orchestrates tools, handles sequencing and edge cases
- **Tools** (`tools/`) — Python scripts that generate deployable assets: open call pages, social posts, email blasts, ransom letters

```bash
# Generate open call page
python3 tools/generate_open_call.py       # → .tmp/open_call.html

# Generate distribution copy
python3 tools/generate_social_posts.py   # → .tmp/social_posts.md
python3 tools/generate_email_blast.py    # → .tmp/email_blast.md

# Generate responsible disclosure letter (white-hat findings only)
python3 tools/generate_ransom_letter.py  # → .tmp/ransom_letter.html
```

Edit the `CONFIG` / `FINDING` dict at the top of each script before running.

---

## Tools

| Script | Output | Purpose |
|--------|--------|---------|
| `tools/generate_open_call.py` | `.tmp/open_call.html` | Static open call page (Jinja2 + countdown timer) |
| `tools/generate_social_posts.py` | `.tmp/social_posts.md` | Instagram caption + X/Twitter thread |
| `tools/generate_email_blast.py` | `.tmp/email_blast.md` | Mailing list email (plain text + HTML) |
| `tools/generate_ransom_letter.py` | `.tmp/ransom_letter.html` | Responsible disclosure notice, styled as ransom note |

**Dependency:** `pip install jinja2`

---

## Ethical Position

> a. The work is about violence, not violent.
> b. It stages symbolic systems, not real-world harm.
> c. It exposes fragility as aesthetic condition.

White-hat technical findings follow responsible disclosure: CICFA notifies the institution before publishing, with a 30-day remediation window. The notification letter is itself an artifact.

---

## Lineage

- [Electronic Disturbance Theater](https://en.wikipedia.org/wiki/Electronic_Disturbance_Theater)
- [Ubermorgen — Digital Hijack](https://www.ubermorgen.com/digital_hijack/hijacksearch.html)
- [Critical Engineering Manifesto](https://criticalengineering.org/es)
- [0100101110101101.org — Biennale.py](https://0100101110101101.org/biennale-py/)
- [!Mediengruppe Bitnik](https://2016.bitnik.org/r/)

---

**Maintained by** [@MarketDepravation](https://github.com/boris-maker) &nbsp;|&nbsp; **License:** [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

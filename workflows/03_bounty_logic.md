---
name: bounty-logic
description: Load for anything related to the CICFA bounty program — generating the bounty site, open call pages, social posts, email blasts, ransom letters, or managing the ETH bounty pool. Also load for any Operation (e.g., Operation 001 / MOMA.SYM) that follows the bounty program structure.
trigger: "bounty", "open call", "MOMA.SYM", "Operation 001", "submission", "vulnerability challenge", "deploy bounty", "ransom letter", "ETH pool", "jury", "exploit challenge", "social posts", "email blast"
skills: [cicfa-aesthetic]
tools: [generate_bounty_site.py, deploy_to_gh_pages.py, generate_open_call.py, generate_social_posts.py, generate_email_blast.py, generate_ransom_letter.py]
---

# Workflow: Bounty Logic — Exploit Challenge Framework
**Component:** CICFA-03
**Status:** Active — Operation 001 running

---

## Conceptual Position

The CICFA Bounty Program sits at the intersection of three frameworks:

```
  Penetration Testing          Crowdsourcing
         ●                          ●
              ↘              ↙
               [ Bug Bounty ]   ← CICFA operates here
```

> "A bug bounty program is a deal offered by many websites, organizations, and software
> developers by which individuals can receive recognition and compensation for reporting
> bugs, especially those pertaining to security vulnerabilities. If no financial reward
> is offered, it is called a **vulnerability disclosure program**."
> — Wikipedia

CICFA runs a **bug bounty program with a live ETH prize pool** — crowdfunded by voluntary contributors — reframed for cultural infrastructure. The target is institutional architecture. The primary currency is attribution and exhibition; the secondary currency is Ethereum.

References:
- [Bug Bounty Program](https://en.wikipedia.org/wiki/Bug_bounty_program)
- [Crowdsourcing](https://en.wikipedia.org/wiki/Crowdsourcing)
- [Penetration Test](https://en.wikipedia.org/wiki/Penetration_test)

---

## Objective
Operate a decentralized bug-bounty program targeting the "symbolic architecture" of cultural institutions. The program runs two simultaneous audiences:

- **Funders** voluntarily contribute ETH to a live, on-chain bounty pool. The act of funding is itself a critical gesture — an assertion that institutional critique has market value.
- **Hunters** submit vulnerability disclosures (conceptual or white-hat technical) wrapped in the CICFA aesthetic. If a submission passes jury review, the bounty pool unlocks and transfers to the submitter.

The program is decentralized in structure: the prize pool is on-chain (transparent, verifiable), the verification protocol is published, the jury is named. No hidden process.

---

## Dual Register Framework

Every operation runs on two registers that can coexist in a single submission:

**Register A — Symbolic / Conceptual**
Structural contradictions, power leaks, governance exploits, curatorial blindspots. Institutional critique as vulnerability disclosure.

**Register B — Technical / Operational (White Hat)**
Real security or opsec findings in the target's public digital infrastructure. Submitted through CICFA, dramatized as "friendly ransomware." No exploitation, no harm — the act of surfacing the flaw is the work. Real findings follow responsible disclosure: CICFA notifies the institution via a styled ransom letter before publishing.

---

## Reward Structure

**Primary (Financial):**
- ETH bounty pool — crowdfunded, held in a public Ethereum address
- Transferred to winning submitter on jury approval
- Balance visible on-chain (Etherscan) and displayed live on the bounty site

**Secondary (Cultural):**
- CICFA public credit on the program dashboard
- Exhibition attribution if selected for display
- The naming of the vulnerability enters the archive — the archive is the work

**Jury Verification (Unlock Conditions):**
1. Submission discloses a genuine vulnerability in the target's institutional architecture
2. Sufficient detail to verify the finding (vague claims do not qualify)
3. Passes review by the CICFA Jury (simple majority)
4. [Register B only] Survives 30-day responsible disclosure window without retraction
5. On approval: ETH transferred from bounty pool to submitter's provided address

**Jury composition:** Named, public. Announced before the submission deadline. Typically 3–5 members including @MarketDepravation.

---

## Operation 001 Inputs

| Field | Value |
|-------|-------|
| Target | MoMA (Museum of Modern Art, NYC) |
| Operation name | MOMA.SYM |
| Submission formats | Written document, visual/diagram, web artifact |
| Deadline | TBD |
| Submission URL | TBD (Google Form or email) |
| Distribution | GitHub Pages + Instagram + X/Twitter + mailing list |

---

## Review / Jury Process
1. Submissions collected via intake form into `.tmp/` archive
2. Jury reviews all submissions (see Reward Structure for unlock conditions)
3. Jury vote: simple majority required to approve
4. Winning submitter notified; ETH transfer confirmed with @MarketDepravation before execution
5. All submissions notified for archive/exhibition inclusion
6. White-hat technical findings (Register B) trigger ransom letter workflow before publication

---

## Tools
| Tool | Purpose |
|------|---------|
| `tools/generate_bounty_site.py` | **Main site** — full bounty program page with live ETH pool, two-audience layout, shock effects. Deploys to GitHub Pages. |
| `tools/deploy_to_gh_pages.py` | Deploys `.tmp/bounty_site/` to the CICF repo's gh-pages branch |
| `tools/generate_open_call.py` | Secondary asset — minimal HTML open call page |
| `tools/generate_social_posts.py` | Outputs social copy (Instagram + X/Twitter) |
| `tools/generate_email_blast.py` | Outputs email template for mailing list |
| `tools/generate_ransom_letter.py` | Renders responsible disclosure as styled ransom note (Register B) |

---

## Expected Outputs Per Operation
- Deployed bounty site (GitHub Pages) — primary public interface
- Live ETH bounty pool (on-chain, public address)
- Social posts published
- Email distributed to mailing list
- Submission archive in `.tmp/`
- Jury review → winner notification → ETH transfer
- Selected submissions → exhibition

---

## Edge Cases / Notes
- All symbolic submissions are valid regardless of technical depth
- White-hat technical submissions must not include working exploit code — findings only
- Responsible disclosure window: notify institution, allow 30 days before publishing
- Archive doubles as the artwork

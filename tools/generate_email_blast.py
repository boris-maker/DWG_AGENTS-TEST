#!/usr/bin/env python3
"""
generate_email_blast.py
CICFA — Generates plain-text + HTML email template for mailing list distribution.
Output: .tmp/email_blast.md
"""

from pathlib import Path
from datetime import datetime

# ── CONFIG ────────────────────────────────────────────────────────────────────

CONFIG = {
    "operation_id":   "001",
    "operation_name": "MOMA.SYM",
    "target_name":    "Museum of Modern Art (MoMA)",
    "open_call_url":  "https://boris-maker.github.io/CICF/",  # update when live
    "submission_url": "#",                                      # update with form link
    "deadline":       "TBD",
    "sender_name":    "@MarketDepravation",
    "sender_email":   "",   # fill in before sending
}

# ── COPY ──────────────────────────────────────────────────────────────────────

def subject_line(c: dict) -> str:
    return f"CICFA OPEN CALL // {c['operation_name']} // Vulnerability Disclosure Program"


def plain_text(c: dict) -> str:
    return f"""CICFA BOUNTY PROGRAM — OPERATION {c["operation_id"]}
{c["operation_name"]} // Target: {c["target_name"]}
———————————————————————————————————————

You are receiving this because you are part of the CICFA collaborator network.

We are running the first operation of the CICFA Bounty Program.

TARGET: {c["target_name"]}

We invite you to identify and document a vulnerability in its institutional architecture.

TWO REGISTERS — BOTH VALID:

[A] Symbolic / Conceptual
A structural contradiction. A power leak. A governance exploit. A curatorial blindspot.
Institutional critique as vulnerability disclosure.

[B] Technical / Operational (White Hat)
A real opsec or security finding in the institution's public infrastructure.
No exploitation. No harm. Submit through CICFA. We handle responsible disclosure.
The act of surfacing the flaw is the work.

Submissions can operate in one or both registers simultaneously.

———————————————————————————————————————
SUBMIT AS:
• Written document — 1–3 pages, any style
• Visual / diagram — attack surface map, power flow, annotated org chart
• Web artifact — link to hosted version + screenshot

REWARD:
CICFA dashboard credit.
Exhibition attribution if selected for display.
No cash.

DEADLINE: {c["deadline"]}

Full brief + submission form:
{c["open_call_url"]}

———————————————————————————————————————
The work is about violence, not violent.
It stages symbolic systems, not real-world harm.
It exposes fragility as aesthetic condition.

— {c["sender_name"]}
CICFA / DWG-CICFA-01
{c["open_call_url"]}
"""


def html_body(c: dict) -> str:
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  body {{ font-family: 'Courier New', monospace; background: #0a0a0a; color: #e8e8e8;
          max-width: 640px; margin: 0 auto; padding: 2rem; font-size: 13px; line-height: 1.7; }}
  h1 {{ color: #ff2d2d; font-size: 1.1rem; letter-spacing: 0.1em; text-transform: uppercase; }}
  h2 {{ color: #ff2d2d; font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase;
        border-left: 2px solid #ff2d2d; padding-left: 0.75rem; margin: 1.5rem 0 0.5rem; }}
  .meta {{ color: #555; font-size: 11px; margin-bottom: 1.5rem; }}
  .register {{ border: 1px solid #222; padding: 0.75rem; margin: 0.5rem 0; background: #111; }}
  .reg-label {{ color: #ff2d2d; font-size: 10px; letter-spacing: 0.15em; text-transform: uppercase; }}
  .cta {{ display: block; background: #ff2d2d; color: #000; padding: 0.75rem 1.5rem;
          text-align: center; text-decoration: none; font-weight: bold;
          letter-spacing: 0.1em; text-transform: uppercase; margin: 1.5rem 0; }}
  .footer {{ color: #444; font-size: 11px; border-top: 1px solid #222; padding-top: 1rem; margin-top: 2rem; }}
  hr {{ border: none; border-top: 1px solid #222; margin: 1.5rem 0; }}
</style>
</head>
<body>
<p class="meta">CICFA // BOUNTY PROGRAM // OPERATION {c["operation_id"]}</p>
<h1>{c["operation_name"]}</h1>
<p>Target: <strong style="color:#fff">{c["target_name"]}</strong></p>

<p>We are running the first operation of the CICFA Bounty Program. You are invited to identify
and document a vulnerability in {c["target_name"]}'s institutional architecture.</p>

<h2>Two Registers</h2>
<div class="register">
  <div class="reg-label">A — Symbolic / Conceptual</div>
  <p>A structural contradiction. A power leak. A governance exploit. A curatorial blindspot.
  Institutional critique as vulnerability disclosure.</p>
</div>
<div class="register">
  <div class="reg-label">B — Technical / Operational (White Hat)</div>
  <p>A real opsec or security finding in the institution's public infrastructure.
  No exploitation. No harm. Submit through CICFA — we handle responsible disclosure.
  The act of surfacing the flaw is the work.</p>
</div>
<p style="color:#555; font-size:12px;">Both registers are valid. They can coexist in one submission.</p>

<h2>Submit As</h2>
<ul>
  <li>Written document — 1–3 pages, any style</li>
  <li>Visual / diagram — attack surface map, power flow, annotated org chart</li>
  <li>Web artifact — link to hosted version + screenshot</li>
</ul>

<h2>Reward</h2>
<p>CICFA dashboard credit. Exhibition attribution if selected for display. No cash.</p>

<p>Deadline: <strong style="color:#ff2d2d">{c["deadline"]}</strong></p>

<a href="{c["open_call_url"]}" class="cta">View Full Brief &amp; Submit &rarr;</a>

<hr>
<div class="footer">
  <p>The work is about violence, not violent. It stages symbolic systems, not real-world harm.
  It exposes fragility as aesthetic condition.</p>
  <p style="margin-top:0.5rem;">— {c["sender_name"]} // CICFA // DWG-CICFA-01</p>
</div>
</body>
</html>"""

# ── OUTPUT ────────────────────────────────────────────────────────────────────

def main():
    output_dir = Path(__file__).parent.parent / ".tmp"
    output_dir.mkdir(exist_ok=True)

    c = CONFIG
    lines = [
        f"# Email Blast — Operation {c['operation_id']}: {c['operation_name']}",
        f"_Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}_",
        "",
        "---",
        "",
        f"## Subject Line",
        "",
        f"`{subject_line(c)}`",
        "",
        "---",
        "",
        "## Plain Text Body",
        "",
        "```",
        plain_text(c),
        "```",
        "",
        "---",
        "",
        "## HTML Body",
        "",
        "```html",
        html_body(c),
        "```",
    ]

    output_path = output_dir / "email_blast.md"
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[OK] Email blast generated: {output_path}")

if __name__ == "__main__":
    main()

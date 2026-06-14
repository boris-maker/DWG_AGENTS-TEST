#!/usr/bin/env python3
"""
generate_ransom_letter.py
CICFA — Generates a styled responsible disclosure "ransom letter" for white-hat findings.
This letter is sent to the target institution as part of the performance before publishing.
Output: .tmp/ransom_letter.html

Usage: Edit the FINDING dict below, then run:
  python tools/generate_ransom_letter.py
"""

from pathlib import Path
from datetime import datetime

# ── FINDING CONFIG ────────────────────────────────────────────────────────────
# Fill in the details of the white-hat finding before running.

FINDING = {
    "operation_id":       "001",
    "operation_name":     "MOMA.SYM",
    "target_name":        "Museum of Modern Art",
    "target_contact":     "security@moma.org",   # or general contact if no security email
    "submitted_by":       "[SUBMITTER HANDLE]",   # CICFA-assigned handle, not real name unless consented
    "finding_title":      "[FINDING TITLE]",
    "finding_summary":    "[Brief plain-language description of the finding. 2–4 sentences.]",
    "finding_detail":     "[Full technical or structural detail. What was found, where, and how.]",
    "severity":           "[Critical / High / Medium / Low / Informational]",
    "register":           "B",    # A, B, or A+B
    "disclosure_date":    "",     # ISO 8601: "2026-03-16" — date this letter is sent
    "publish_date":       "",     # ISO 8601: "2026-04-16" — 30 days later
    "cicfa_url":          "https://boris-maker.github.io/CICF/",
}

# ── RENDER ────────────────────────────────────────────────────────────────────

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>CICFA Responsible Disclosure — {operation_name}</title>
<style>
  :root {{
    --bg: #0a0a0a; --fg: #e8e8e8; --accent: #ff2d2d;
    --dim: #555; --border: #222; --mono: 'Courier New', monospace;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: var(--bg); color: var(--fg); font-family: var(--mono);
    font-size: 13px; line-height: 1.8; padding: 2rem;
    max-width: 800px; margin: 0 auto;
  }}
  .letterhead {{
    border: 1px solid var(--accent); padding: 1.5rem; margin-bottom: 2rem;
    background: #0f0000;
  }}
  .letterhead .from {{ color: var(--dim); font-size: 11px; letter-spacing: 0.15em;
    text-transform: uppercase; margin-bottom: 0.5rem; }}
  .letterhead .title {{ color: #fff; font-size: 1.2rem; letter-spacing: 0.05em; }}
  .letterhead .sub {{ color: var(--accent); font-size: 11px; margin-top: 0.25rem; }}
  .meta-grid {{
    display: grid; grid-template-columns: 160px 1fr; gap: 0.3rem;
    margin: 1.5rem 0; font-size: 12px;
  }}
  .meta-label {{ color: var(--dim); text-transform: uppercase;
    letter-spacing: 0.1em; font-size: 10px; padding-top: 2px; }}
  .severity-critical {{ color: #ff2d2d; }}
  .severity-high {{ color: #ff7700; }}
  .severity-medium {{ color: #ffcc00; }}
  .severity-low {{ color: #88cc88; }}
  .severity-informational {{ color: var(--dim); }}
  h2 {{
    color: var(--accent); font-size: 0.8rem; letter-spacing: 0.2em;
    text-transform: uppercase; border-left: 2px solid var(--accent);
    padding-left: 0.75rem; margin: 2rem 0 0.75rem;
  }}
  p {{ margin-bottom: 1rem; }}
  .finding-box {{
    border: 1px solid var(--border); padding: 1.25rem; background: #111;
    margin: 1rem 0; white-space: pre-wrap; font-size: 12px;
  }}
  .timeline {{
    display: grid; grid-template-columns: 160px 1fr; gap: 0.5rem;
    margin: 1rem 0; font-size: 12px;
  }}
  .timeline-label {{ color: var(--dim); }}
  .signature {{
    margin-top: 2.5rem; padding-top: 1.5rem; border-top: 1px solid var(--border);
    color: var(--dim); font-size: 11px;
  }}
  .stamp {{
    display: inline-block; border: 2px solid var(--accent); padding: 0.3rem 0.75rem;
    color: var(--accent); letter-spacing: 0.2em; text-transform: uppercase;
    font-size: 11px; margin-top: 1rem; opacity: 0.7;
  }}
</style>
</head>
<body>

<div class="letterhead">
  <div class="from">From: CICFA // Cultural Infrastructure Critical Failure Attack</div>
  <div class="title">RESPONSIBLE DISCLOSURE NOTICE</div>
  <div class="sub">Operation {operation_id} — {operation_name} // Register {register}</div>
</div>

<p>To: <strong>{target_name}</strong> &lt;{target_contact}&gt;<br>
Date: {disclosure_date}<br>
Re: Vulnerability disclosure — CICFA Operation {operation_id}</p>

<p>This notice is issued as part of the <strong>CICFA Bounty Program</strong>, an art-world
responsible disclosure framework operating in the intersection of net.art, institutional
critique, and white-hat security practice. A vulnerability in your institution's
infrastructure has been submitted to us by a program participant and is being disclosed
to you in good faith prior to public archival.</p>

<p>No exploitation has occurred or will occur. This disclosure is the work.</p>

<h2>Finding Summary</h2>

<div class="meta-grid">
  <span class="meta-label">Title</span>
  <span>{finding_title}</span>

  <span class="meta-label">Submitted by</span>
  <span>{submitted_by}</span>

  <span class="meta-label">Severity</span>
  <span class="severity-{severity_lower}">{severity}</span>

  <span class="meta-label">Register</span>
  <span>{register_label}</span>
</div>

<p>{finding_summary}</p>

<h2>Technical / Structural Detail</h2>
<div class="finding-box">{finding_detail}</div>

<h2>Disclosure Timeline</h2>
<div class="timeline">
  <span class="timeline-label">Notice sent</span>
  <span>{disclosure_date}</span>

  <span class="timeline-label">Response window</span>
  <span>30 days</span>

  <span class="timeline-label">Scheduled publication</span>
  <span>{publish_date} — CICFA archive + exhibition</span>
</div>

<p>We encourage you to acknowledge receipt and, if appropriate, remediate the finding
before the publication date. Acknowledgement is not required for publication to proceed.</p>

<p>The ransom: none. The publication: certain. The performance: already underway.</p>

<div class="signature">
  <p>CICFA — Cultural Infrastructure Critical Failure Attack<br>
  @MarketDepravation // DWG-CICFA-01<br>
  <a href="{cicfa_url}" style="color: var(--dim);">{cicfa_url}</a></p>

  <div class="stamp">Friendly Ransomware // No Harm Intended</div>
</div>

</body>
</html>"""

REGISTER_LABELS = {
    "A":   "A — Symbolic / Conceptual",
    "B":   "B — Technical / Operational (White Hat)",
    "A+B": "A + B — Dual Register",
}

def main():
    output_dir = Path(__file__).parent.parent / ".tmp"
    output_dir.mkdir(exist_ok=True)

    f = FINDING.copy()
    f["disclosure_date"] = f["disclosure_date"] or datetime.now().strftime("%Y-%m-%d")
    f["severity_lower"] = f["severity"].lower().split("/")[0].strip()
    f["register_label"] = REGISTER_LABELS.get(f["register"], f["register"])

    rendered = HTML_TEMPLATE.format(**f)

    output_path = output_dir / "ransom_letter.html"
    output_path.write_text(rendered, encoding="utf-8")
    print(f"[OK] Ransom letter generated: {output_path}")

if __name__ == "__main__":
    main()

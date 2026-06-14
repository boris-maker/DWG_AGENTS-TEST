#!/usr/bin/env python3
"""
generate_open_call.py
CICFA — Generates a static HTML open call page from the Jinja2 template.
Output: .tmp/open_call.html
"""

import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# ── CONFIG ────────────────────────────────────────────────────────────────────
# Edit these values before running.

CONFIG = {
    "operation_id":    "001",
    "operation_name":  "MOMA.SYM",
    "target_name":     "Museum of Modern Art",
    "target_location": "New York City, USA",
    "brief_html": """
        <p>MoMA has been selected as the first target of the CICFA Bounty Program.</p>
        <p>You are invited to identify and document a vulnerability in its institutional
        architecture — symbolic, structural, or technical. Who gets shown? Who funds the
        walls? What disappears between the press release and the permanent collection?
        Where does the opsec fail?</p>
        <p>Surface the flaw. Submit the disclosure. The act of naming it is the work.</p>
    """,
    # Leave deadline fields empty ("") to hide the countdown timer.
    "deadline_iso":     "",          # ISO 8601 format: "2026-04-30T23:59:00Z"
    "deadline_display": "",          # Human-readable: "30 April 2026, 23:59 UTC"
    "submission_url":   "#",         # Replace with live Google Form or email link
    "cicfa_url":        "https://boris-maker.github.io/CICF/",
}

# ── RENDER ────────────────────────────────────────────────────────────────────

def main():
    base_dir = Path(__file__).parent
    template_dir = base_dir / "templates"
    output_dir = base_dir.parent / ".tmp"
    output_dir.mkdir(exist_ok=True)

    env = Environment(loader=FileSystemLoader(str(template_dir)))
    template = env.get_template("open_call.html")
    rendered = template.render(**CONFIG)

    output_path = output_dir / "open_call.html"
    output_path.write_text(rendered, encoding="utf-8")
    print(f"[OK] Open call generated: {output_path}")

if __name__ == "__main__":
    main()

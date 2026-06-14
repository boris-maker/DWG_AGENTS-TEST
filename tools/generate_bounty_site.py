#!/usr/bin/env python3
"""
generate_bounty_site.py
CICFA — Generates the full bounty program website from the Jinja2 template.
Output: .tmp/bounty_site/index.html

Two audiences:
  - FUNDERS:  contribute ETH to the live on-chain prize pool
  - HUNTERS:  take the challenge, earn the bounty if jury-approved

Edit CONFIG before running. Wallet address, jury, and submission URL
must be set before deployment — see workflows/03a_operation_001.md.
"""

import json
from pathlib import Path
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

# ── CONFIG ──────────────────────────────────────────────────────────────────
# Edit these values before running. See workflows/03_bounty_logic.md for
# field descriptions and constraints.

CONFIG = {
    # ── Operation metadata ──────────────────────────────────────────────────
    "operation_id":       "001",
    "operation_name":     "MOMA.SYM",
    "operation_status":   "ACTIVE",        # "ACTIVE" | "CLASSIFIED" | "CLOSED"
    "program_code":       "DWG-CICFA-01",

    # ── Target ──────────────────────────────────────────────────────────────
    "target_name":        "Museum of Modern Art",
    "target_alias":       "MoMA",
    "target_location":    "New York City, USA",

    # ── Bounty pool (ETH) ───────────────────────────────────────────────────
    "wallet_address":     "0x7fC76C439c200151Dde0345B09BA02764B9143Ec",
    "wallet_ens":         "",              # e.g. "cicfa.eth" — add when registered
    "rpc_url":            "https://cloudflare-eth.com",   # free public RPC
    "target_amount_eth":  1.0,             # goal amount for progress bar

    # Contributors list — update manually when deposits arrive.
    # Each entry: {"handle": str, "amount": str}
    # Use "@anon" for anonymous contributors.
    "contributors": [
        # {"handle": "@example", "amount": "0.1"},
    ],

    # ── Jury — SELF-ASSEMBLING ───────────────────────────────────────────────
    # Jury seats are open. First volunteers to register via GitHub Issues
    # (submitting their ETH wallet address) become jurors.
    # Votes are registered on-chain: jurors sign a message with their wallet.
    # Each entry once registered: {"handle": str, "wallet": str, "role": str, "affiliation": str}
    "jury": [
        # {"handle": "@boris-maker", "wallet": "0x...", "role": "Lead Curator", "affiliation": "CICFA"},
    ],
    "jury_seats_open":    True,           # False once jury is sealed
    "jury_max_seats":     5,              # max jury members
    "jury_registration_url": "https://github.com/DEEP-WEB-GALLERY/CICFA/issues/new?template=jury_registration.yml",

    # ── Deadline ────────────────────────────────────────────────────────────
    # Leave both empty ("") to hide the countdown timer.
    "deadline_iso":       "",              # ISO 8601: "2026-05-31T23:59:00Z"
    "deadline_display":   "",             # Human: "31 May 2026, 23:59 UTC"

    # ── URLs ────────────────────────────────────────────────────────────────
    "submission_url":     "https://github.com/DEEP-WEB-GALLERY/CICFA/issues/new?template=submission.yml",
    "cicfa_url":          "https://deep-web-gallery.github.io/CICFA/",

    # ── Copy ────────────────────────────────────────────────────────────────
    "brief_html": """
        <p>MoMA has been selected as the first target of the CICFA Bounty Program.</p>
        <p>You are invited to identify and document a vulnerability in its institutional
        architecture — symbolic, structural, or technical. Who gets shown? Who funds the
        walls? What disappears between the press release and the permanent collection?
        Where does the opsec fail?</p>
        <p>Surface the flaw. Submit the disclosure. The act of naming it is the work.
        If the jury verifies it — the bounty is yours.</p>
    """,

    # brief_text: plain-text version used as data-original attribute (for glitch effect).
    # Keep it short — one sentence.
    "brief_text": "Surface the flaw. Submit the disclosure. The act of naming it is the work.",

    # Boot sequence lines — typed one by one on page load.
    "boot_lines": [
        "CICFA OS v2.1.4 — booting...",
        "initializing exploit_surface_scanner...",
        "loading institutional_memory_core...",
        "target_lock: MUSEUM OF MODERN ART [CONFIRMED]",
        "operation_id: 001 // MOMA.SYM",
        "bounty_pool: LIVE — checking on-chain balance...",
        "jury_status: ASSEMBLED",
        "status: BREACH WINDOW OPEN",
        "WARNING: INSTITUTIONAL ARCHITECTURE UNSTABLE",
        "connecting to bounty_relay_network...",
        "CICFA SYSTEM ONLINE.",
    ],

    # Alert bar scrolling text (doubled internally for seamless loop).
    "alert_text": (
        "⚠ WARNING: INSTITUTIONAL ARCHITECTURE COMPROMISED // "
        "BREACH WINDOW: ACTIVE // "
        "OPERATION 001 IN PROGRESS // "
        "TARGET: MUSEUM OF MODERN ART // "
        "REGISTER A+B OPEN // "
        "SUBMIT YOUR FINDINGS // "
        "BOUNTY POOL LIVE //"
    ),

    # ── Page metadata ────────────────────────────────────────────────────────
    "page_title":         "MOMA.SYM — CICFA Bounty Program",
    "meta_description":   (
        "CICFA Operation 001: decentralized bug bounty targeting MoMA's "
        "institutional architecture. Fund the pot or take the challenge."
    ),
    "author":             "@MarketDepravation",
}

# ── RENDER ───────────────────────────────────────────────────────────────────

def main():
    base_dir     = Path(__file__).parent
    template_dir = base_dir / "templates"
    output_dir   = base_dir.parent / ".tmp" / "bounty_site"
    output_dir.mkdir(parents=True, exist_ok=True)

    env      = Environment(loader=FileSystemLoader(str(template_dir)))
    template = env.get_template("bounty_site.html")

    ctx = dict(CONFIG)
    ctx["generated_at"] = datetime.now().isoformat()

    rendered = template.render(**ctx)

    output_path = output_dir / "index.html"
    output_path.write_text(rendered, encoding="utf-8")

    print(f"[OK] Bounty site generated: {output_path}")
    print()

    # Warn on any TBD fields
    warnings = []
    if not CONFIG["wallet_address"]:
        warnings.append("wallet_address is not set — fund CTA will show placeholder")
    if CONFIG["jury_seats_open"] and not CONFIG["jury"]:
        print("[i] Jury seats are open — first volunteers to register become jurors.")
    elif not CONFIG["jury"]:
        warnings.append("jury is empty — jury section will show TBD placeholder")
    if not CONFIG["submission_url"] or CONFIG["submission_url"] == "#":
        warnings.append("submission_url is not set — submit button goes nowhere")
    if not CONFIG["deadline_iso"]:
        warnings.append("deadline_iso is not set — countdown will be hidden")

    if warnings:
        print("[!] Pre-deploy checklist — set these before going live:")
        for w in warnings:
            print(f"    — {w}")
        print()

    print(f"[?] Preview: open .tmp/bounty_site/index.html in your browser")
    print(f"[?] Deploy:  python tools/deploy_to_gh_pages.py")


if __name__ == "__main__":
    main()

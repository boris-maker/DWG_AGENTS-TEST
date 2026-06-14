#!/usr/bin/env python3
"""
generate_social_posts.py
CICFA — Generates social post copy for Instagram and X/Twitter.
Output: .tmp/social_posts.md
"""

from pathlib import Path
from datetime import datetime

# ── CONFIG ────────────────────────────────────────────────────────────────────

CONFIG = {
    "operation_id":    "001",
    "operation_name":  "MOMA.SYM",
    "target_name":     "Museum of Modern Art (MoMA)",
    "open_call_url":   "https://boris-maker.github.io/CICF/",  # update when live
    "submission_url":  "#",                                      # update with form link
    "deadline":        "TBD",
}

INSTAGRAM_HASHTAGS = [
    "#CICFA", "#NetArt", "#InstitutionalCritique", "#OpenCall",
    "#ArtAndTechnology", "#HacktivismAsArt", "#ConceptualArt",
    "#MarketDepravation", "#MOMASYM", "#ArtCall",
]

# ── COPY ──────────────────────────────────────────────────────────────────────

def instagram_caption(c: dict) -> str:
    return f"""OPEN CALL // OPERATION {c["operation_id"]}

{c["operation_name"]}
Target: {c["target_name"]}

CICFA is running its first Bounty Program operation.

We're inviting you to identify and document a vulnerability in MoMA's institutional architecture.

Symbolic. Structural. Technical (white hat).
A curatorial blindspot. A governance exploit. A real opsec failure, submitted through CICFA as friendly ransomware.

Submit: Written document / Visual diagram / Web artifact
Reward: CICFA dashboard credit + exhibition attribution if selected

Deadline: {c["deadline"]}

Link in bio → {c["open_call_url"]}

—

{" ".join(INSTAGRAM_HASHTAGS)}"""


def twitter_thread(c: dict) -> list[str]:
    return [
        f"""🔴 OPEN CALL — OPERATION {c["operation_id"]}

{c["operation_name"]}
Target: {c["target_name"]}

CICFA is running its first Bounty Program.

Identify a vulnerability in MoMA's institutional architecture. Submit it. Get credited.

[1/3]""",

        f"""Two registers. Both valid. They can coexist.

A — Symbolic: power leaks, governance exploits, curatorial blindspots. Institutional critique as vulnerability disclosure.

B — Technical (white hat): a real opsec or security finding. Submit through CICFA. We handle responsible disclosure. The act of surfacing it is the work.

[2/3]""",

        f"""Submit: written doc / visual diagram / web artifact

Reward: CICFA dashboard credit. Exhibition attribution if selected. No cash.

Deadline: {c["deadline"]}
Full brief → {c["open_call_url"]}

#CICFA #NetArt #InstitutionalCritique #OpenCall

[3/3]""",
    ]


# ── OUTPUT ────────────────────────────────────────────────────────────────────

def main():
    output_dir = Path(__file__).parent.parent / ".tmp"
    output_dir.mkdir(exist_ok=True)

    c = CONFIG
    thread = twitter_thread(c)

    lines = [
        f"# Social Posts — Operation {c['operation_id']}: {c['operation_name']}",
        f"_Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}_",
        "",
        "---",
        "",
        "## Instagram Caption",
        "",
        "```",
        instagram_caption(c),
        "```",
        "",
        "---",
        "",
        "## X / Twitter Thread",
        "",
    ]

    for i, post in enumerate(thread, 1):
        lines += [f"### Post {i}", "", "```", post, "```", ""]

    output_path = output_dir / "social_posts.md"
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[OK] Social posts generated: {output_path}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
generate_dwg_site.py
DWG — Generates the main organizational website from the Jinja2 template.
Output: .tmp/dwg_site/index.html

This is the primary organizational homepage for DeepWebGallery:
programs, active epics, the Shadow Library, and an explainer video
section (placeholder until the video is produced).

Edit CONFIG before running. Set video_url once the explainer video
is ready — see workflows/05_main_site.md.
"""

from pathlib import Path
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

# ── CONFIG ──────────────────────────────────────────────────────────────────
# Edit these values before running or regenerating the site.
# See workflows/05_main_site.md for field descriptions.

CONFIG = {
    # ── Site identity ────────────────────────────────────────────────────────
    "site_title": "DeepWebGallery",
    "tagline_1":  "Thinking art and the internet beyond artists and artworks.",
    "tagline_2":  "Beyond subjects and objects; in a non-transcendental fashion.",

    # ── Video explainer ──────────────────────────────────────────────────────
    # Leave video_url empty ("") to show the placeholder box.
    # Once produced, set to a YouTube/Vimeo embed URL, e.g.:
    #   "https://www.youtube.com/embed/XXXXXXXXXXXX"
    #   "https://player.vimeo.com/video/XXXXXXXXX"
    "video_url":     "",
    "video_caption": "",   # Caption below video. Leave empty to use default.

    # ── Programs ─────────────────────────────────────────────────────────────
    "programs": [
        {
            "code":        "#W3SP",
            "name":        "Web3Suicide Program",
            "description": (
                "Blockchain, peer-to-peer networks, and their political and "
                "cultural implications. Created in 2020 as a critical response "
                "to the NFT wave — challenging the idea that market price is the "
                "ultimate measure of value."
            ),
            "operator":    None,
            "status":      "active",
        },
        {
            "code":        "#UHP",
            "name":        "Uncreating Humans Program",
            "description": (
                "Cognitive architectures, social reality, bots, software tools, "
                "hardware installations. Uses cognitive architecture as an "
                "analytical tool to understand operative systems underlying "
                "social phenomena."
            ),
            "operator":    "Anon",
            "status":      "active",
        },
        {
            "code":        "#DCP",
            "name":        "Digital Clinique Program",
            "description": (
                "Emotional and spiritual issues of non-human subjectivities. "
                "Bots. Machinic desire. Running since 2017. Operates at the "
                "intersection of psychoanalysis, neuroscience, and machine behavior."
            ),
            "operator":    "@tdc1831",
            "status":      "active",
        },
    ],

    # ── Epics ────────────────────────────────────────────────────────────────
    # status: "active" | "archived"
    "epics": [
        {
            "code":        "CICFA",
            "name":        "Cultural Infrastructure Critical Failure Attack",
            "status":      "active",
            "current_op":  "MOMA.SYM",
            "url":         "https://deep-web-gallery.github.io/CICFA/",
            "description": (
                "Bug Bounty Program for Cultural Infrastructure. Inspired by "
                "cybersecurity methodology, the program redirects that logic "
                "toward museums, biennials, foundations, and cultural bureaucracies. "
                "The target is not the server. The target is the institutional logic itself."
            ),
        },
        {
            "code":        "DeFi Guillotine",
            "name":        "DeFi Guillotine",
            "status":      "archived",
            "current_op":  None,
            "url":         None,
            "description": (
                "Open-source financial software art project operating as a Flash Grant. "
                "Core software allowed users to 'suicide' their NFTs — permanently "
                "redirecting them to the Ethereum dead address. Quadratic voting "
                "($DWGT tokens) decided which NFT would be publicly executed."
            ),
        },
    ],

    # ── Shadow Library ───────────────────────────────────────────────────────
    "shadow_library_url": "https://deepwebgallery.substack.com/",

    # ── Footer ───────────────────────────────────────────────────────────────
    "governance":  "Decentralized Monarchism / Ironic-Corp",
    "since_year":  "2017",
    "contact":     "@deepwebgallery",
}

# ── RENDER ───────────────────────────────────────────────────────────────────

def main():
    base_dir     = Path(__file__).parent
    template_dir = base_dir / "templates"
    output_dir   = base_dir.parent / ".tmp" / "dwg_site"
    output_dir.mkdir(parents=True, exist_ok=True)

    env      = Environment(loader=FileSystemLoader(str(template_dir)))
    template = env.get_template("dwg_main_site.html")

    ctx = dict(CONFIG)
    ctx["generated_at"] = datetime.now().isoformat()

    rendered = template.render(**ctx)

    output_path = output_dir / "index.html"
    output_path.write_text(rendered, encoding="utf-8")

    print(f"[OK] DWG site generated: {output_path}")
    print()

    # Checklist hints
    if not CONFIG["video_url"]:
        print("[i] video_url is not set — video placeholder will be shown.")
        print("    Set video_url once the explainer video is produced.")

    print()
    print(f"[?] Preview: open .tmp/dwg_site/index.html in your browser")
    print(f"[?] Deploy:  update deploy_to_gh_pages.py with source_dir='.tmp/dwg_site'")
    print(f"             and target repo set to the DWG main site repo.")


if __name__ == "__main__":
    main()

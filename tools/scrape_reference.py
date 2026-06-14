"""
scrape_reference.py — Fetch a reference website and save as clean markdown.

Uses Firecrawl when FIRECRAWL_API_KEY is set and credits are available.
Falls back to Jina AI Reader (free, no key required) automatically.

Usage:
    python tools/scrape_reference.py --url URL --output PATH [--depth N] [--extract PROMPT]

Examples:
    python tools/scrape_reference.py \
        --url https://www.sacred.computer/ \
        --output skills/cicfa-aesthetic/references/sacred_computer.md

    python tools/scrape_reference.py \
        --url https://www.sacred.computer/ \
        --output .tmp/sacred_computer.md \
        --extract "Extract the color palette, typography rules, and spacing system"
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

import requests
from dotenv import load_dotenv

# Always load .env from the project root (parent of tools/)
load_dotenv(Path(__file__).parent.parent / ".env")


def scrape_via_firecrawl(app, url: str, depth: int, extract_prompt: str):
    """Returns markdown string or raises on failure."""
    if extract_prompt:
        result = app.scrape(
            url,
            formats=["extract"],
            extract={"prompt": extract_prompt},
        )
        content = getattr(result, "extract", "") or ""
        if isinstance(content, dict):
            import json
            content = json.dumps(content, indent=2)
        return content
    elif depth > 1:
        result = app.crawl(
            url,
            limit=depth * 10,
            scrape_options={"formats": ["markdown"]},
        )
        pages = getattr(result, "data", []) or []
        parts = []
        for page in pages:
            meta = getattr(page, "metadata", {}) or {}
            page_url = meta.get("sourceURL", "")
            page_md = getattr(page, "markdown", "") or ""
            if page_md:
                parts.append(f"## Source: {page_url}\n\n{page_md}")
        return "\n\n---\n\n".join(parts)
    else:
        result = app.scrape(url, formats=["markdown"])
        return getattr(result, "markdown", "") or ""


def scrape_via_jina(url: str) -> str:
    """Jina AI Reader — free, no key needed. Returns markdown string."""
    jina_url = f"https://r.jina.ai/{url}"
    headers = {"Accept": "text/markdown", "X-Return-Format": "markdown"}
    resp = requests.get(jina_url, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.text


def scrape(url: str, output: str, depth: int = 1, extract_prompt: str = None) -> None:
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    content = ""
    backend = None

    api_key = os.getenv("FIRECRAWL_API_KEY")
    if api_key:
        try:
            from firecrawl import FirecrawlApp
            app = FirecrawlApp(api_key=api_key)
            print(f"Scraping via Firecrawl: {url}")
            content = scrape_via_firecrawl(app, url, depth, extract_prompt)
            backend = "firecrawl"
        except Exception as e:
            print(f"Firecrawl failed ({e}), falling back to Jina...", file=sys.stderr)

    if not content:
        if extract_prompt:
            print("Note: --extract requires Firecrawl. Running plain scrape via Jina.", file=sys.stderr)
        print(f"Scraping via Jina AI Reader: {url}")
        content = scrape_via_jina(url)
        backend = "jina"

    if not content:
        print("Error: no content returned from any backend", file=sys.stderr)
        sys.exit(1)

    header = f"<!-- scraped: {url} | {datetime.utcnow().strftime('%Y-%m-%d')} | backend: {backend} -->\n\n"
    output_path.write_text(header + content, encoding="utf-8")
    print(f"Saved to: {output_path} ({len(content):,} chars)")


def main():
    parser = argparse.ArgumentParser(description="Scrape a reference site to markdown.")
    parser.add_argument("--url", required=True, help="URL to scrape")
    parser.add_argument("--output", required=True, help="Output file path (.md)")
    parser.add_argument(
        "--depth",
        type=int,
        default=1,
        help="Crawl depth: 1 = single page, 2+ = follow links — Firecrawl only (default: 1)",
    )
    parser.add_argument(
        "--extract",
        default=None,
        help="Natural language prompt for structured extraction — Firecrawl only",
    )
    args = parser.parse_args()
    scrape(args.url, args.output, args.depth, args.extract)


if __name__ == "__main__":
    main()

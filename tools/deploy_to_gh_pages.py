#!/usr/bin/env python3
"""
deploy_to_gh_pages.py
CICFA — Deploys the generated bounty site to the CICF GitHub Pages repo.

Prerequisites:
  1. Run `python tools/generate_bounty_site.py` first
  2. Set target_repo below to the local path of your CICF repo
  3. Ensure the CICF repo has a gh-pages branch (or main with /docs)
  4. Set dry_run to False when ready to push

GitHub Pages setup (one-time):
  In the CICF repo on GitHub → Settings → Pages:
  - Source: Deploy from branch
  - Branch: gh-pages / (root)
  The live URL will be: https://boris-maker.github.io/CICF/
"""

import shutil
import subprocess
import sys
from pathlib import Path
from datetime import datetime

# ── CONFIG ───────────────────────────────────────────────────────────────────

CONFIG = {
    # Absolute path to your local CICF repo (the one that deploys to GitHub Pages).
    "target_repo":    "/Users/boris/Documents/DWG/CICFA_PUBLIC",

    # Branch that GitHub Pages serves from.
    "target_branch":  "main",

    # Subdirectory inside target_repo to write files into.
    # Use "" (empty string) for the repo root.
    "target_subdir":  "",

    # Source directory (relative to this repo's root).
    "source_dir":     ".tmp/bounty_site",

    # Git commit message.
    "commit_message": f"deploy: CICFA bounty site — Operation 001 [{datetime.now().strftime('%Y-%m-%d %H:%M')}]",

    # Dry run: print what would happen without executing git commands.
    "dry_run":        True,

    # Live URL (for confirmation message).
    "live_url":       "https://deep-web-gallery.github.io/CICFA/",
}

# ── HELPERS ──────────────────────────────────────────────────────────────────

def run(cmd, cwd=None, check=True):
    """Run a shell command. Prints it first. Raises on failure unless check=False."""
    print(f"  $ {' '.join(str(c) for c in cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.stdout.strip():
        print(f"    {result.stdout.strip()}")
    if result.returncode != 0:
        if check:
            print(f"[ERROR] Command failed (exit {result.returncode}):")
            print(f"    {result.stderr.strip()}")
            sys.exit(1)
    return result


def dry(cmd):
    print(f"  [DRY] $ {' '.join(str(c) for c in cmd)}")


# ── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    repo_root   = Path(__file__).parent.parent
    source_dir  = repo_root / CONFIG["source_dir"]
    target_repo = Path(CONFIG["target_repo"]).expanduser() if CONFIG["target_repo"] else None
    branch      = CONFIG["target_branch"]
    subdir      = CONFIG["target_subdir"]
    dry_run     = CONFIG["dry_run"]

    print("=" * 60)
    print("CICFA — Deploy to GitHub Pages")
    print("=" * 60)

    # ── Validate source ──────────────────────────────────────────
    if not source_dir.exists():
        print(f"[ERROR] Source directory not found: {source_dir}")
        print("        Run `python tools/generate_bounty_site.py` first.")
        sys.exit(1)

    index_file = source_dir / "index.html"
    if not index_file.exists():
        print(f"[ERROR] index.html not found in {source_dir}")
        print("        Run `python tools/generate_bounty_site.py` first.")
        sys.exit(1)

    # ── SAFETY INTERLOCK — DEE-30, added 2026-07-24 ──────────────
    # The bounty pool's key is held by a third party; the wallet was swept
    # 2026-07-10. The live page stopped soliciting contributions, but the
    # artifact this script publishes is a March render that still asks for
    # them — so deploying it would put the invitation back in front of the
    # public. Refuse on the *content* rather than a flag: a genuinely fixed
    # artifact still deploys, only a soliciting one is blocked.
    SOLICITATION = [
        "invited to arm",
        "increases the prize",
        "To fund the bounty",
        'onclick="copyAddress()"',
        "new QRCode",
        "ethereum:' +",
    ]
    html = index_file.read_text(encoding="utf-8", errors="replace")
    found = [p for p in SOLICITATION if p in html]
    if found:
        print("[ABORT] This artifact solicits contributions to a compromised wallet.")
        print("        The bounty pool's private key is in someone else's hands and")
        print("        the wallet was swept on 2026-07-10 (DEE-30). Publishing this")
        print("        would ask the public to send ETH to a thief.")
        print()
        print(f"        Offending markers in {index_file}:")
        for p in found:
            print(f"          - {p}")
        print()
        print("        Fix the template, or edit CICFA_PUBLIC/index.html directly —")
        print("        it is the source of truth for the live page. CLAUDE.md §5.")
        sys.exit(2)

    print(f"[OK] Source: {source_dir}")

    # ── Validate target repo ─────────────────────────────────────
    if not CONFIG["target_repo"]:
        print("[ERROR] target_repo is not set in CONFIG.")
        print("        Set it to the absolute path of your local CICF repo.")
        sys.exit(1)

    if not target_repo.exists():
        print(f"[ERROR] target_repo path does not exist: {target_repo}")
        sys.exit(1)

    if not (target_repo / ".git").exists():
        print(f"[ERROR] target_repo is not a git repository: {target_repo}")
        sys.exit(1)

    print(f"[OK] Target repo: {target_repo}")

    # ── Check out / create target branch ────────────────────────
    print(f"\n[1] Checking out branch: {branch}")
    # Check if branch exists locally
    result = run(["git", "branch", "--list", branch], cwd=target_repo, check=False)
    branch_exists = branch in result.stdout

    if dry_run:
        if not branch_exists:
            dry(["git", "checkout", "--orphan", branch])
            dry(["git", "rm", "-rf", "."])
        else:
            dry(["git", "checkout", branch])
    else:
        if not branch_exists:
            # Check if it exists on remote
            result = run(["git", "fetch", "origin", branch], cwd=target_repo, check=False)
            if result.returncode == 0:
                run(["git", "checkout", branch], cwd=target_repo)
            else:
                print(f"  Creating orphan branch: {branch}")
                run(["git", "checkout", "--orphan", branch], cwd=target_repo)
                run(["git", "rm", "-rf", "."], cwd=target_repo, check=False)
        else:
            run(["git", "checkout", branch], cwd=target_repo)

    # ── Copy files ───────────────────────────────────────────────
    print(f"\n[2] Copying files to target repo")
    dest = target_repo / subdir if subdir else target_repo

    if dry_run:
        for f in source_dir.rglob("*"):
            if f.is_file():
                rel = f.relative_to(source_dir)
                dry(["cp", str(f), str(dest / rel)])
    else:
        if subdir:
            dest.mkdir(parents=True, exist_ok=True)
        for f in source_dir.rglob("*"):
            if f.is_file():
                rel = f.relative_to(source_dir)
                target_file = dest / rel
                target_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, target_file)
                print(f"  Copied: {rel}")

    # ── Stage ────────────────────────────────────────────────────
    print(f"\n[3] Staging changes")
    if dry_run:
        dry(["git", "add", "."])
    else:
        run(["git", "add", "."], cwd=target_repo)

    # ── Commit ───────────────────────────────────────────────────
    print(f"\n[4] Committing")
    msg = CONFIG["commit_message"]
    if dry_run:
        dry(["git", "commit", "-m", msg])
    else:
        result = run(["git", "commit", "-m", msg], cwd=target_repo, check=False)
        if result.returncode != 0 and "nothing to commit" in result.stdout + result.stderr:
            print("  Nothing to commit — files are up to date.")
        elif result.returncode != 0:
            print(f"[ERROR] Commit failed: {result.stderr.strip()}")
            sys.exit(1)

    # ── Push ─────────────────────────────────────────────────────
    print(f"\n[5] Pushing to origin/{branch}")
    if dry_run:
        dry(["git", "push", "origin", branch])
    else:
        run(["git", "push", "origin", branch], cwd=target_repo)

    # ── Done ─────────────────────────────────────────────────────
    print()
    print("=" * 60)
    if dry_run:
        print("[DRY RUN COMPLETE] No changes were made.")
        print("Set dry_run = False in CONFIG to execute for real.")
    else:
        print("[DEPLOYED]")
        print(f"Live at: {CONFIG['live_url']}")
        print("Note: GitHub Pages may take 1-2 minutes to update.")
    print("=" * 60)


if __name__ == "__main__":
    main()

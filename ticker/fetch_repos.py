#!/usr/bin/env python3
"""Fetch and refresh featured Codex CLI repository statistics from GitHub API.

Uses the Python standard library only (no external dependencies required).
"""

from __future__ import annotations

import csv
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
TICKER_CSV = DATA_DIR / "repo-ticker.csv"
PREVIOUS_CSV = DATA_DIR / "repo-ticker-previous.csv"

# Core query searching for Codex CLI repositories and tooling
DEFAULT_QUERY = '"codex cli" OR "openai codex" in:name,description,readme archived:false'

# Blocklist for unrelated or spam repositories
BLOCKED_REPOS: set[str] = {
    "source-code",
    "codex-malware",
}


def load_metrics_map(path: Path) -> dict[str, dict[str, int]]:
    """Load repo metrics from an existing CSV snapshot."""
    if not path.is_file():
        return {}

    mapping: dict[str, dict[str, int]] = {}
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("full_name")
            if not name:
                continue
            mapping[name] = {
                "stars": int(row.get("stars", 0)),
                "forks": int(row.get("forks", 0)),
            }
    return mapping


def query_github_search(
    token: str | None = None,
    query: str = DEFAULT_QUERY,
    limit: int = 60,
) -> list[dict[str, Any]]:
    """Query GitHub Search API for relevant repositories."""
    url = (
        f"https://api.github.com/search/repositories?"
        + urllib.parse.urlencode({"q": query, "sort": "stars", "order": "desc", "per_page": limit})
    )

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Awesome-Codex-CLI-Ticker",
            "Accept": "application/vnd.github.v3+json",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )

    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    results: list[dict[str, Any]] = []
    for item in data.get("items", []):
        full_name = item.get("full_name", "")
        if item.get("fork") or any(b in full_name.lower() for b in BLOCKED_REPOS):
            continue

        results.append(
            {
                "full_name": full_name,
                "stars": int(item.get("stargazers_count", 0)),
                "forks": int(item.get("forks_count", 0)),
                "description": (item.get("description") or "").strip(),
                "url": item.get("html_url", f"https://github.com/{full_name}"),
            }
        )
    return results


def calculate_deltas(
    current: list[dict[str, Any]],
    baseline: dict[str, dict[str, int]],
) -> list[dict[str, Any]]:
    """Compute star and fork changes against previous snapshot."""
    updated: list[dict[str, Any]] = []
    for repo in current:
        name = repo["full_name"]
        prev = baseline.get(name)
        if prev:
            repo["stars_delta"] = repo["stars"] - prev["stars"]
            repo["forks_delta"] = repo["forks"] - prev["forks"]
        else:
            repo["stars_delta"] = 0
            repo["forks_delta"] = 0
        updated.append(repo)
    return updated


def write_csv(data: list[dict[str, Any]], target: Path) -> None:
    """Save repository metrics to CSV."""
    target.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "full_name",
        "stars",
        "forks",
        "stars_delta",
        "forks_delta",
        "url",
        "description",
    ]
    with target.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data)


def main() -> None:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Note: GITHUB_TOKEN not provided, using unauthenticated public API limit.", file=sys.stderr)

    previous = load_metrics_map(PREVIOUS_CSV if PREVIOUS_CSV.exists() else TICKER_CSV)

    try:
        repos = query_github_search(token=token)
        print(f"Fetched {len(repos)} repositories from GitHub.")
    except urllib.error.URLError as err:
        print(f"Network error querying GitHub API: {err}", file=sys.stderr)
        sys.exit(1)

    enriched = calculate_deltas(repos, previous)
    write_csv(enriched, TICKER_CSV)
    print(f"Saved ticker metrics to {TICKER_CSV}")


if __name__ == "__main__":
    main()

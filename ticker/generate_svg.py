#!/usr/bin/env python3
"""Generate a smooth scrolling SVG banner for featured Codex CLI repositories.

Clean-room implementation with zero external dependencies.
"""

from __future__ import annotations

import csv
import html
import random
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
TICKER_CSV = REPO_ROOT / "data" / "repo-ticker.csv"
OUTPUT_SVG = REPO_ROOT / "assets" / "repo-ticker.svg"
OUTPUT_LIGHT_SVG = REPO_ROOT / "assets" / "repo-ticker-light.svg"

CARD_WIDTH = 260
CARD_GAP = 16
SLOT_WIDTH = CARD_WIDTH + CARD_GAP


def format_count(val: int) -> str:
    """Format star count cleanly (e.g., 14.2k, 850)."""
    if val >= 1_000_000:
        return f"{val / 1_000_000:.1f}M"
    if val >= 1_000:
        return f"{val / 1_000:.1f}k"
    return str(val)


def truncate_text(text: str, max_chars: int = 24) -> str:
    """Truncate text with ellipsis if length exceeds threshold."""
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 1] + "…"


def load_repositories(csv_path: Path) -> list[dict[str, Any]]:
    """Read repositories from CSV file."""
    if not csv_path.is_file():
        return []

    repos: list[dict[str, Any]] = []
    with csv_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            full_name = row.get("full_name", "").strip()
            if not full_name or "/" not in full_name:
                continue
            stars = int(row.get("stars", 0))
            url = row.get("url") or f"https://github.com/{full_name}"
            repos.append({"full_name": full_name, "stars": stars, "url": url})
    return repos


def render_card(repo: dict[str, Any], x_offset: int) -> str:
    """Render a single repository card in SVG."""
    owner, name = repo["full_name"].split("/", 1)
    short_name = truncate_text(name, max_chars=18)
    short_owner = truncate_text(owner, max_chars=16)
    star_str = format_count(repo["stars"])
    url = html.escape(repo["url"])

    return f"""    <a href="{url}" target="_blank">
      <g transform="translate({x_offset}, 14)" class="card">
        <rect width="{CARD_WIDTH}" height="56" rx="8" fill="#161b22" stroke="#30363d" stroke-width="1"/>
        <text x="14" y="24" fill="#58a6ff" font-size="16" font-weight="600">{html.escape(short_name)}</text>
        <text x="14" y="44" fill="#8b949e" font-size="14">{html.escape(short_owner)}</text>
        <g transform="translate({CARD_WIDTH - 64}, 18)">
          <rect width="52" height="20" rx="4" fill="#21262d"/>
          <text x="8" y="14" fill="#e6edf3" font-size="11" font-weight="500">★ {star_str}</text>
        </g>
      </g>
    </a>"""


def build_svg(repos: list[dict[str, Any]], sample_size: int = 10) -> str:
    """Generate the complete animated ticker SVG string."""
    if not repos:
        selected = [
            {"full_name": "openai/codex", "stars": 12500, "url": "https://github.com/openai/codex"},
            {"full_name": "openai/skills", "stars": 3200, "url": "https://github.com/openai/skills"},
        ]
    else:
        sample_count = min(sample_size, len(repos))
        selected = random.sample(repos, sample_count)

    loop_count = len(selected)
    total_strip_width = loop_count * SLOT_WIDTH
    duration = max(24, total_strip_width // 60)

    # Render base cards + duplicate cards for seamless infinite scroll
    cards_svg: list[str] = []
    for idx, repo in enumerate(selected):
        cards_svg.append(render_card(repo, idx * SLOT_WIDTH))

    # Add trailing clone cards to prevent blanks before loop restarts
    clone_count = min(4, loop_count)
    for idx in range(clone_count):
        cards_svg.append(render_card(selected[idx], (loop_count + idx) * SLOT_WIDTH))

    rendered_cards = "\n".join(cards_svg)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="360" height="84" viewBox="0 0 360 84" role="img" aria-label="Codex CLI Projects">
  <style>
    text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
    .card:hover rect:first-child {{ stroke: #58a6ff; fill: #1c2128; }}
  </style>
  <defs>
    <linearGradient id="fadeEdgeLeft" x1="0" x2="1" y1="0" y2="0">
      <stop offset="0%" stop-color="#0d1117" stop-opacity="1"/>
      <stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="fadeEdgeRight" x1="0" x2="1" y1="0" y2="0">
      <stop offset="0%" stop-color="#0d1117" stop-opacity="0"/>
      <stop offset="100%" stop-color="#0d1117" stop-opacity="1"/>
    </linearGradient>
    <clipPath id="viewportClip">
      <rect x="0" y="0" width="360" height="84"/>
    </clipPath>
  </defs>

  <!-- Background container -->
  <rect width="360" height="84" rx="10" fill="#0d1117" stroke="#30363d" stroke-width="1"/>

  <!-- Ticker Track -->
  <g clip-path="url(#viewportClip)">
    <g>
      <animateTransform
        attributeName="transform"
        type="translate"
        from="12 0"
        to="{12 - total_strip_width} 0"
        dur="{duration}s"
        repeatCount="indefinite"
      />
{rendered_cards}
    </g>
  </g>

  <!-- Side Fading Overlays -->
  <rect x="0" y="1" width="12" height="82" fill="url(#fadeEdgeLeft)" pointer-events="none"/>
  <rect x="340" y="1" width="20" height="82" fill="url(#fadeEdgeRight)" pointer-events="none"/>
</svg>
"""


def main() -> None:
    repos = load_repositories(TICKER_CSV)
    svg_content = build_svg(repos)
    # Reuse the same selection and animation for both theme variants.
    light_palette = {
        "#0d1117": "#ffffff",
        "#161b22": "#f6f8fa",
        "#30363d": "#d1d9e0",
        "#58a6ff": "#0969da",
        "#8b949e": "#59636e",
        "#21262d": "#e6ebf1",
        "#e6edf3": "#1f2328",
        "#1c2128": "#eef2f6",
    }
    light_svg = svg_content
    for dark, light in light_palette.items():
        light_svg = light_svg.replace(dark, light)
    OUTPUT_SVG.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_SVG.write_text(svg_content, encoding="utf-8")
    OUTPUT_LIGHT_SVG.write_text(light_svg, encoding="utf-8")
    print(f"Generated dark and light tickers ({len(repos)} repositories loaded)")


if __name__ == "__main__":
    main()

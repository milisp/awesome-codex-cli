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

CARD_WIDTH = 280
CARD_GAP = 24
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


def render_card(repo: dict[str, Any], x_offset: int, flip: bool = False) -> str:
    """Render an editorial-style project, alternating above/below the midline."""
    owner, name = repo["full_name"].split("/", 1)
    short_name = truncate_text(name, max_chars=20)
    short_owner = truncate_text(owner, max_chars=18)
    star_str = format_count(repo["stars"])
    url = html.escape(repo["url"])
    y_offset = 78 if flip else 12

    return f"""    <a href="{url}" target="_blank">
      <g transform="translate({x_offset}, {y_offset})" class="project">
        <title>{html.escape(repo['full_name'])} — {repo['stars']} stars</title>
        <text x="0" y="26" fill="#e6edf3" font-size="25" font-weight="600" letter-spacing="-0.5">{html.escape(short_name)}</text>
        <text x="0" y="47" fill="#8b949e" font-size="14">{html.escape(short_owner)} · ★ {star_str}</text>
      </g>
    </a>"""


def build_svg(repos: list[dict[str, Any]], sample_size: int = 10) -> str:
    """Generate daily picks with a fresh sample on each refresh."""
    if sample_size < 1:
        raise ValueError("sample_size must be positive")
    if not repos:
        selected = [
            {"full_name": "openai/codex", "stars": 0, "url": "https://github.com/openai/codex"},
            {"full_name": "openai/skills", "stars": 0, "url": "https://github.com/openai/skills"},
        ]
    else:
        sample_count = min(sample_size, len(repos))
        selected = random.sample(repos, sample_count)

    loop_count = len(selected)
    column_count = (loop_count + 1) // 2
    total_strip_width = column_count * SLOT_WIDTH
    duration = max(24, total_strip_width // 30)

    # Render base cards + duplicate cards for seamless infinite scroll
    cards_svg: list[str] = []
    for column in range(column_count):
        cards_svg.append(render_card(selected[column * 2], column * SLOT_WIDTH))
        cards_svg.append(render_card(
            selected[(column * 2 + 1) % loop_count], column * SLOT_WIDTH + 28, True
        ))

    # Add trailing clone cards to prevent blanks before loop restarts
    for column in range(2):
        original_column = column % column_count
        x = (column_count + column) * SLOT_WIDTH
        cards_svg.append(render_card(selected[original_column * 2], x))
        cards_svg.append(render_card(
            selected[(original_column * 2 + 1) % loop_count], x + 28, True
        ))

    rendered_cards = "\n".join(cards_svg)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="640" height="142" viewBox="0 0 640 142" role="img" aria-label="Daily Codex Picks">
  <title>Daily Codex Picks</title>
  <style>
    text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
    .project:hover text:first-of-type {{ fill: #58a6ff; }}
    .static-card {{ display: none; }}
    @media (prefers-reduced-motion: reduce) {{
      .ticker-track {{ display: none; }}
      .static-card {{ display: inline; }}
    }}
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
      <rect x="100" y="0" width="540" height="142"/>
    </clipPath>
  </defs>

  <!-- Background container -->
  <rect width="640" height="142" rx="8" fill="#0d1117"/>
  <path d="M8 1 H632 M8 141 H632" stroke="#30363d"/>
  <rect x="0" y="1" width="92" height="140" rx="8" fill="#161b22"/>
  <text x="46" y="53" fill="#e6edf3" font-size="13" font-weight="700" text-anchor="middle" letter-spacing="1">CODEX</text>
  <text x="46" y="75" fill="#8b949e" font-size="12" text-anchor="middle">Daily picks</text>
  <circle cx="46" cy="99" r="3" fill="#58a6ff"/>
  <path d="M93 16 V126" stroke="#30363d"/>

  <!-- Ticker Track -->
  <path d="M106 71 H626" stroke="#30363d" stroke-dasharray="5 7" opacity="0.5"/>
  <g clip-path="url(#viewportClip)">
    <g class="static-card" transform="translate(114, 0)">
{render_card(selected[0], 0)}
{render_card(selected[min(1, loop_count - 1)], 0, True)}
    </g>
    <g class="ticker-track">
      <animateTransform
        attributeName="transform"
        type="translate"
        from="114 0"
        to="{114 - total_strip_width} 0"
        dur="{duration}s"
        repeatCount="indefinite"
      />
{rendered_cards}
    </g>
  </g>

  <!-- Side Fading Overlays -->
  <rect x="100" y="1" width="14" height="140" fill="url(#fadeEdgeLeft)" pointer-events="none"/>
  <rect x="608" y="1" width="32" height="140" fill="url(#fadeEdgeRight)" pointer-events="none"/>
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

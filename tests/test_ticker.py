#!/usr/bin/env python3
"""Tests for Codex CLI Ticker suite (clean-room implementation)."""

import csv
import sys
import tempfile
import unittest
from pathlib import Path

# Add repo root to import path
sys.path.insert(0, str(Path(__file__).parent.parent))

from ticker.fetch_repos import calculate_deltas, load_metrics_map, write_csv
from ticker.generate_svg import (
    build_svg,
    format_count,
    load_repositories,
    render_card,
    truncate_text,
)


class TestTickerFormatting(unittest.TestCase):
    def test_format_count(self) -> None:
        self.assertEqual(format_count(500), "500")
        self.assertEqual(format_count(1500), "1.5k")
        self.assertEqual(format_count(12500), "12.5k")
        self.assertEqual(format_count(2500000), "2.5M")

    def test_truncate_text(self) -> None:
        self.assertEqual(truncate_text("short", 10), "short")
        self.assertEqual(truncate_text("exactly10!", 10), "exactly10!")
        truncated = truncate_text("a_very_long_string_here", 10)
        self.assertTrue(truncated.endswith("…"))
        self.assertEqual(len(truncated), 10)


class TestTickerSvgGeneration(unittest.TestCase):
    def test_render_card(self) -> None:
        repo = {
            "full_name": "openai/codex",
            "stars": 12500,
            "url": "https://github.com/openai/codex",
        }
        card = render_card(repo, 0)
        self.assertIn("openai", card)
        self.assertIn("codex", card)
        self.assertIn("12.5k", card)
        self.assertIn("https://github.com/openai/codex", card)

    def test_build_svg_structure(self) -> None:
        repos = [
            {"full_name": "openai/codex", "stars": 12500, "url": "https://github.com/openai/codex"},
            {"full_name": "openai/skills", "stars": 3200, "url": "https://github.com/openai/skills"},
        ]
        svg = build_svg(repos)
        self.assertIn("<svg", svg)
        self.assertIn("CODEX CLI", svg)
        self.assertIn("FEATURED", svg)
        self.assertIn("<animateTransform", svg)
        self.assertIn("openai", svg)


class TestTickerMetrics(unittest.TestCase):
    def test_calculate_deltas(self) -> None:
        current = [{"full_name": "owner/repo", "stars": 120, "forks": 15}]
        baseline = {"owner/repo": {"stars": 100, "forks": 10}}
        result = calculate_deltas(current, baseline)
        self.assertEqual(result[0]["stars_delta"], 20)
        self.assertEqual(result[0]["forks_delta"], 5)

    def test_calculate_deltas_new_repo(self) -> None:
        current = [{"full_name": "owner/new", "stars": 50, "forks": 5}]
        result = calculate_deltas(current, {})
        self.assertEqual(result[0]["stars_delta"], 0)
        self.assertEqual(result[0]["forks_delta"], 0)

    def test_csv_roundtrip(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_path = Path(tmpdir) / "test.csv"
            sample_data = [
                {
                    "full_name": "owner/repo",
                    "stars": 42,
                    "forks": 7,
                    "stars_delta": 2,
                    "forks_delta": 1,
                    "url": "https://github.com/owner/repo",
                    "description": "test repo",
                }
            ]
            write_csv(sample_data, csv_path)
            self.assertTrue(csv_path.exists())

            mapping = load_metrics_map(csv_path)
            self.assertEqual(mapping["owner/repo"]["stars"], 42)
            self.assertEqual(mapping["owner/repo"]["forks"], 7)

            loaded_repos = load_repositories(csv_path)
            self.assertEqual(len(loaded_repos), 1)
            self.assertEqual(loaded_repos[0]["full_name"], "owner/repo")
            self.assertEqual(loaded_repos[0]["stars"], 42)


if __name__ == "__main__":
    unittest.main()

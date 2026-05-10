#!/usr/bin/env python3
"""
Sync YouTube embed URLs in dla-docs Markdown from screenshot-14-marketing.json.

Reads youtube_url per locale, converts to https://www.youtube.com/embed/{id}, then:
  - docs/index.md: first iframe = English (en), second = Tiếng Việt (vi)
  - docs/{locale}/index.md: single iframe for that locale

Folder names zh-cn and zh-tw map to JSON keys "zh" and "zh-TW".

Usage (from repo root or this directory):
  python dla-docs/scripts/update-docs-video-embeds.py
  python update-docs-video-embeds.py --dry-run
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
DOCS_DIR = SCRIPT_DIR.parent / "docs"
MARKETING_JSON = SCRIPT_DIR / "screenshot-14-marketing.json"

# docs/zh-cn -> JSON key "zh", docs/zh-tw -> "zh-TW"
FOLDER_TO_MARKETING_KEY: dict[str, str] = {
    "zh-cn": "zh",
    "zh-tw": "zh-TW",
}

IFRAME_SRC_PATTERN = re.compile(
    r'src="https://www\.youtube\.com/embed/[^"]+"',
    re.MULTILINE,
)


def folder_to_key(folder: str) -> str:
    return FOLDER_TO_MARKETING_KEY.get(folder, folder)


def youtube_url_to_embed_url(url: str) -> str | None:
    """Extract video id from watch / shorts / embed URL and return canonical embed URL."""
    if not url or not str(url).strip():
        return None
    s = str(url).strip()
    # Already embed
    m = re.search(r"/embed/([^/?&#]+)", s)
    if m:
        return f"https://www.youtube.com/embed/{m.group(1)}"
    # shorts
    m = re.search(r"/shorts/([^/?&#]+)", s)
    if m:
        return f"https://www.youtube.com/embed/{m.group(1)}"
    # watch?v=
    m = re.search(r"[?&]v=([^&]+)", s)
    if m:
        return f"https://www.youtube.com/embed/{m.group(1)}"
    return None


def load_marketing(path: Path) -> dict[str, dict]:
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Expected object at root in {path}")
    return data


def replace_first_n_iframe_srcs(content: str, embed_urls: list[str]) -> tuple[str, int]:
    """Replace iframe src values in document order (first match = embed_urls[0]).

    Applies replacements from the **last** match backward so that replacing the second
    iframe does not re-match and overwrite the first iframe on the next iteration.
    """
    matches = list(IFRAME_SRC_PATTERN.finditer(content))
    n_pairs = min(len(matches), len(embed_urls))
    if n_pairs == 0:
        return content, 0
    out = content
    # Reverse index order: replace trailing iframes first so earlier match positions stay valid.
    for i in range(n_pairs - 1, -1, -1):
        m = matches[i]
        embed_url = embed_urls[i]
        replacement = f'src="{embed_url}"'
        out = out[: m.start()] + replacement + out[m.end() :]
    return out, n_pairs


def update_root_index(marketing: dict[str, dict], path: Path, dry_run: bool) -> bool:
    """docs/index.md: first iframe en, second vi."""
    if not path.is_file():
        print(f"  [skip] missing {path}", file=sys.stderr)
        return False
    en = marketing.get("en", {}).get("youtube_url")
    vi = marketing.get("vi", {}).get("youtube_url")
    if not en or not vi:
        print("  [error] marketing JSON missing en or vi youtube_url", file=sys.stderr)
        return False
    embed_en = youtube_url_to_embed_url(en)
    embed_vi = youtube_url_to_embed_url(vi)
    if not embed_en or not embed_vi:
        print("  [error] could not parse en/vi youtube_url", file=sys.stderr)
        return False

    text = path.read_text(encoding="utf-8")
    new_text, count = replace_first_n_iframe_srcs(text, [embed_en, embed_vi])
    if count < 2:
        print(
            f"  [warn] {path.name}: expected 2 iframe src lines, replaced {count}",
            file=sys.stderr,
        )
    if new_text == text:
        print(f"  [ok] {path.relative_to(DOCS_DIR.parent)} (no change)")
        return True
    if dry_run:
        print(f"  [dry-run] would update {path} ({count} iframe(s))")
        return True
    path.write_text(new_text, encoding="utf-8", newline="\n")
    print(f"  [write] {path.relative_to(DOCS_DIR.parent)} ({count} iframe(s))")
    return True


def update_locale_index(
    marketing: dict[str, dict],
    locale_folder: str,
    path: Path,
    dry_run: bool,
) -> bool:
    key = folder_to_key(locale_folder)
    block = marketing.get(key)
    if not block:
        print(f"  [skip] no marketing key {key!r} for folder {locale_folder}", file=sys.stderr)
        return False
    url = block.get("youtube_url")
    if not url:
        print(f"  [skip] no youtube_url for {key}", file=sys.stderr)
        return False
    embed = youtube_url_to_embed_url(url)
    if not embed:
        print(f"  [error] could not parse youtube_url for {key}: {url!r}", file=sys.stderr)
        return False

    text = path.read_text(encoding="utf-8")
    new_text, count = replace_first_n_iframe_srcs(text, [embed])
    if count == 0:
        print(f"  [warn] {path}: no iframe src matched", file=sys.stderr)
        return False
    if new_text == text:
        print(f"  [ok] {path.relative_to(DOCS_DIR.parent)} (no change)")
        return True
    if dry_run:
        print(f"  [dry-run] would update {path}")
        return True
    path.write_text(new_text, encoding="utf-8", newline="\n")
    print(f"  [write] {path.relative_to(DOCS_DIR.parent)}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions without writing files",
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=MARKETING_JSON,
        help=f"Path to marketing JSON (default: {MARKETING_JSON})",
    )
    parser.add_argument(
        "--docs",
        type=Path,
        default=DOCS_DIR,
        help=f"Docs root (default: {DOCS_DIR})",
    )
    args = parser.parse_args()

    jpath: Path = args.json
    docs: Path = args.docs

    if not jpath.is_file():
        print(f"Missing JSON: {jpath}", file=sys.stderr)
        return 1

    marketing = load_marketing(jpath)
    print(f"Loaded {len(marketing)} locales from {jpath.name}")
    print(f"Docs dir: {docs}")

    root_index = docs / "index.md"
    print("\nRoot index (en + vi):")
    update_root_index(marketing, root_index, args.dry_run)

    locale_dirs = sorted(
        p for p in docs.iterdir() if p.is_dir() and (p / "index.md").is_file()
    )
    print("\nLocale index files:")
    for d in locale_dirs:
        rel = d.name
        idx = d / "index.md"
        update_locale_index(marketing, rel, idx, args.dry_run)

    print("\nDone.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

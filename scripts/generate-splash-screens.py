"""Compose localized splash screens: app name (top) + artwork + slogan (bottom).

Input artwork: dsa-app/src/assets/splash_v2.png
Copy: screenshot-14-marketing.json — app_name, slogan
Output: dsa-app/src/assets/splash/{locale}/splash.png

Usage:
  python generate-splash-screens.py
  python generate-splash-screens.py --locale vi
  python generate-splash-screens.py --dry-run
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
MARKETING_PATH = SCRIPT_DIR / "screenshot-14-marketing.json"
DEFAULT_INPUT = REPO_ROOT / "dsa-app" / "src" / "assets" / "splash_v2.png"
OUTPUT_ROOT = REPO_ROOT / "dsa-app" / "src" / "assets" / "splash"

# Match promo screenshot typography
TEXT_GREEN = (27, 67, 50)
CANVAS_BG = (255, 255, 255, 255)
TEXT_MARGIN_X = 56
TEXT_LINE_GAP = 10

HEADER_HEIGHT_FRAC = 0.118
FOOTER_HEIGHT_FRAC = 0.155

APP_NAME_FONT_START = 58
APP_NAME_FONT_MIN = 40
SLOGAN_FONT_START = 52
SLOGAN_FONT_MIN = 34


def _load_find_font():
    path = SCRIPT_DIR / "generate-screenshot-14-appstore.py"
    spec = importlib.util.spec_from_file_location("_g14_find_font", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.find_font


find_font = _load_find_font()


def wrap_paragraph(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont,
    max_w: int,
) -> list[str]:
    text = " ".join(text.split())
    if not text:
        return [""]
    if " " not in text:
        lines: list[str] = []
        chunk = ""
        for ch in text:
            trial = chunk + ch
            bb = draw.textbbox((0, 0), trial, font=font)
            if bb[2] - bb[0] <= max_w:
                chunk = trial
            else:
                if chunk:
                    lines.append(chunk)
                chunk = ch
        if chunk:
            lines.append(chunk)
        return lines if lines else [text]

    words = text.split()
    lines: list[str] = []
    cur: list[str] = []
    for word in words:
        trial = " ".join(cur + [word])
        bb = draw.textbbox((0, 0), trial, font=font)
        if bb[2] - bb[0] <= max_w:
            cur.append(word)
        else:
            if cur:
                lines.append(" ".join(cur))
            cur = [word]
    if cur:
        lines.append(" ".join(cur))
    return lines


def fit_text_block(
    draw: ImageDraw.ImageDraw,
    text: str,
    *,
    locale: str,
    max_w: int,
    max_h: int,
    start_size: int,
    min_size: int,
) -> tuple[ImageFont.FreeTypeFont, list[str]]:
    for size in range(start_size, min_size - 1, -2):
        font = find_font(size, bold=True, locale=locale)
        lines = wrap_paragraph(draw, text, font, max_w)
        total_h = 0
        for line in lines:
            bb = draw.textbbox((0, 0), line, font=font)
            total_h += bb[3] - bb[1] + TEXT_LINE_GAP
        total_h -= TEXT_LINE_GAP
        if total_h <= max_h:
            return font, lines

    font = find_font(min_size, bold=True, locale=locale)
    return font, wrap_paragraph(draw, text, font, max_w)


def draw_centered_block(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    font: ImageFont.FreeTypeFont,
    *,
    canvas_w: int,
    band_top: int,
    band_height: int,
) -> None:
    line_heights: list[int] = []
    line_widths: list[int] = []
    for line in lines:
        bb = draw.textbbox((0, 0), line, font=font)
        line_widths.append(bb[2] - bb[0])
        line_heights.append(bb[3] - bb[1])

    block_h = sum(line_heights) + TEXT_LINE_GAP * max(0, len(lines) - 1)
    y = band_top + max(0, (band_height - block_h) // 2)

    for line, lw, lh in zip(lines, line_widths, line_heights):
        bb = draw.textbbox((0, 0), line, font=font)
        tx = (canvas_w - lw) // 2 - bb[0]
        draw.text((tx, y - bb[1]), line, font=font, fill=TEXT_GREEN)
        y += lh + TEXT_LINE_GAP


def compose_splash(
    artwork: Image.Image,
    *,
    app_name: str,
    slogan: str,
    locale: str,
    canvas_size: tuple[int, int] | None = None,
) -> Image.Image:
    src_w, src_h = artwork.size
    out_w, out_h = canvas_size or (src_w, src_h)

    header_h = int(out_h * HEADER_HEIGHT_FRAC)
    footer_h = int(out_h * FOOTER_HEIGHT_FRAC)
    art_h = out_h - header_h - footer_h

    canvas = Image.new("RGBA", (out_w, out_h), CANVAS_BG)
    draw = ImageDraw.Draw(canvas)

    scale = min(out_w / src_w, art_h / src_h)
    new_w = max(1, int(src_w * scale))
    new_h = max(1, int(src_h * scale))
    art = artwork.convert("RGBA").resize((new_w, new_h), Image.Resampling.LANCZOS)
    art_x = (out_w - new_w) // 2
    art_y = header_h + (art_h - new_h) // 2
    canvas.alpha_composite(art, (art_x, art_y))

    max_text_w = out_w - 2 * TEXT_MARGIN_X

    app_font, app_lines = fit_text_block(
        draw,
        app_name,
        locale=locale,
        max_w=max_text_w,
        max_h=header_h - 24,
        start_size=APP_NAME_FONT_START,
        min_size=APP_NAME_FONT_MIN,
    )
    draw_centered_block(
        draw,
        app_lines,
        app_font,
        canvas_w=out_w,
        band_top=0,
        band_height=header_h,
    )

    slogan_font, slogan_lines = fit_text_block(
        draw,
        slogan,
        locale=locale,
        max_w=max_text_w,
        max_h=footer_h - 24,
        start_size=SLOGAN_FONT_START,
        min_size=SLOGAN_FONT_MIN,
    )
    draw_centered_block(
        draw,
        slogan_lines,
        slogan_font,
        canvas_w=out_w,
        band_top=out_h - footer_h,
        band_height=footer_h,
    )

    return canvas.convert("RGB")


def load_marketing() -> dict[str, dict[str, str]]:
    with MARKETING_PATH.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Expected object in {MARKETING_PATH}")
    return data


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate localized splash screens.")
    parser.add_argument("--locale", help="Single locale key (default: all locales in JSON)")
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help=f"Artwork PNG (default: {DEFAULT_INPUT})",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=OUTPUT_ROOT,
        help=f"Output root (default: {OUTPUT_ROOT})",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print planned outputs only")
    args = parser.parse_args()

    marketing = load_marketing()
    locales = [args.locale] if args.locale else list(marketing.keys())
    if args.locale and args.locale not in marketing:
        raise SystemExit(f"Unknown locale: {args.locale}")

    if not args.input.is_file():
        raise SystemExit(f"Missing input artwork: {args.input}")

    artwork = Image.open(args.input).convert("RGBA")
    print(f"Input: {args.input} ({artwork.size[0]}x{artwork.size[1]})")

    for locale in locales:
        entry = marketing[locale]
        app_name = entry.get("app_name", "").strip()
        slogan = entry.get("slogan", "").strip()
        if not app_name or not slogan:
            print(f"Skip {locale}: missing app_name or slogan")
            continue

        out_dir = args.output_root / locale
        out_path = out_dir / "splash.png"
        if args.dry_run:
            print(f"Would write {out_path}")
            continue

        out_dir.mkdir(parents=True, exist_ok=True)
        composed = compose_splash(
            artwork,
            app_name=app_name,
            slogan=slogan,
            locale=locale,
        )
        composed.save(out_path, format="PNG", optimize=True)
        print(f"Wrote {out_path}")

    print("Done.")


if __name__ == "__main__":
    main()

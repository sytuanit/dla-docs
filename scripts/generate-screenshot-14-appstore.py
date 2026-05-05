"""App Store first frame: screenshot-*-capture + overlay text → screenshot-14 (all locales).

Reads app display name from dsa-app/src/i18n/locales/{locale}.json.
Marketing copy: screenshot-14-marketing.json (UTF-8). Skips locales without the chosen capture PNG.

Usage:
  python generate-screenshot-14-appstore.py
  python generate-screenshot-14-appstore.py --capture-num 15
  python generate-screenshot-14-appstore.py --locale en --locale ja
  python generate-screenshot-14-appstore.py --ipad
  python generate-screenshot-14-appstore.py --ipad --locale de --capture-num 15
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
SCREENSHOTS_DIR = ROOT / "screenshots"
SCREENSHOTS_IPAD_DIR = ROOT / "screenshots-ipad"
MARKETING_PATH = SCRIPT_DIR / "screenshot-14-marketing.json"


def _resolve_i18n_locales() -> Path:
    here = SCRIPT_DIR.resolve()
    for base in [here, *here.parents]:
        candidate = base / "dsa-app" / "src" / "i18n" / "locales"
        if candidate.is_dir():
            return candidate
    raise FileNotFoundError(
        "Could not find dsa-app/src/i18n/locales — place this script under the repo that contains dsa-app."
    )


I18N_DIR = _resolve_i18n_locales()

REF_W = 1290

MARKETING: dict[str, dict[str, object]] = json.loads(MARKETING_PATH.read_text(encoding="utf-8"))

LOCALE_ORDER = [
    "vi",
    "en",
    "de",
    "es",
    "fr",
    "hi",
    "id",
    "it",
    "ja",
    "ko",
    "lo",
    "pt",
    "th",
    "tr",
    "zh",
    "zh-TW",
]

WIN_FONTS = Path(r"C:\Windows\Fonts")
# Bundled Noto fonts (OFL, fontsource); Windows fallbacks when system fonts missing
_BUNDLED_LAOS_BOLD = SCRIPT_DIR / "fonts" / "noto-sans-lao-700.woff2"
_BUNDLED_LAOS_REG = SCRIPT_DIR / "fonts" / "noto-sans-lao-400.woff2"
_BUNDLED_LAO_VF = SCRIPT_DIR / "fonts" / "noto-sans-lao-vf.ttf"
_BUNDLED_DEVA_BOLD = SCRIPT_DIR / "fonts" / "noto-sans-devanagari-700.woff2"
_BUNDLED_DEVA_REG = SCRIPT_DIR / "fonts" / "noto-sans-devanagari-400.woff2"
# Full VF from google/fonts (OFL); subset woff2 above can miss glyphs on sub lines (hi/lo).
_BUNDLED_DEVA_VF = SCRIPT_DIR / "fonts" / "noto-sans-devanagari-vf.ttf"


def load_app_name(locale: str) -> str:
    path = I18N_DIR / f"{locale}.json"
    if not path.is_file():
        raise FileNotFoundError(f"Missing i18n: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    name = data.get("app_name")
    if not name or not isinstance(name, str):
        raise ValueError(f"No app_name in {path}")
    return name


def _try_truetype(path: Path, size: int) -> ImageFont.FreeTypeFont | None:
    if not path.is_file():
        return None
    try:
        return ImageFont.truetype(str(path), size)
    except OSError:
        pass
    if path.suffix.lower() == ".ttc":
        for idx in range(5):
            try:
                return ImageFont.truetype(str(path), size, index=idx)
            except OSError:
                continue
    return None


def _noto_vf_font(vf_path: Path, size: int, bold: bool) -> ImageFont.FreeTypeFont | None:
    """Load google/fonts Noto * [wdth,wght].ttf and set weight (subset woff2 can miss Lao/Devanagari glyphs)."""
    if not vf_path.is_file():
        return None
    try:
        f = ImageFont.truetype(str(vf_path), size)
    except OSError:
        return None
    try:
        axes = f.get_variation_axes()
    except OSError:
        return f
    if not axes:
        return f
    vals = [float(ax["default"]) for ax in axes]
    vals[0] = 700.0 if bold else 400.0
    try:
        f.set_variation_by_axes(vals)
    except (OSError, TypeError, ValueError):
        pass
    return f


def find_font(size: int, bold: bool = False, *, locale: str = "en") -> ImageFont.FreeTypeFont:
    loc = locale.replace("_", "-").split("-")[0].lower()
    if locale == "zh-TW":
        loc = "zh-TW"
    paths: list[Path] = []

    if loc == "ja":
        paths = [
            WIN_FONTS / "meiryob.ttf",
            WIN_FONTS / "meiryo.ttc",
            WIN_FONTS / "YuGothB.ttc",
            WIN_FONTS / "msgothic.ttc",
        ]
    elif loc == "ko":
        paths = [
            WIN_FONTS / "malgunbd.ttf",
            WIN_FONTS / "malgun.ttf",
        ]
    elif loc == "zh" or locale == "zh":
        paths = [
            WIN_FONTS / "msyhbd.ttc",
            WIN_FONTS / "msyh.ttc",
            WIN_FONTS / "simhei.ttf",
        ]
    elif locale == "zh-TW":
        paths = [
            WIN_FONTS / "msjhbd.ttc",
            WIN_FONTS / "msjh.ttc",
            WIN_FONTS / "msyhbd.ttc",
            WIN_FONTS / "msyh.ttc",
        ]
    elif loc == "hi":
        vf = _noto_vf_font(_BUNDLED_DEVA_VF, size, bold)
        if vf is not None:
            return vf
        if bold:
            paths = [
                _BUNDLED_DEVA_BOLD,
                _BUNDLED_DEVA_REG,
                WIN_FONTS / "NirmalaB.ttf",
                WIN_FONTS / "NirmalaUI.ttf",
                WIN_FONTS / "Nirmala.ttf",
                WIN_FONTS / "MangalB.ttf",
                WIN_FONTS / "Mangal.ttf",
                WIN_FONTS / "Kokila.ttf",
                WIN_FONTS / "KokilaB.ttf",
            ]
        else:
            paths = [
                _BUNDLED_DEVA_REG,
                _BUNDLED_DEVA_BOLD,
                WIN_FONTS / "Nirmala.ttf",
                WIN_FONTS / "NirmalaUI.ttf",
                WIN_FONTS / "NirmalaB.ttf",
                WIN_FONTS / "Mangal.ttf",
                WIN_FONTS / "MangalB.ttf",
                WIN_FONTS / "Kokila.ttf",
                WIN_FONTS / "KokilaB.ttf",
            ]
    elif loc == "th":
        paths = [
            WIN_FONTS / "LeelawUI.ttf",
            WIN_FONTS / "LeelUIsl.ttf",
            WIN_FONTS / "LeelawadeeUI-Bold.ttf",
        ]
    elif loc == "lo":
        vf = _noto_vf_font(_BUNDLED_LAO_VF, size, bold)
        if vf is not None:
            return vf
        if bold:
            paths = [
                _BUNDLED_LAOS_BOLD,
                _BUNDLED_LAOS_REG,
                WIN_FONTS / "seguihis.ttf",
                WIN_FONTS / "SegoeUIHistoric.ttf",
                WIN_FONTS / "Phetsarath-Bold.ttf",
                WIN_FONTS / "Phetsarath-Regular.ttf",
                WIN_FONTS / "LaoUI.ttf",
                WIN_FONTS / "laoui.ttf",
                WIN_FONTS / "Dokchampa.ttf",
                WIN_FONTS / "dokchamp.ttf",
            ]
        else:
            paths = [
                _BUNDLED_LAOS_REG,
                _BUNDLED_LAOS_BOLD,
                WIN_FONTS / "seguihis.ttf",
                WIN_FONTS / "SegoeUIHistoric.ttf",
                WIN_FONTS / "Phetsarath-Regular.ttf",
                WIN_FONTS / "Phetsarath-Bold.ttf",
                WIN_FONTS / "LaoUI.ttf",
                WIN_FONTS / "laoui.ttf",
                WIN_FONTS / "Dokchampa.ttf",
                WIN_FONTS / "dokchamp.ttf",
            ]

    for p in paths:
        f = _try_truetype(p, size)
        if f:
            return f

    candidates = [
        WIN_FONTS / ("segoeuib.ttf" if bold else "segoeui.ttf"),
        WIN_FONTS / "segoeui.ttf",
        WIN_FONTS / ("arialbd.ttf" if bold else "arial.ttf"),
        WIN_FONTS / "arial.ttf",
    ]
    for p in candidates:
        f = _try_truetype(p, size)
        if f:
            return f
    return ImageFont.load_default()


def scale_px(n: int, w: int) -> int:
    return max(10, int(round(n * w / REF_W)))


def draw_stroke_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    *,
    font: ImageFont.ImageFont,
    fill: tuple[int, int, int, int],
    stroke: tuple[int, int, int, int],
    stroke_w: int,
) -> None:
    x, y = xy
    for dx in range(-stroke_w, stroke_w + 1):
        for dy in range(-stroke_w, stroke_w + 1):
            if dx == 0 and dy == 0:
                continue
            draw.text((x + dx, y + dy), text, font=font, fill=stroke)
    draw.text((x, y), text, font=font, fill=fill)


def top_scrim(w: int, h: int, *, height_frac: float = 0.40) -> Image.Image:
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    strip = max(1, int(h * height_frac))
    for y in range(strip):
        t = y / max(strip - 1, 1)
        a = int(78 * (1.0 - t) ** 0.55)
        d.line([(0, y), (w, y)], fill=(248, 252, 255, a))
    return layer


def fit_headline_font(
    draw: ImageDraw.ImageDraw, text: str, max_w: int, w_img: int, *, locale: str
) -> ImageFont.FreeTypeFont:
    start = scale_px(70, w_img)
    minimum = scale_px(42, w_img)
    for sz in range(start, minimum - 1, -2):
        f = find_font(sz, bold=True, locale=locale)
        bbox = draw.textbbox((0, 0), text, font=f)
        if bbox[2] - bbox[0] <= max_w:
            return f
    return find_font(minimum, bold=True, locale=locale)


def _font_pixel_size(font: ImageFont.ImageFont, fallback: int) -> int:
    sz = getattr(font, "size", None)
    if isinstance(sz, int) and sz > 0:
        return sz
    return fallback


def fit_sub_lines_font(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    max_w: int,
    w_img: int,
    *,
    locale: str,
    max_size: int,
) -> ImageFont.FreeTypeFont:
    """Bold font ≤ headline size so every sub line fits max_w (avoids horizontal overflow)."""
    minimum = scale_px(26, w_img)
    cap = max(max_size, minimum)
    for sz in range(cap, minimum - 1, -2):
        f = find_font(sz, bold=True, locale=locale)
        ok = True
        for line in lines:
            bb = draw.textbbox((0, 0), line, font=f)
            if bb[2] - bb[0] > max_w:
                ok = False
                break
        if ok:
            return f
    return find_font(minimum, bold=True, locale=locale)


def render_screenshot_14(
    locale: str,
    *,
    screenshots_root: Path = SCREENSHOTS_DIR,
    capture_num: int = 13,
) -> Path | None:
    copy = MARKETING.get(locale)
    if not copy:
        print(f"Skip {locale}: no MARKETING entry")
        return None

    base_path = screenshots_root / locale / f"screenshot-{capture_num}-capture.png"
    out_path = screenshots_root / locale / "screenshot-14.png"
    if not base_path.is_file():
        print(f"Skip {locale}: missing {base_path}")
        return None

    label = load_app_name(locale)
    headline = str(copy["headline"])
    sub_lines = copy["sub"]
    if not isinstance(sub_lines, list) or len(sub_lines) != 2:
        raise ValueError(f"locale {locale}: need exactly 2 sub lines")

    im = Image.open(base_path).convert("RGBA")
    w, h = im.size

    im.alpha_composite(top_scrim(w, h, height_frac=0.36), (0, 0))

    draw = ImageDraw.Draw(im)
    margin = max(scale_px(28, w), 20)
    block_w = w - 2 * margin

    fill = (255, 255, 255, 255)
    stroke_c = (25, 70, 120, 255)
    sub_line_gap = max(scale_px(32, w), 18)

    font_label = find_font(scale_px(64, w), bold=True, locale=locale)

    y = int(h * 0.048)

    lb = draw.textbbox((0, 0), label, font=font_label)
    lx = (w - (lb[2] - lb[0])) // 2
    draw_stroke_text(draw, (lx, y), label, font=font_label, fill=fill, stroke=stroke_c, stroke_w=3)
    y += lb[3] - lb[1] + scale_px(64, w)

    fh = fit_headline_font(draw, headline, block_w, w, locale=locale)
    hb = draw.textbbox((0, 0), headline, font=fh)
    hx = (w - (hb[2] - hb[0])) // 2
    draw_stroke_text(draw, (hx, y), headline, font=fh, fill=fill, stroke=stroke_c, stroke_w=3)

    sub_strs = [str(x) for x in sub_lines]
    sub_max = _font_pixel_size(fh, scale_px(48, w))
    f_sub = fit_sub_lines_font(draw, sub_strs, block_w, w, locale=locale, max_size=sub_max)

    sub_layouts: list[tuple[str, tuple[int, int, int, int]]] = []
    total_sub_h = 0
    for i, line_s in enumerate(sub_strs):
        bb = draw.textbbox((0, 0), line_s, font=f_sub)
        th = bb[3] - bb[1]
        sub_layouts.append((line_s, bb))
        total_sub_h += th
        if i < len(sub_strs) - 1:
            total_sub_h += sub_line_gap

    bottom_pad = max(scale_px(80, w), 36)
    y_sub = h - bottom_pad - total_sub_h
    for i, (line, bb) in enumerate(sub_layouts):
        lw_line = bb[2] - bb[0]
        th = bb[3] - bb[1]
        x = (w - lw_line) // 2
        draw_stroke_text(draw, (x, y_sub), line, font=f_sub, fill=fill, stroke=stroke_c, stroke_w=3)
        y_sub += th + (sub_line_gap if i < len(sub_layouts) - 1 else 0)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    im.convert("RGB").save(out_path, "PNG", optimize=True)
    print(f"Wrote {out_path} ({w}x{h})")
    return out_path


def main() -> None:
    if not MARKETING_PATH.is_file():
        raise SystemExit(f"Missing {MARKETING_PATH}")

    parser = argparse.ArgumentParser(
        description="Generate screenshot-14.png from screenshot-N-capture per locale (default N=13).",
    )
    parser.add_argument(
        "--ipad",
        action="store_true",
        help=f"Use {SCREENSHOTS_IPAD_DIR.name}/{{locale}}/ (phone default: {SCREENSHOTS_DIR.name}/).",
    )
    parser.add_argument(
        "--capture-num",
        type=int,
        default=13,
        metavar="N",
        help="Input file per locale: screenshot-N-capture.png (default: 13). Example: 15 for screenshot-15-capture.png.",
    )
    parser.add_argument(
        "--locale",
        action="append",
        dest="locales",
        metavar="CODE",
        help="Locale code (repeat for multiple). Default: all with MARKETING and the capture file present.",
    )
    args = parser.parse_args()

    if args.capture_num < 1:
        raise SystemExit("--capture-num must be >= 1")

    screenshots_root = SCREENSHOTS_IPAD_DIR if args.ipad else SCREENSHOTS_DIR

    if args.locales:
        to_run = [x.strip() for x in args.locales if x.strip()]
    else:
        to_run = [loc for loc in LOCALE_ORDER if loc in MARKETING]

    for loc in to_run:
        try:
            render_screenshot_14(loc, screenshots_root=screenshots_root, capture_num=args.capture_num)
        except FileNotFoundError as e:
            print(f"Skip {loc}: {e}")
        except ValueError as e:
            print(f"Error {loc}: {e}")


if __name__ == "__main__":
    main()

"""Compose App Store–style frames (1242×2688): gradient + slogan + device; writes screenshot-{n}.png.

Style: gradient background, dark green slogan; device: iOS (iPhone bezel + Dynamic Island) vs Android (legacy frame).
Copy: screenshot-14-marketing.json — 11 = sub[0], 12 = sub[1], 13 or 15 = headline;
      20 = sub[0], 21 = sub[1].
Input: screenshot-{n}-capture.png (raw device shot).
Output: screenshot-{n}.png — iOS → dla-docs/screenshots/, Android → dla-docs/screenshots-android/ (same layout).
Android: current frame (no status bar). iOS: graphite frame + Dynamic Island only (no clock/signal/battery row).

Usage:
  python generate-promo-screenshots.py
  python generate-promo-screenshots.py --locale en --platform ios
  python generate-promo-screenshots.py --platform android
  python generate-promo-screenshots.py --only 11 13 20 21
  python generate-promo-screenshots.py --all-locales --only 13 20 21
  python generate-promo-screenshots.py --all-locales --only 15 20 21
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
SCREENSHOTS_DIR = ROOT / "screenshots"
SCREENSHOTS_ANDROID_DIR = ROOT / "screenshots-android"
MARKETING_PATH = SCRIPT_DIR / "screenshot-14-marketing.json"

W_CANVAS = 1242
H_CANVAS = 2688

# Reference: dark forest green type (#1B4332); background gradient (top → bottom)
TEXT_GREEN = (27, 67, 50)
GRADIENT_TOP = (255, 252, 242)
GRADIENT_BOTTOM = (228, 238, 232)

TEXT_MARGIN_X = 56
TEXT_TOP = 148
TEXT_LINE_GAP = 12
TEXT_BLOCK_TAIL = 16
PHONE_GAP_BELOW_TEXT = 40
# Fixed Y for top of device (same for promo 11/12/13 so frames align when swiped)
PHONE_TOP_Y = 612
# Outer device width vs canvas (bezel + screen + island drawn in code)
PHONE_WIDTH_FRAC = 0.88
DEVICE_H_OVER_W = 2.08
# Min gap between phone bottom and canvas bottom (after width clamp)
CANVAS_BOTTOM_PAD = 16
BEZEL_FRAC = 0.034
R_OUTER_FRAC = 0.088
R_INNER_FRAC = 0.062
# Promo 20 & 21: reserve this many pixels at the top of the inner screen, then re-fit the
# capture into the shorter viewport — otherwise nh often equals ih and a naive py+offset
# clamp cancels the shift entirely (no visible movement).
SCREENSHOT_PROMO_SHOT_OFFSET_Y = 64
# Promo 20 & 21: inner screen letterbox — matches app `colors.background`
SCREENSHOT_PROMO_APP_BG = (245, 245, 245, 255)  # #F5F5F5
# Promo 21: fallback LR inset if screenshot-20-capture.png is missing (same folder as 21).
SCREENSHOT_21_HORIZONTAL_INSET_FRAC = 0.028


def phone_inner_screen_dimensions(
    outer_w: int,
    *,
    content_offset_y: int = 0,
) -> tuple[int, int]:
    """Inner width `iw` and `ih_avail` after vertical promo inset — must match compose_phone_device."""
    ow = outer_w
    oh = int(ow * DEVICE_H_OVER_W)
    b = max(14, int(ow * BEZEL_FRAC))
    iw, ih = ow - 2 * b, oh - 2 * b
    offset_y = int(content_offset_y) if content_offset_y > 0 else 0
    ih_avail = ih - offset_y if offset_y > 0 else ih
    if ih_avail < 48:
        ih_avail = ih
    return iw, ih_avail


def contain_fit_horizontal_gutter_px(sw: int, sh: int, iw: int, ih_avail: int) -> int:
    """One-sided horizontal gap for contain-fit with full inner width (inset_lr = 0)."""
    scale = min(iw / sw, ih_avail / sh)
    nw = max(1, int(sw * scale))
    return max(0, (iw - nw) // 2)


def _load_find_font():
    path = SCRIPT_DIR / "generate-screenshot-14-appstore.py"
    spec = importlib.util.spec_from_file_location("_g14_find_font", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.find_font


find_font = _load_find_font()


def draw_cream_background(w: int, h: int) -> Image.Image:
    """Vertical RGB gradient; cheap build via 1×h strip + resize."""
    top = GRADIENT_TOP
    bot = GRADIENT_BOTTOM
    col = Image.new("RGB", (1, h))
    px = col.load()
    denom = max(h - 1, 1)
    for y in range(h):
        t = y / denom
        r = int(top[0] + (bot[0] - top[0]) * t)
        g = int(top[1] + (bot[1] - top[1]) * t)
        b = int(top[2] + (bot[2] - top[2]) * t)
        px[0, y] = (r, g, b)
    return col.resize((w, h), Image.Resampling.NEAREST).convert("RGBA")


def wrap_paragraph(
    draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_w: int
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
    lines = []
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


def slogan_text_bottom_y(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    font: ImageFont.FreeTypeFont,
    top_y: int,
) -> int:
    """Bottom Y of slogan block (matches compose_promo drawing loop + TEXT_BLOCK_TAIL)."""
    y = top_y
    for line in lines:
        bb = draw.textbbox((0, 0), line, font=font)
        y += bb[3] - bb[1] + TEXT_LINE_GAP
    return y + TEXT_BLOCK_TAIL


def fit_slogan_for_fixed_phone(
    draw: ImageDraw.ImageDraw,
    slogan: str,
    max_w: int,
    max_text_bottom: int,
    top_y: int,
    *,
    locale: str,
    start: int,
    minimum: int,
) -> tuple[ImageFont.FreeTypeFont, list[str]]:
    for sz in range(start, minimum - 1, -2):
        fh = find_font(sz, bold=True, locale=locale)
        wrapped = wrap_paragraph(draw, slogan, fh, max_w)
        ok_w = True
        for line in wrapped:
            bb = draw.textbbox((0, 0), line, font=fh)
            if bb[2] - bb[0] > max_w:
                ok_w = False
                break
        if not ok_w:
            continue
        if slogan_text_bottom_y(draw, wrapped, fh, top_y) <= max_text_bottom:
            return fh, wrapped
    fh = find_font(minimum, bold=True, locale=locale)
    wrapped = wrap_paragraph(draw, slogan, fh, max_w)
    return fh, wrapped


def fit_single_line_font(
    draw: ImageDraw.ImageDraw,
    text: str,
    max_w: int,
    *,
    locale: str,
    start: int,
    minimum: int,
    bold: bool,
) -> ImageFont.FreeTypeFont:
    for sz in range(start, minimum - 1, -2):
        f = find_font(sz, bold=bold, locale=locale)
        bb = draw.textbbox((0, 0), text, font=f)
        if bb[2] - bb[0] <= max_w:
            return f
    return find_font(minimum, bold=bold, locale=locale)


def compose_phone_device(
    shot: Image.Image,
    outer_w: int,
    *,
    inner_letterbox: tuple[int, int, int, int] = (12, 12, 14, 255),
    inner_screen_title: str | None = None,
    inner_screen_footer: str | None = None,
    locale: str = "en",
    device_style: str = "android",
    content_offset_y: int = 0,
    content_inset_lr_px: int = 0,
) -> Image.Image:
    """Phone body + inner screen (`contain` shot). Android: current look. iOS: graphite + Dynamic Island (no status icons)."""
    shot = shot.convert("RGBA")
    is_ios = device_style.lower() == "ios"
    ow = outer_w
    oh = int(ow * DEVICE_H_OVER_W)
    b = max(14, int(ow * BEZEL_FRAC))
    r_out = max(40, int(ow * 0.092)) if is_ios else max(36, int(ow * R_OUTER_FRAC))
    r_in = max(26, int(ow * R_INNER_FRAC))
    iw, ih = ow - 2 * b, oh - 2 * b
    ix, iy = b, b

    isl_w = int(iw * 0.34)
    isl_h = max(26, int(ow * 0.026))
    isl_x = ix + (iw - isl_w) // 2
    isl_y = iy + max(10, int(ih * 0.015))

    body_rgb = (48, 48, 52, 255) if is_ios else (46, 46, 50, 255)
    dev = Image.new("RGBA", (ow, oh), (0, 0, 0, 0))
    body_draw = ImageDraw.Draw(dev)
    body_draw.rounded_rectangle((0, 0, ow, oh), radius=r_out, fill=body_rgb)

    sw, sh = shot.size
    # Fit into ih_avail < ih when shifting down: scales nh smaller and places content lower.
    # Adding py offset alone fails when nh == ih (contain height-fill) — clamp removed the shift.
    offset_y = int(content_offset_y) if content_offset_y > 0 else 0
    ih_avail = ih - offset_y if offset_y > 0 else ih
    if ih_avail < 48:
        ih_avail = ih
        offset_y = 0

    inset_lr = max(0, int(content_inset_lr_px))
    iw_fit = iw - 2 * inset_lr
    if iw_fit < 48:
        iw_fit = iw
        inset_lr = 0

    scale = min(iw_fit / sw, ih_avail / sh)
    nw, nh = max(1, int(sw * scale)), max(1, int(sh * scale))
    fitted = shot.resize((nw, nh), Image.Resampling.LANCZOS)
    px = ix + inset_lr + (iw_fit - nw) // 2
    py = iy + offset_y + (ih_avail - nh) // 2

    screen_layer = Image.new("RGBA", (ow, oh), (0, 0, 0, 0))
    inner_bg = Image.new("RGBA", (iw, ih), inner_letterbox)
    screen_layer.paste(inner_bg, (ix, iy))
    screen_layer.paste(fitted, (px, py), fitted)

    if inner_screen_title and inner_screen_title.strip():
        title = inner_screen_title.strip()
        band_top = isl_y + isl_h + 8
        band_bot = py - 8
        if band_bot > band_top + 14:
            pad_x = max(12, int(iw * 0.055))
            max_tw = iw - 2 * pad_x
            t_start = max(42, int(iw * 0.072))
            t_min = max(24, int(iw * 0.046))
            sdraw = ImageDraw.Draw(screen_layer)
            fn = fit_single_line_font(
                sdraw, title, max_tw, locale=locale, start=t_start, minimum=t_min, bold=True
            )
            nb = sdraw.textbbox((0, 0), title, font=fn)
            tw, th = nb[2] - nb[0], nb[3] - nb[1]
            tx = ix + (iw - tw) // 2
            ty = (band_top + band_bot - th) // 2
            sdraw.text((tx, ty), title, font=fn, fill=(*TEXT_GREEN, 255))

    if inner_screen_footer and inner_screen_footer.strip():
        footer = inner_screen_footer.strip()
        band_top = py + nh + 10
        band_bot = iy + ih - 12
        pad_x = max(12, int(iw * 0.055))
        max_tw = iw - 2 * pad_x
        available_h = band_bot - band_top
        if available_h > 28:
            sdraw = ImageDraw.Draw(screen_layer)
            max_sz = max(42, int(iw * 0.065))
            min_sz = max(24, int(iw * 0.042))
            chosen_font: ImageFont.FreeTypeFont | None = None
            chosen_lines: list[str] | None = None
            for sz in range(max_sz, min_sz - 1, -2):
                f = find_font(sz, bold=True, locale=locale)
                lines = wrap_paragraph(sdraw, footer, f, max_tw)
                line_h = 0
                for line in lines:
                    lb = sdraw.textbbox((0, 0), line, font=f)
                    line_h += lb[3] - lb[1] + 6
                line_h -= 6
                if line_h <= available_h:
                    chosen_font = f
                    chosen_lines = lines
                    break
            ff = chosen_font or find_font(min_sz, bold=True, locale=locale)
            lines = chosen_lines or wrap_paragraph(sdraw, footer, ff, max_tw)
            th = 0
            line_metrics: list[tuple[str, tuple[int, int, int, int]]] = []
            for line in lines:
                bb = sdraw.textbbox((0, 0), line, font=ff)
                line_metrics.append((line, bb))
                th += bb[3] - bb[1] + 6
            th -= 6
            ty = band_top + max(0, (available_h - th) // 2)
            fill_f = (*TEXT_GREEN, 255)
            for line, bb in line_metrics:
                lw = bb[2] - bb[0]
                tx = ix + (iw - lw) // 2
                sdraw.text((tx, ty), line, font=ff, fill=fill_f)
                ty += bb[3] - bb[1] + 6

    inner_mask = Image.new("L", (ow, oh), 0)
    ImageDraw.Draw(inner_mask).rounded_rectangle(
        (ix, iy, ix + iw - 1, iy + ih - 1), radius=r_in, fill=255
    )
    clipped = Image.new("RGBA", (ow, oh), (0, 0, 0, 0))
    clipped.paste(screen_layer, (0, 0), inner_mask)
    dev = Image.alpha_composite(dev, clipped)

    island_fill = (20, 20, 22, 255) if is_ios else (10, 10, 12, 255)
    top_draw = ImageDraw.Draw(dev)
    top_draw.rounded_rectangle(
        (isl_x, isl_y, isl_x + isl_w, isl_y + isl_h),
        radius=isl_h // 2,
        fill=island_fill,
    )
    return dev


def compose_promo(
    screenshot_path: Path,
    slogan: str,
    out_path: Path,
    *,
    locale: str,
    screenshot_index: int,
    device_style: str,
    app_name: str | None = None,
    inner_screen_footer: str | None = None,
) -> None:
    max_text_w = W_CANVAS - 2 * TEXT_MARGIN_X
    base = draw_cream_background(W_CANVAS, H_CANVAS).convert("RGBA")
    draw = ImageDraw.Draw(base)

    start_sz = max(62, int(W_CANVAS * 0.069))
    min_sz = max(40, int(W_CANVAS * 0.046))

    max_text_bottom = PHONE_TOP_Y - PHONE_GAP_BELOW_TEXT
    fh, wrapped = fit_slogan_for_fixed_phone(
        draw,
        slogan,
        max_text_w,
        max_text_bottom,
        TEXT_TOP,
        locale=locale,
        start=start_sz,
        minimum=min_sz,
    )

    y = TEXT_TOP
    fill = (*TEXT_GREEN, 255)
    for line in wrapped:
        bb = draw.textbbox((0, 0), line, font=fh)
        lw = bb[2] - bb[0]
        x = (W_CANVAS - lw) // 2
        draw.text((x, y), line, font=fh, fill=fill)
        y += bb[3] - bb[1] + TEXT_LINE_GAP

    y_phone = PHONE_TOP_Y
    max_phone_h = max(120, H_CANVAS - y_phone - CANVAS_BOTTOM_PAD)
    outer_w_target = int(W_CANVAS * PHONE_WIDTH_FRAC)
    phone_h_if = int(outer_w_target * DEVICE_H_OVER_W)
    if phone_h_if > max_phone_h:
        outer_w = max(280, int(max_phone_h / DEVICE_H_OVER_W))
    else:
        outer_w = outer_w_target

    shot_offset_y = SCREENSHOT_PROMO_SHOT_OFFSET_Y if screenshot_index in (20, 21) else 0

    content_inset_lr_px = 0
    if screenshot_index == 21:
        iw_m, ih_avail_m = phone_inner_screen_dimensions(
            outer_w, content_offset_y=shot_offset_y
        )
        cap20_path = screenshot_path.parent / "screenshot-20-capture.png"
        if cap20_path.is_file():
            with Image.open(cap20_path) as im20:
                sw20, sh20 = im20.size
            content_inset_lr_px = contain_fit_horizontal_gutter_px(sw20, sh20, iw_m, ih_avail_m)
        else:
            content_inset_lr_px = max(0, int(round(iw_m * SCREENSHOT_21_HORIZONTAL_INSET_FRAC)))

    shot = Image.open(screenshot_path).convert("RGBA")
    is_13_style = screenshot_index in (13, 15, 20)
    if screenshot_index in (20, 21):
        inner_bg = SCREENSHOT_PROMO_APP_BG
    elif is_13_style:
        inner_bg = (255, 255, 255, 255)
    else:
        inner_bg = (12, 12, 14, 255)
    title_in_phone = app_name.strip() if (is_13_style and app_name and app_name.strip()) else None
    footer_in_phone = inner_screen_footer.strip() if (is_13_style and inner_screen_footer and inner_screen_footer.strip()) else None
    phone = compose_phone_device(
        shot,
        outer_w,
        inner_letterbox=inner_bg,
        inner_screen_title=title_in_phone,
        inner_screen_footer=footer_in_phone,
        locale=locale,
        device_style=device_style,
        content_offset_y=shot_offset_y,
        content_inset_lr_px=content_inset_lr_px,
    )
    pw = phone.size[0]

    x_phone = (W_CANVAS - pw) // 2

    layer = Image.new("RGBA", (W_CANVAS, H_CANVAS), (0, 0, 0, 0))
    layer.paste(phone, (x_phone, y_phone), phone)
    base = Image.alpha_composite(base, layer)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    base.convert("RGB").save(out_path, "PNG", optimize=True)
    print(f"Wrote {out_path}")


def promo13_inner_footer(block: dict[str, object]) -> str | None:
    raw = block.get("phone_inner_footer")
    if raw and str(raw).strip():
        return str(raw).strip()
    return None


def slogan_for_index(block: dict[str, object], index: int) -> str | None:
    if index == 11:
        sub = block.get("sub")
        if isinstance(sub, list) and len(sub) > 0:
            return str(sub[0])
        return None
    if index == 12:
        sub = block.get("sub")
        if isinstance(sub, list) and len(sub) > 1:
            return str(sub[1])
        return None
    if index in (13, 15):
        raw = block.get("headline", "")
        return str(raw) if raw else None
    if index == 20:
        sub = block.get("sub")
        if isinstance(sub, list) and len(sub) > 0:
            return str(sub[0])
        return None
    if index == 21:
        sub = block.get("sub")
        if isinstance(sub, list) and len(sub) > 1:
            return str(sub[1])
        return None
    return None


def main() -> None:
    parser = argparse.ArgumentParser(
        description="1242×2688 frames from screenshot-{n}-capture.png + marketing → screenshot-{n}.png."
    )
    parser.add_argument("--locale", default="vi", help="Locale key in JSON + folder under screenshots/")
    parser.add_argument(
        "--all-locales",
        action="store_true",
        help="Process every locale in screenshot-14-marketing.json (overrides --locale).",
    )
    parser.add_argument(
        "--only",
        nargs="*",
        metavar="N",
        type=int,
        help="Screenshot numbers (default: 11 12 13). 13 or 15=headline; 20=sub[0]; 21=sub[1].",
    )
    parser.add_argument(
        "--platform",
        choices=("ios", "android", "both"),
        default="both",
        help="ios → screenshots/ + iPhone UI; android → screenshots-android/ + current frame; both (default).",
    )
    args = parser.parse_args()

    if not MARKETING_PATH.is_file():
        raise SystemExit(f"Missing {MARKETING_PATH}")

    marketing: dict[str, dict[str, object]] = json.loads(MARKETING_PATH.read_text(encoding="utf-8"))

    if args.all_locales:
        locales = sorted(marketing.keys())
    else:
        loc = args.locale
        if loc not in marketing:
            raise SystemExit(f"No locale '{loc}' in {MARKETING_PATH}")
        locales = [loc]

    nums = args.only if args.only else [11, 12, 13]
    platforms: tuple[str, ...]
    if args.platform == "both":
        platforms = ("ios", "android")
    else:
        platforms = (args.platform,)

    for loc in locales:
        block = marketing[loc]
        locale_dir_src = SCREENSHOTS_DIR / loc

        for n in nums:
            capture_name = f"screenshot-{n}-capture.png"
            out_name = f"screenshot-{n}.png"
            slogan = slogan_for_index(block, n)
            if not slogan or not slogan.strip():
                print(f"[{loc}] Skip {out_name}: no slogan mapped for index {n}")
                continue
            src = locale_dir_src / capture_name
            if not src.is_file():
                print(f"[{loc}] Skip {out_name}: missing source {src}")
                continue
            raw_app = block.get("app_name")
            app = str(raw_app).strip() if raw_app else None
            inner_f = promo13_inner_footer(block) if n in (13, 15, 20) else None
            for plat in platforms:
                out_root = SCREENSHOTS_ANDROID_DIR if plat == "android" else SCREENSHOTS_DIR
                out_root.mkdir(parents=True, exist_ok=True)
                out_dir = out_root / loc
                out_dir.mkdir(parents=True, exist_ok=True)
                out = out_dir / out_name
                compose_promo(
                    src,
                    slogan.strip(),
                    out,
                    locale=loc,
                    screenshot_index=n,
                    device_style=plat,
                    app_name=app,
                    inner_screen_footer=inner_f,
                )


if __name__ == "__main__":
    main()

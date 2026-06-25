"""Compose App Store–style frames: gradient + slogan + device; writes screenshot-{n}.png.

Phone: 1242×2688 (screenshots/, screenshots-android/). iPad: 2048×2732 (screenshots-ipad/).
Style: gradient background, dark green slogan; device: iOS (iPhone bezel + Dynamic Island) vs Android (legacy frame) vs iPad (tablet frame).
Copy: screenshot-14-marketing.json — 11 = sub[0], 12 = sub[1], 13 or 15 = headline;
      headline is a string (single line) or [above screenshot, below screenshot] array;
      promo 15 uses [0] above the phone and [1] below the screenshot;
      20 = sub[0], 21 = sub[1].
Input: screenshot-{n}-capture.png (raw device shot).
Output: screenshot-{n}.png — iOS → dla-docs/screenshots/, Android → dla-docs/screenshots-android/, iPad → dla-docs/screenshots-ipad/.
Promo 15: headline[0] above the phone, headline[1] below the screenshot; phone on the right,
  wife/husband avatars stacked on the left; QR hub in the middle with dashed links
  (phone ↔ hub horizontal, hub ↔ avatars curved); defaults: scripts/assets/promo-15-wife.png,
  promo-15-husband.png.
Android: current frame (no status bar). iOS: graphite frame + Dynamic Island only (no clock/signal/battery row).

Usage:
  python generate-promo-screenshots.py
  python generate-promo-screenshots.py --locale en --platform ios
  python generate-promo-screenshots.py --platform android
  python generate-promo-screenshots.py --ipad
  python generate-promo-screenshots.py --ipad --locale en --only 15 20 21
  python generate-promo-screenshots.py --only 11 13 20 21
  python generate-promo-screenshots.py --all-locales --only 13 20 21
  python generate-promo-screenshots.py --all-locales --only 15 20 21
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
SCREENSHOTS_DIR = ROOT / "screenshots"
SCREENSHOTS_ANDROID_DIR = ROOT / "screenshots-android"
SCREENSHOTS_IPAD_DIR = ROOT / "screenshots-ipad"
MARKETING_PATH = SCRIPT_DIR / "screenshot-14-marketing.json"
PROMO_15_ASSETS_DIR = SCRIPT_DIR / "assets"
PROMO_15_WIFE_AVATAR = PROMO_15_ASSETS_DIR / "promo-15-wife.png"
PROMO_15_HUSBAND_AVATAR = PROMO_15_ASSETS_DIR / "promo-15-husband.png"
PROMO_15_FAKE_QR = PROMO_15_ASSETS_DIR / "fake-qr.png"

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

# Promo 15 — split layout (headline / avatars left / phone right)
PROMO_15_AVATAR_DIAMETER = 252
PROMO_15_AVATAR_WHITE_BORDER = 10
PROMO_15_AVATAR_RENDER_SCALE = 2
PROMO_15_AVATAR_LEFT = 52
PROMO_15_AVATAR_V_GAP = 72
PROMO_15_PHONE_WIDTH_FRAC = 0.44
PROMO_15_PHONE_RIGHT_MARGIN = 28
PROMO_15_PHONE_HEADLINE_GAP = 36
PROMO_15_PHONE_MIN_OUTER_W = 260
PROMO_15_CONNECTOR_WIDTH = 9
PROMO_15_CONNECTOR_DASH = 8
PROMO_15_CONNECTOR_GAP = 8
PROMO_15_CONNECTOR_COLOR = (39, 130, 92, 235)
PROMO_15_HUB_AVATAR_GAP = 0
PROMO_15_HUB_SHIFT_LEFT = 36
PROMO_15_CONNECTOR_CORNER_RADIUS = 26
PROMO_15_QR_TOUCH_OVERLAP = 20
PROMO_15_QR_PHONE_EDGE_OFFSET = 34
PROMO_15_PHONE_LINK_END_GAP = 6
PROMO_15_LINK_LABEL_FONT = 34
PROMO_15_LINK_LABEL_GAP_RIGHT = 24
PROMO_HEADLINE_FONT_START = max(62, int(W_CANVAS * 0.069))
PROMO_HEADLINE_FONT_MIN = max(40, int(W_CANVAS * 0.046))
PROMO_15_HEADLINE_EDGE_MARGIN = TEXT_TOP
PROMO_15_HEADLINE_BOTTOM_LIFT = 40
PROMO_15_HEADLINE_TOP_FONT_START = max(80, int(W_CANVAS * 0.086))
PROMO_15_HEADLINE_TOP_FONT_MIN = max(50, int(W_CANVAS * 0.054))
PROMO_15_HEADLINE_TOP_LINE_GAP = 10


@dataclass(frozen=True)
class PromoLayout:
    """Canvas + layout constants for phone (1242×2688) or iPad (2048×2732)."""

    w_canvas: int
    h_canvas: int
    device_h_over_w: float
    phone_width_frac: float
    promo_15_phone_width_frac: float

    def scale_x(self, value: int) -> int:
        return int(round(value * self.w_canvas / W_CANVAS))

    def scale_y(self, value: int) -> int:
        return int(round(value * self.h_canvas / H_CANVAS))

    @property
    def text_margin_x(self) -> int:
        return self.scale_x(TEXT_MARGIN_X)

    @property
    def text_top(self) -> int:
        return self.scale_y(TEXT_TOP)

    @property
    def text_line_gap(self) -> int:
        return self.scale_y(TEXT_LINE_GAP)

    @property
    def text_block_tail(self) -> int:
        return self.scale_y(TEXT_BLOCK_TAIL)

    @property
    def phone_gap_below_text(self) -> int:
        return self.scale_y(PHONE_GAP_BELOW_TEXT)

    @property
    def phone_top_y(self) -> int:
        return self.scale_y(PHONE_TOP_Y)

    @property
    def canvas_bottom_pad(self) -> int:
        return self.scale_y(CANVAS_BOTTOM_PAD)

    @property
    def screenshot_promo_shot_offset_y(self) -> int:
        return self.scale_y(SCREENSHOT_PROMO_SHOT_OFFSET_Y)

    @property
    def promo_headline_font_start(self) -> int:
        return max(62, int(self.w_canvas * 0.069))

    @property
    def promo_headline_font_min(self) -> int:
        return max(40, int(self.w_canvas * 0.046))

    @property
    def promo_15_headline_top_font_start(self) -> int:
        return max(80, int(self.w_canvas * 0.086))

    @property
    def promo_15_headline_top_font_min(self) -> int:
        return max(50, int(self.w_canvas * 0.054))


PHONE_LAYOUT = PromoLayout(
    w_canvas=W_CANVAS,
    h_canvas=H_CANVAS,
    device_h_over_w=DEVICE_H_OVER_W,
    phone_width_frac=PHONE_WIDTH_FRAC,
    promo_15_phone_width_frac=PROMO_15_PHONE_WIDTH_FRAC,
)

IPAD_LAYOUT = PromoLayout(
    w_canvas=2048,
    h_canvas=2732,
    device_h_over_w=1.44,
    phone_width_frac=0.90,
    promo_15_phone_width_frac=0.50,
)

COMPACT_PROMO_INDICES = (15, 20, 21)


def promo_headline_font_sizes(
    layout: PromoLayout,
    screenshot_index: int,
    *,
    top_headline: bool = False,
) -> tuple[int, int]:
    """Smaller headline bounds for promo 15/20/21 (especially on iPad)."""
    if top_headline:
        start = layout.promo_15_headline_top_font_start
        minimum = layout.promo_15_headline_top_font_min
    else:
        start = layout.promo_headline_font_start
        minimum = layout.promo_headline_font_min

    if screenshot_index not in COMPACT_PROMO_INDICES:
        return start, minimum

    if layout.w_canvas > W_CANVAS:
        scale = 0.82 if top_headline else 0.82
    else:
        scale = 0.82

    start = max(int(minimum * scale), int(start * scale))
    minimum = max(32, int(minimum * scale))
    return start, minimum


def phone_inner_screen_dimensions(
    outer_w: int,
    *,
    layout: PromoLayout,
    content_offset_y: int = 0,
) -> tuple[int, int]:
    """Inner width `iw` and `ih_avail` after vertical promo inset — must match compose_phone_device."""
    ow = outer_w
    oh = int(ow * layout.device_h_over_w)
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
    *,
    line_gap: int = TEXT_LINE_GAP,
    text_block_tail: int = TEXT_BLOCK_TAIL,
) -> int:
    """Bottom Y of slogan block (matches compose_promo drawing loop + TEXT_BLOCK_TAIL)."""
    y = top_y
    for line in lines:
        bb = draw.textbbox((0, 0), line, font=font)
        y += bb[3] - bb[1] + line_gap
    return y + text_block_tail


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
    line_gap: int = TEXT_LINE_GAP,
    text_block_tail: int = TEXT_BLOCK_TAIL,
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
        if slogan_text_bottom_y(
            draw, wrapped, fh, top_y, line_gap=line_gap, text_block_tail=text_block_tail
        ) <= max_text_bottom:
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
    layout: PromoLayout,
    inner_letterbox: tuple[int, int, int, int] = (12, 12, 14, 255),
    inner_screen_title: str | None = None,
    inner_screen_footer: str | None = None,
    locale: str = "en",
    device_style: str = "android",
    content_offset_y: int = 0,
    content_inset_lr_px: int = 0,
) -> Image.Image:
    """Phone/tablet body + inner screen (`contain` shot). Android: current look. iOS: graphite + Dynamic Island. iPad: tablet frame."""
    shot = shot.convert("RGBA")
    style = device_style.lower()
    is_ipad = style == "ipad"
    is_ios = style == "ios" or is_ipad
    ow = outer_w
    oh = int(ow * layout.device_h_over_w)
    b = max(14, int(ow * BEZEL_FRAC))
    r_out = max(40, int(ow * 0.092)) if is_ios else max(36, int(ow * R_OUTER_FRAC))
    if is_ipad:
        r_out = max(48, int(ow * 0.055))
    r_in = max(26, int(ow * R_INNER_FRAC))
    if is_ipad:
        r_in = max(30, int(ow * 0.045))
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

    if not is_ipad:
        island_fill = (20, 20, 22, 255) if is_ios else (10, 10, 12, 255)
        top_draw = ImageDraw.Draw(dev)
        top_draw.rounded_rectangle(
            (isl_x, isl_y, isl_x + isl_w, isl_y + isl_h),
            radius=isl_h // 2,
            fill=island_fill,
        )
    return dev


def resolve_promo_asset_path(block: dict[str, object], key: str, default: Path) -> Path:
    raw = block.get(key)
    if raw and str(raw).strip():
        path = Path(str(raw).strip())
        if not path.is_absolute():
            path = SCRIPT_DIR / path
        return path
    return default


def _avatar_box(d: int, x1: float, y1: float, x2: float, y2: float) -> tuple[float, float, float, float]:
    k = d / 400.0
    return x1 * k, y1 * k, x2 * k, y2 * k


def render_cheerful_avatar_face(diameter: int, *, variant: str) -> Image.Image:
    """Flat cheerful portrait avatar (reference-style illustration)."""
    palettes = {
        "husband": {
            "bg": (224, 49, 49),
            "hoodie": (37, 99, 235),
            "skin": (255, 205, 178),
            "hair": (24, 24, 28),
            "eye": (20, 20, 24),
            "lip": (232, 150, 130),
        },
        "wife": {
            "bg": (240, 101, 149),
            "hoodie": (124, 58, 237),
            "skin": (255, 214, 196),
            "hair": (92, 51, 23),
            "eye": (20, 20, 24),
            "lip": (235, 155, 140),
        },
    }
    if variant not in palettes:
        raise ValueError(f"Unknown avatar variant: {variant}")
    pal = palettes[variant]

    d = diameter
    k = d / 400.0
    img = Image.new("RGBA", (d, d), (0, 0, 0, 0))
    dr = ImageDraw.Draw(img)
    box = lambda x1, y1, x2, y2: _avatar_box(d, x1, y1, x2, y2)

    dr.ellipse(box(0, 0, 400, 400), fill=pal["bg"])
    dr.ellipse(box(10, 232, 390, 408), fill=pal["hoodie"])
    dr.ellipse(box(158, 218, 242, 292), fill=pal["skin"])
    dr.ellipse(box(102, 96, 298, 292), fill=pal["skin"])
    dr.ellipse(box(96, 176, 118, 218), fill=pal["skin"])
    dr.ellipse(box(282, 176, 304, 218), fill=pal["skin"])

    if variant == "husband":
        dr.ellipse(box(92, 70, 308, 198), fill=pal["hair"])
        dr.polygon(
            [(130 * k, 82 * k), (148 * k, 48 * k), (166 * k, 84 * k)],
            fill=pal["hair"],
        )
        dr.polygon(
            [(188 * k, 68 * k), (206 * k, 42 * k), (224 * k, 76 * k)],
            fill=pal["hair"],
        )
        dr.polygon(
            [(248 * k, 78 * k), (268 * k, 50 * k), (286 * k, 86 * k)],
            fill=pal["hair"],
        )
        dr.rectangle(box(92, 128, 128, 196), fill=pal["hair"])
        dr.rectangle(box(272, 128, 308, 196), fill=pal["hair"])
    else:
        dr.ellipse(box(82, 72, 318, 210), fill=pal["hair"])
        dr.ellipse(box(62, 132, 132, 278), fill=pal["hair"])
        dr.ellipse(box(268, 132, 338, 278), fill=pal["hair"])
        dr.ellipse(box(108, 82, 292, 168), fill=pal["hair"])
        dr.ellipse(box(112, 118, 288, 292), fill=pal["skin"])

    dr.rounded_rectangle(box(142, 146, 190, 153), radius=max(2, int(3 * k)), fill=pal["hair"])
    dr.rounded_rectangle(box(210, 146, 258, 153), radius=max(2, int(3 * k)), fill=pal["hair"])

    for ex in (168, 232):
        dr.ellipse(box(ex - 15, 166, ex + 15, 198), fill=pal["eye"])
        dr.ellipse(box(ex + 2, 172, ex + 10, 180), fill=(255, 255, 255))

    dr.chord(box(132, 196, 268, 252), start=180, end=360, fill=(255, 255, 255))
    dr.line(
        (142 * k, 226 * k, 258 * k, 226 * k),
        fill=pal["lip"],
        width=max(2, int(3 * k)),
    )

    img.putalpha(_disk_alpha_mask(d, d / 2.0, d / 2.0, d / 2.0))
    return img


def _disk_alpha_mask(size: int, cx: float, cy: float, radius: float) -> Image.Image:
    mask = Image.new("L", (size, size), 0)
    px = mask.load()
    r2 = radius * radius
    y0 = max(0, int(cy - radius - 1))
    y1 = min(size, int(cy + radius + 2))
    x0 = max(0, int(cx - radius - 1))
    x1 = min(size, int(cx + radius + 2))
    for y in range(y0, y1):
        dy = y + 0.5 - cy
        for x in range(x0, x1):
            dx = x + 0.5 - cx
            if dx * dx + dy * dy <= r2:
                px[x, y] = 255
    return mask


def _ring_alpha_mask(
    size: int,
    cx: float,
    cy: float,
    inner_r: float,
    outer_r: float,
) -> Image.Image:
    mask = Image.new("L", (size, size), 0)
    px = mask.load()
    ir2 = inner_r * inner_r
    or2 = outer_r * outer_r
    y0 = max(0, int(cy - outer_r - 1))
    y1 = min(size, int(cy + outer_r + 2))
    x0 = max(0, int(cx - outer_r - 1))
    x1 = min(size, int(cx + outer_r + 2))
    for y in range(y0, y1):
        dy = y + 0.5 - cy
        for x in range(x0, x1):
            dx = x + 0.5 - cx
            d2 = dx * dx + dy * dy
            if ir2 < d2 <= or2:
                px[x, y] = 255
    return mask


def _add_white_ring(face: Image.Image, border: int) -> Image.Image:
    diameter = face.size[0]
    outer = diameter + 2 * border
    cx = cy = outer / 2.0
    inner_r = diameter / 2.0
    outer_r = inner_r + border

    result = Image.new("RGBA", (outer, outer), (0, 0, 0, 0))
    ring = _ring_alpha_mask(outer, cx, cy, inner_r, outer_r)
    white = Image.new("RGBA", (outer, outer), (255, 255, 255, 255))
    result.paste(white, mask=ring)
    result.paste(face, (border, border), face)
    return result


def _load_photo_avatar_face(image_path: Path, diameter: int) -> Image.Image:
    """Load pre-circular PNG; keep native alpha edge."""
    img = Image.open(image_path).convert("RGBA")
    w, h = img.size
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    img = img.crop((left, top, left + side, top + side))
    return img.resize((diameter, diameter), Image.Resampling.LANCZOS)


def apply_promo_15_white_border(face: Image.Image, border: int) -> Image.Image:
    """Even white ring; source avatar is already a clean circle with alpha."""
    scale = PROMO_15_AVATAR_RENDER_SCALE
    d = face.size[0]
    if scale > 1:
        face_hr = face.resize((d * scale, d * scale), Image.Resampling.LANCZOS)
        composed = _add_white_ring(face_hr, border * scale)
        return composed.resize((d + 2 * border, d + 2 * border), Image.Resampling.LANCZOS)
    return _add_white_ring(face, border)


def create_promo_15_avatar(
    diameter: int,
    variant: str,
    image_path: Path | None,
) -> Image.Image:
    if image_path and image_path.is_file():
        inner = _load_photo_avatar_face(image_path, diameter)
    else:
        inner = render_cheerful_avatar_face(diameter, variant=variant)
    return apply_promo_15_white_border(inner, PROMO_15_AVATAR_WHITE_BORDER)


def resolve_promo_15_avatar_path(
    block: dict[str, object],
    json_key: str,
    cli_path: Path | None,
    default_path: Path,
) -> Path | None:
    if cli_path is not None:
        return cli_path
    raw = block.get(json_key)
    if raw and str(raw).strip():
        path = Path(str(raw))
        if not path.is_absolute():
            path = SCRIPT_DIR / path
        return path
    if default_path.is_file():
        return default_path
    return None


def promo_15_avatar_outer_size(layout: PromoLayout) -> int:
    return layout.scale_x(PROMO_15_AVATAR_DIAMETER) + 2 * layout.scale_x(PROMO_15_AVATAR_WHITE_BORDER)


def promo_15_content_block_height(phone_h: int, avatar_outer: int, layout: PromoLayout) -> int:
    hub_size = avatar_outer
    avatar_v_gap = layout.scale_y(PROMO_15_AVATAR_V_GAP)
    span = avatar_outer + avatar_v_gap + hub_size + avatar_v_gap + avatar_outer
    return max(phone_h, span)


def promo_15_min_center_height(layout: PromoLayout, gap: int, phone_width_frac: float) -> int:
    avatar_outer = promo_15_avatar_outer_size(layout)
    min_outer_w = layout.scale_x(PROMO_15_PHONE_MIN_OUTER_W)
    outer_w = max(min_outer_w, int(layout.w_canvas * phone_width_frac))
    phone_h = int(outer_w * layout.device_h_over_w)
    return promo_15_content_block_height(phone_h, avatar_outer, layout) + 2 * gap


def promo_15_phone_layout(
    top_end: int,
    bottom_start: int,
    *,
    layout: PromoLayout,
    phone_width_frac: float,
    avatar_outer: int,
) -> tuple[int, int]:
    """Center phone + avatars vertically between headline blocks."""
    available = bottom_start - top_end
    min_outer_w = layout.scale_x(PROMO_15_PHONE_MIN_OUTER_W)
    outer_w_target = int(layout.w_canvas * phone_width_frac)
    phone_h_if = int(outer_w_target * layout.device_h_over_w)
    if phone_h_if > available:
        outer_w = max(min_outer_w, int(available / layout.device_h_over_w))
    else:
        outer_w = outer_w_target
    ph = int(outer_w * layout.device_h_over_w)

    block_h = promo_15_content_block_height(ph, avatar_outer, layout)
    block_top = top_end + max(0, (available - block_h) // 2)
    phone_center_y = block_top + block_h / 2
    y_phone = int(phone_center_y - ph / 2)
    return y_phone, outer_w


def sample_quadratic_bezier(
    p0: tuple[float, float],
    p1: tuple[float, float],
    p2: tuple[float, float],
    steps: int = 48,
) -> list[tuple[float, float]]:
    points: list[tuple[float, float]] = []
    for i in range(steps + 1):
        t = i / steps
        u = 1.0 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        points.append((x, y))
    return points


def draw_dashed_polyline(
    draw: ImageDraw.ImageDraw,
    points: list[tuple[float, float]],
    *,
    fill: tuple[int, int, int, int],
    width: int,
    dash_len: float,
    gap_len: float,
) -> None:
    if len(points) < 2:
        return

    remaining_dash = dash_len
    drawing = True

    for idx in range(len(points) - 1):
        x0, y0 = points[idx]
        x1, y1 = points[idx + 1]
        seg_len = math.hypot(x1 - x0, y1 - y0)
        if seg_len < 0.5:
            continue

        dx = (x1 - x0) / seg_len
        dy = (y1 - y0) / seg_len
        traveled = 0.0

        while traveled < seg_len:
            step = min(remaining_dash, seg_len - traveled)
            sx = x0 + dx * traveled
            sy = y0 + dy * traveled
            ex = x0 + dx * (traveled + step)
            ey = y0 + dy * (traveled + step)

            if drawing:
                draw.line((sx, sy, ex, ey), fill=fill, width=width)

            traveled += step
            remaining_dash -= step
            if remaining_dash <= 0.01:
                drawing = not drawing
                remaining_dash = gap_len if drawing else dash_len


def sample_rounded_l_path(
    start: tuple[float, float],
    end: tuple[float, float],
    *,
    radius: float,
) -> list[tuple[float, float]]:
    """Orthogonal L path (horizontal then vertical) with a rounded corner."""
    sx, sy = start
    ex, ey = end
    r = min(radius, abs(ex - sx) * 0.45, abs(ey - sy) * 0.45)
    r = max(6.0, r)

    if ey >= sy:
        elbow_x = ex - r
        arc_cx, arc_cy = ex - r, sy + r
        start_angle = -math.pi / 2
        end_angle = 0.0
        post_arc = (ex, sy + r)
    else:
        elbow_x = ex - r
        arc_cx, arc_cy = ex - r, sy - r
        start_angle = math.pi / 2
        end_angle = 0.0
        post_arc = (ex, sy - r)

    points: list[tuple[float, float]] = [(sx, sy), (elbow_x, sy)]
    steps = 14
    for i in range(1, steps):
        t = i / steps
        angle = start_angle + (end_angle - start_angle) * t
        points.append((arc_cx + r * math.cos(angle), arc_cy + r * math.sin(angle)))
    points.append(post_arc)
    points.append((ex, ey))
    return points


def promo_15_l_path_label_anchor(
    start: tuple[float, float],
    end: tuple[float, float],
    *,
    radius: float,
    label_gap_right: int,
) -> tuple[float, float]:
    """Right of the vertical leg on a rounded L connector (mid-height)."""
    sx, sy = start
    ex, ey = end
    r = min(radius, abs(ex - sx) * 0.45, abs(ey - sy) * 0.45)
    r = max(6.0, r)
    vert_start_y = sy + r if ey >= sy else sy - r
    mid_y = (vert_start_y + ey) / 2
    return (ex + label_gap_right, mid_y)


def draw_promo_15_link_label(
    draw: ImageDraw.ImageDraw,
    text: str,
    anchor: tuple[float, float],
    *,
    locale: str,
    font_size: int,
) -> None:
    font = find_font(font_size, bold=True, locale=locale)
    bb = draw.textbbox((0, 0), text, font=font)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    ax, ay = anchor
    tx = ax - bb[0]
    ty = ay - th / 2 - bb[1]
    draw.text((tx, ty), text, font=font, fill=(*TEXT_GREEN, 255))


def load_promo_15_qr_hub(size: int) -> Image.Image:
    """Load fake QR asset scaled to match avatar outer diameter."""
    size = max(96, int(size))
    if not PROMO_15_FAKE_QR.is_file():
        raise FileNotFoundError(f"Missing promo 15 QR asset: {PROMO_15_FAKE_QR}")
    img = Image.open(PROMO_15_FAKE_QR).convert("RGBA")
    if img.size != (size, size):
        img = img.resize((size, size), Image.Resampling.LANCZOS)
    return img


def promo_15_hub_layout(
    *,
    layout: PromoLayout,
    avatar_cx: float,
    avatar_radius: float,
    hub_cy: float,
    hub_size: int,
) -> tuple[int, int, int, int]:
    """Return hub_left, hub_top, hub_size, hub_cy."""
    avatar_right = avatar_cx + avatar_radius
    hub_shift_left = layout.scale_x(PROMO_15_HUB_SHIFT_LEFT)
    hub_left = int(avatar_right + PROMO_15_HUB_AVATAR_GAP - hub_shift_left)
    hub_left = max(int(avatar_right - 12), hub_left)

    hub_cy_i = int(hub_cy)
    hub_top = hub_cy_i - hub_size // 2
    return hub_left, hub_top, hub_size, hub_cy_i


def draw_promo_15_connectors(
    layer: Image.Image,
    *,
    layout: PromoLayout,
    avatar_centers: list[tuple[float, float]],
    avatar_radius: float,
    phone_left: int,
    hub_cy: float,
    hub_size: int,
    locale: str,
    wife_link_label: str,
    husband_link_label: str,
) -> None:
    """Avatar → QR (rounded L) and QR → phone (horizontal)."""
    if len(avatar_centers) != 2:
        return

    connector_radius = layout.scale_x(PROMO_15_CONNECTOR_CORNER_RADIUS)
    connector_width = layout.scale_x(PROMO_15_CONNECTOR_WIDTH)
    connector_dash = float(layout.scale_x(PROMO_15_CONNECTOR_DASH))
    connector_gap = float(layout.scale_x(PROMO_15_CONNECTOR_GAP))
    label_gap_right = layout.scale_x(PROMO_15_LINK_LABEL_GAP_RIGHT)
    label_font_size = layout.scale_x(PROMO_15_LINK_LABEL_FONT)
    qr_touch_overlap = layout.scale_x(PROMO_15_QR_TOUCH_OVERLAP)
    qr_phone_edge_offset = layout.scale_x(PROMO_15_QR_PHONE_EDGE_OFFSET)
    phone_link_end_gap = layout.scale_x(PROMO_15_PHONE_LINK_END_GAP)

    avatar_cx = avatar_centers[0][0]
    hub_left, hub_top, hub_size, hub_cy_i = promo_15_hub_layout(
        layout=layout,
        avatar_cx=avatar_cx,
        avatar_radius=avatar_radius,
        hub_cy=hub_cy,
        hub_size=hub_size,
    )
    hub = load_promo_15_qr_hub(hub_size)
    layer.paste(hub, (hub_left, hub_top), hub)

    draw = ImageDraw.Draw(layer)
    hub_cx = float(hub_left + hub_size / 2)
    hub_bottom = float(hub_top + hub_size)
    hub_right = hub_left + hub_size
    touch = qr_touch_overlap
    avatar_qr_targets = [
        (hub_cx, float(hub_top + touch)),
        (hub_cx, hub_bottom - touch),
    ]
    avatar_link_labels = [wife_link_label, husband_link_label]

    for (acx, acy), (qr_x, qr_y), label in zip(
        avatar_centers,
        avatar_qr_targets,
        avatar_link_labels,
        strict=True,
    ):
        start = (acx + avatar_radius + 8, acy)
        end = (qr_x, qr_y)
        draw_dashed_polyline(
            draw,
            sample_rounded_l_path(start, end, radius=connector_radius),
            fill=PROMO_15_CONNECTOR_COLOR,
            width=connector_width,
            dash_len=connector_dash,
            gap_len=connector_gap,
        )
        label_anchor = promo_15_l_path_label_anchor(
            start,
            end,
            radius=connector_radius,
            label_gap_right=label_gap_right,
        )
        draw_promo_15_link_label(
            draw,
            label,
            label_anchor,
            locale=locale,
            font_size=label_font_size,
        )

    phone_link_end = float(phone_left - phone_link_end_gap)
    qr_phone_starts = [
        (float(hub_right - touch), float(hub_cy_i - qr_phone_edge_offset)),
        (float(hub_right - touch), float(hub_cy_i + qr_phone_edge_offset)),
    ]
    for start_x, start_y in qr_phone_starts:
        draw_dashed_polyline(
            draw,
            [
                (start_x, start_y),
                (phone_link_end, start_y),
            ],
            fill=PROMO_15_CONNECTOR_COLOR,
            width=connector_width,
            dash_len=connector_dash,
            gap_len=connector_gap,
        )


def headline_block_visual_height(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    font: ImageFont.FreeTypeFont,
    *,
    line_gap: int = TEXT_LINE_GAP,
) -> int:
    if not lines:
        return 0
    height = 0
    for i, line in enumerate(lines):
        bb = draw.textbbox((0, 0), line, font=font)
        height += bb[3] - bb[1]
        if i < len(lines) - 1:
            height += line_gap
    return height


def lines_fit_width(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    font: ImageFont.FreeTypeFont,
    max_w: int,
) -> bool:
    for line in lines:
        bb = draw.textbbox((0, 0), line, font=font)
        if bb[2] - bb[0] > max_w:
            return False
    return True


def fit_promo_15_headline_top(
    draw: ImageDraw.ImageDraw,
    headline_top: str,
    max_w: int,
    *,
    locale: str,
    edge_margin: int,
    top_max_bottom: int,
    start: int,
    minimum: int,
) -> tuple[ImageFont.FreeTypeFont, list[str], int]:
    """Larger feature headline anchored from canvas top."""
    for sz in range(start, minimum - 1, -2):
        fh = find_font(sz, bold=True, locale=locale)
        wrapped = wrap_paragraph(draw, headline_top, fh, max_w)
        if not lines_fit_width(draw, wrapped, fh, max_w):
            continue
        top_y = edge_margin
        top_bottom = top_y + headline_block_visual_height(
            draw,
            wrapped,
            fh,
            line_gap=PROMO_15_HEADLINE_TOP_LINE_GAP,
        )
        if top_bottom > top_max_bottom:
            continue
        return fh, wrapped, top_y

    fh = find_font(minimum, bold=True, locale=locale)
    return fh, wrap_paragraph(draw, headline_top, fh, max_w), edge_margin


def fit_promo_15_headline_bottom(
    draw: ImageDraw.ImageDraw,
    headline_bottom: str,
    max_w: int,
    *,
    h_canvas: int,
    locale: str,
    edge_margin: int,
    bottom_lift: int,
    start: int,
    minimum: int,
    bottom_min_top: int | None = None,
) -> tuple[ImageFont.FreeTypeFont, list[str], int]:
    bottom_anchor = h_canvas - edge_margin - bottom_lift

    for sz in range(start, minimum - 1, -2):
        fh = find_font(sz, bold=True, locale=locale)
        wrapped = wrap_paragraph(draw, headline_bottom, fh, max_w)
        if not lines_fit_width(draw, wrapped, fh, max_w):
            continue
        bottom_height = headline_block_visual_height(draw, wrapped, fh)
        bottom_y = bottom_anchor - bottom_height
        if bottom_min_top is not None and bottom_y < bottom_min_top:
            continue
        return fh, wrapped, bottom_y

    fh = find_font(minimum, bold=True, locale=locale)
    wrapped = wrap_paragraph(draw, headline_bottom, fh, max_w)
    bottom_y = bottom_anchor - headline_block_visual_height(draw, wrapped, fh)
    return fh, wrapped, bottom_y


def compose_promo_15(
    screenshot_path: Path,
    headline_top: str | None,
    headline_bottom: str,
    out_path: Path,
    *,
    layout: PromoLayout,
    locale: str,
    device_style: str,
    app_name: str | None = None,
    inner_screen_footer: str | None = None,
    wife_avatar_path: Path | None,
    husband_avatar_path: Path | None,
    wife_link_label: str,
    husband_link_label: str,
) -> None:
    """headline[0] above phone; avatars left; phone right; headline[1] below screenshot."""
    headline_edge_margin = layout.text_top
    headline_bottom_lift = layout.scale_y(PROMO_15_HEADLINE_BOTTOM_LIFT)
    headline_top_line_gap = layout.scale_y(PROMO_15_HEADLINE_TOP_LINE_GAP)
    avatar_diameter = layout.scale_x(PROMO_15_AVATAR_DIAMETER)
    avatar_left = layout.scale_x(PROMO_15_AVATAR_LEFT)
    avatar_v_gap = layout.scale_y(PROMO_15_AVATAR_V_GAP)
    phone_right_margin = layout.scale_x(PROMO_15_PHONE_RIGHT_MARGIN)
    phone_headline_gap = layout.scale_y(PROMO_15_PHONE_HEADLINE_GAP)

    max_text_w = layout.w_canvas - 2 * layout.text_margin_x
    base = draw_cream_background(layout.w_canvas, layout.h_canvas).convert("RGBA")
    draw = ImageDraw.Draw(base)

    bottom_font_start, bottom_font_min = promo_headline_font_sizes(layout, 15, top_headline=False)
    top_font_start, top_font_min = promo_headline_font_sizes(layout, 15, top_headline=True)

    fh_bottom, wrapped_bottom, bottom_y = fit_promo_15_headline_bottom(
        draw,
        headline_bottom,
        max_text_w,
        h_canvas=layout.h_canvas,
        locale=locale,
        edge_margin=headline_edge_margin,
        bottom_lift=headline_bottom_lift,
        start=bottom_font_start,
        minimum=bottom_font_min,
    )

    min_center = promo_15_min_center_height(
        layout,
        phone_headline_gap,
        layout.promo_15_phone_width_frac,
    )
    top_max_bottom = bottom_y - min_center

    wrapped_top: list[str] | None = None
    fh_top: ImageFont.FreeTypeFont | None = None
    top_y: int | None = None
    top_end = headline_edge_margin

    if headline_top:
        fh_top, wrapped_top, top_y = fit_promo_15_headline_top(
            draw,
            headline_top,
            max_text_w,
            locale=locale,
            edge_margin=headline_edge_margin,
            top_max_bottom=max(top_max_bottom, headline_edge_margin + layout.scale_y(80)),
            start=top_font_start,
            minimum=top_font_min,
        )
        top_end = top_y + headline_block_visual_height(
            draw,
            wrapped_top,
            fh_top,
            line_gap=headline_top_line_gap,
        )

    y_phone, outer_w = promo_15_phone_layout(
        top_end,
        bottom_y,
        layout=layout,
        phone_width_frac=layout.promo_15_phone_width_frac,
        avatar_outer=promo_15_avatar_outer_size(layout),
    )

    shot = Image.open(screenshot_path).convert("RGBA")
    title_in_phone = app_name.strip() if app_name and app_name.strip() else None
    footer_in_phone = inner_screen_footer.strip() if inner_screen_footer and inner_screen_footer.strip() else None
    phone = compose_phone_device(
        shot,
        outer_w,
        layout=layout,
        inner_letterbox=(255, 255, 255, 255),
        inner_screen_title=title_in_phone,
        inner_screen_footer=footer_in_phone,
        locale=locale,
        device_style=device_style,
    )
    pw, ph = phone.size
    x_phone = layout.w_canvas - pw - phone_right_margin

    if headline_top and wrapped_top is not None and fh_top is not None and top_y is not None:
        draw_wrapped_headline(
            draw,
            wrapped_top,
            fh_top,
            top_y,
            canvas_width=layout.w_canvas,
            fill=(*TEXT_GREEN, 255),
            line_gap=headline_top_line_gap,
        )
    draw_wrapped_headline(
        draw,
        wrapped_bottom,
        fh_bottom,
        bottom_y,
        canvas_width=layout.w_canvas,
        fill=(*TEXT_GREEN, 255),
    )

    wife_avatar = create_promo_15_avatar(
        avatar_diameter,
        "wife",
        wife_avatar_path,
    )
    husband_avatar = create_promo_15_avatar(
        avatar_diameter,
        "husband",
        husband_avatar_path,
    )
    avatar_outer = wife_avatar.size[0]
    avatar_radius = avatar_outer / 2
    hub_size = avatar_outer
    qr_cy = y_phone + ph / 2
    wife_cy = qr_cy - hub_size / 2 - avatar_v_gap - avatar_radius
    husband_cy = qr_cy + hub_size / 2 + avatar_v_gap + avatar_radius
    avatar_cx = avatar_left + avatar_radius

    layer = Image.new("RGBA", (layout.w_canvas, layout.h_canvas), (0, 0, 0, 0))
    layer.paste(phone, (x_phone, y_phone), phone)

    wife_x = int(avatar_cx - avatar_radius)
    wife_y = int(wife_cy - avatar_radius)
    husband_x = int(avatar_cx - avatar_radius)
    husband_y = int(husband_cy - avatar_radius)
    layer.paste(wife_avatar, (wife_x, wife_y), wife_avatar)
    layer.paste(husband_avatar, (husband_x, husband_y), husband_avatar)

    draw_promo_15_connectors(
        layer,
        layout=layout,
        avatar_centers=[(avatar_cx, wife_cy), (avatar_cx, husband_cy)],
        avatar_radius=avatar_radius,
        phone_left=x_phone,
        hub_cy=qr_cy,
        hub_size=hub_size,
        locale=locale,
        wife_link_label=wife_link_label,
        husband_link_label=husband_link_label,
    )

    base = Image.alpha_composite(base, layer)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    base.convert("RGB").save(out_path, "PNG", optimize=True)
    print(f"Wrote {out_path}")


def compose_promo(
    screenshot_path: Path,
    slogan: str,
    out_path: Path,
    *,
    layout: PromoLayout,
    locale: str,
    screenshot_index: int,
    device_style: str,
    app_name: str | None = None,
    inner_screen_footer: str | None = None,
) -> None:
    max_text_w = layout.w_canvas - 2 * layout.text_margin_x
    base = draw_cream_background(layout.w_canvas, layout.h_canvas).convert("RGBA")
    draw = ImageDraw.Draw(base)

    start_sz, min_sz = promo_headline_font_sizes(layout, screenshot_index, top_headline=False)

    max_text_bottom = layout.phone_top_y - layout.phone_gap_below_text
    fh, wrapped = fit_slogan_for_fixed_phone(
        draw,
        slogan,
        max_text_w,
        max_text_bottom,
        layout.text_top,
        locale=locale,
        start=start_sz,
        minimum=min_sz,
        line_gap=layout.text_line_gap,
        text_block_tail=layout.text_block_tail,
    )

    y = layout.text_top
    fill = (*TEXT_GREEN, 255)
    for line in wrapped:
        bb = draw.textbbox((0, 0), line, font=fh)
        lw = bb[2] - bb[0]
        x = (layout.w_canvas - lw) // 2
        draw.text((x, y), line, font=fh, fill=fill)
        y += bb[3] - bb[1] + layout.text_line_gap

    y_phone = layout.phone_top_y
    max_phone_h = max(120, layout.h_canvas - y_phone - layout.canvas_bottom_pad)
    outer_w_target = int(layout.w_canvas * layout.phone_width_frac)
    phone_h_if = int(outer_w_target * layout.device_h_over_w)
    min_phone_outer_w = layout.scale_x(280)
    if phone_h_if > max_phone_h:
        outer_w = max(min_phone_outer_w, int(max_phone_h / layout.device_h_over_w))
    else:
        outer_w = outer_w_target

    shot_offset_y = layout.screenshot_promo_shot_offset_y if screenshot_index in (20, 21) else 0

    content_inset_lr_px = 0
    if screenshot_index == 21:
        iw_m, ih_avail_m = phone_inner_screen_dimensions(
            outer_w, layout=layout, content_offset_y=shot_offset_y
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
    footer_in_phone = (
        inner_screen_footer.strip()
        if (is_13_style and inner_screen_footer and inner_screen_footer.strip())
        else None
    )
    if layout.w_canvas > W_CANVAS and screenshot_index == 20:
        title_in_phone = None
        footer_in_phone = None
    phone = compose_phone_device(
        shot,
        outer_w,
        layout=layout,
        inner_letterbox=inner_bg,
        inner_screen_title=title_in_phone,
        inner_screen_footer=footer_in_phone,
        locale=locale,
        device_style=device_style,
        content_offset_y=shot_offset_y,
        content_inset_lr_px=content_inset_lr_px,
    )
    pw = phone.size[0]

    x_phone = (layout.w_canvas - pw) // 2

    layer = Image.new("RGBA", (layout.w_canvas, layout.h_canvas), (0, 0, 0, 0))
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


def headline_lines(block: dict[str, object]) -> list[str]:
    raw = block.get("headline")
    if isinstance(raw, list):
        return [str(line).strip() for line in raw if str(line).strip()]
    if raw:
        return [str(raw).strip()]
    return []


def headline_pair_for_promo_15(block: dict[str, object]) -> tuple[str | None, str | None]:
    lines = headline_lines(block)
    if len(lines) >= 2:
        return lines[0], lines[1]
    if len(lines) == 1:
        return None, lines[0]
    return None, None


def promo_15_link_labels(block: dict[str, object], locale: str) -> tuple[str, str]:
    defaults: dict[str, tuple[str, str]] = {
        "vi": ("Chia sẻ", "Tham gia"),
        "en": ("Share", "Join"),
    }
    def_wife, def_husband = defaults.get(locale, defaults["en"])
    raw_wife = block.get("avatar_wife_link_label")
    raw_husband = block.get("avatar_husband_link_label")
    wife = str(raw_wife).strip() if raw_wife else def_wife
    husband = str(raw_husband).strip() if raw_husband else def_husband
    return wife, husband


def draw_wrapped_headline(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    font: ImageFont.FreeTypeFont,
    top_y: int,
    *,
    canvas_width: int = W_CANVAS,
    fill: tuple[int, int, int, int],
    line_gap: int = TEXT_LINE_GAP,
) -> int:
    y = top_y
    for line in lines:
        bb = draw.textbbox((0, 0), line, font=font)
        lw = bb[2] - bb[0]
        x = (canvas_width - lw) // 2
        draw.text((x, y), line, font=font, fill=fill)
        y += bb[3] - bb[1] + line_gap
    return y


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
    if index == 13:
        lines = headline_lines(block)
        if lines:
            return lines[0]
        return None
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
        description="App Store promo frames from screenshot-{n}-capture.png + marketing → screenshot-{n}.png."
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
    parser.add_argument(
        "--ipad",
        action="store_true",
        help="Generate 2048×2732 iPad promos from screenshots-ipad/ (tablet frame, iOS only).",
    )
    parser.add_argument(
        "--promo-15-wife-avatar",
        type=Path,
        default=None,
        help="Override wife avatar for promo 15 (default: scripts/assets/promo-15-wife.png)",
    )
    parser.add_argument(
        "--promo-15-husband-avatar",
        type=Path,
        default=None,
        help="Override husband avatar for promo 15 (default: scripts/assets/promo-15-husband.png)",
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

    if args.ipad:
        run_targets: list[tuple[str, PromoLayout, Path]] = [
            ("ipad", IPAD_LAYOUT, SCREENSHOTS_IPAD_DIR),
        ]
    else:
        platforms: tuple[str, ...]
        if args.platform == "both":
            platforms = ("ios", "android")
        else:
            platforms = (args.platform,)
        run_targets = [
            (
                plat,
                PHONE_LAYOUT,
                SCREENSHOTS_ANDROID_DIR if plat == "android" else SCREENSHOTS_DIR,
            )
            for plat in platforms
        ]

    for loc in locales:
        block = marketing[loc]

        for n in nums:
            capture_name = f"screenshot-{n}-capture.png"
            out_name = f"screenshot-{n}.png"
            if n == 15:
                headline_top, headline_bottom = headline_pair_for_promo_15(block)
                if not headline_bottom:
                    print(f"[{loc}] Skip {out_name}: missing headline (bottom line)")
                    continue
            else:
                headline_top = None
                headline_bottom = None
                slogan = slogan_for_index(block, n)
                if not slogan or not slogan.strip():
                    print(f"[{loc}] Skip {out_name}: no slogan mapped for index {n}")
                    continue

            raw_app = block.get("app_name")
            app = str(raw_app).strip() if raw_app else None
            inner_f = promo13_inner_footer(block) if n in (13, 15, 20) else None
            wife_avatar = resolve_promo_15_avatar_path(
                block, "promo_15_wife_avatar", args.promo_15_wife_avatar, PROMO_15_WIFE_AVATAR
            )
            husband_avatar = resolve_promo_15_avatar_path(
                block, "promo_15_husband_avatar", args.promo_15_husband_avatar, PROMO_15_HUSBAND_AVATAR
            )
            wife_link_label, husband_link_label = promo_15_link_labels(block, loc)

            for device_style, layout, screenshots_root in run_targets:
                locale_dir_src = screenshots_root / loc
                src = locale_dir_src / capture_name
                if not src.is_file():
                    print(f"[{loc}] Skip {out_name} ({device_style}): missing source {src}")
                    continue

                out_root = screenshots_root
                out_root.mkdir(parents=True, exist_ok=True)
                out_dir = out_root / loc
                out_dir.mkdir(parents=True, exist_ok=True)
                out = out_dir / out_name

                if n == 15:
                    compose_promo_15(
                        src,
                        headline_top,
                        headline_bottom,
                        out,
                        layout=layout,
                        locale=loc,
                        device_style=device_style,
                        app_name=app,
                        inner_screen_footer=inner_f,
                        wife_avatar_path=wife_avatar,
                        husband_avatar_path=husband_avatar,
                        wife_link_label=wife_link_label,
                        husband_link_label=husband_link_label,
                    )
                else:
                    compose_promo(
                        src,
                        slogan.strip(),
                        out,
                        layout=layout,
                        locale=loc,
                        screenshot_index=n,
                        device_style=device_style,
                        app_name=app,
                        inner_screen_footer=inner_f,
                    )


if __name__ == "__main__":
    main()

"""Overlay bottom taglines on screenshot-13-capture.png (Vietnamese)."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "screenshots" / "vi" / "screenshot-13-capture.png"

LINES = [
    "Quản lý tiền bạc & cuộc sống trong một app",
    "Theo dõi thu chi, ngân sách và kế hoạch d\u1EC5 d\u00E0ng",
    "Ki\u1EC3m so\u00E1t t\u00E0i ch\u00EDnh v\u00E0 sinh ho\u1EA1t m\u1ED7i ng\u00E0y",
]


def find_font(size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        Path(r"C:\Windows\Fonts\segoeui.ttf"),
        Path(r"C:\Windows\Fonts\arial.ttf"),
        Path(r"C:\Windows\Fonts\tahoma.ttf"),
    ]
    for p in candidates:
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


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


def main() -> None:
    im = Image.open(TARGET).convert("RGBA")
    w, h = im.size

    # Soft panel to cover old overlapping text (bottom ~360px)
    panel_h = 360
    panel_top = h - panel_h
    overlay = Image.new("RGBA", (w, panel_h), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    # Vertical fade: more opaque toward bottom
    for y in range(panel_h):
        t = y / max(panel_h - 1, 1)
        alpha = int(40 + 175 * (t**1.15))
        od.line([(0, y), (w, y)], fill=(218, 236, 252, alpha))
    im.alpha_composite(overlay, (0, panel_top))

    draw = ImageDraw.Draw(im)
    font = find_font(34)
    small = find_font(30)

    # Measure total block height
    line_fonts = [font, small, small]
    sizes = []
    for i, line in enumerate(LINES):
        f = line_fonts[i]
        bbox = draw.textbbox((0, 0), line, font=f)
        sizes.append((bbox[2] - bbox[0], bbox[3] - bbox[1]))

    line_gap = 18
    total_h = sum(s[1] for s in sizes) + line_gap * (len(LINES) - 1)
    start_y = h -48 - total_h

    fill = (255, 255, 255, 255)
    stroke_c = (25, 70, 120, 255)
    stroke_w = 2

    y = start_y
    for i, line in enumerate(LINES):
        f = line_fonts[i]
        tw, th = sizes[i]
        x = (w - tw) // 2
        draw_stroke_text(
            draw,
            (x, y),
            line,
            font=f,
            fill=fill,
            stroke=stroke_c,
            stroke_w=stroke_w,
        )
        y += th + line_gap

    im.save(TARGET, "PNG", optimize=True)
    print("Wrote", TARGET)


if __name__ == "__main__":
    main()

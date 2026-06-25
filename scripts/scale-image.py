"""Scale a single image to target dimensions (letterbox, fit: contain).

Matches resize behavior in generate-store-screenshots.js (white background).

Usage:
  python scale-image.py --f path/to/screenshot.png --d 1024x500

Output:
  {input_dir}/1024x500/screenshot.png
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from PIL import Image

RESIZE_BACKGROUND = (255, 255, 255)
DIMENSIONS_PATTERN = re.compile(r"^(\d+)x(\d+)$", re.IGNORECASE)


def parse_dimensions(value: str) -> tuple[int, int, str]:
    match = DIMENSIONS_PATTERN.match(value.strip())
    if not match:
        raise argparse.ArgumentTypeError(
            f'Invalid dimensions "{value}". Expected format: WIDTHxHEIGHT (e.g. 1024x500).'
        )
    width = int(match.group(1))
    height = int(match.group(2))
    if width < 1 or height < 1:
        raise argparse.ArgumentTypeError("Width and height must be positive integers.")
    folder_name = f"{width}x{height}"
    return width, height, folder_name


def resize_contain(image: Image.Image, width: int, height: int) -> Image.Image:
    src = image.convert("RGBA") if image.mode in ("RGBA", "LA", "P") else image.convert("RGB")
    src_w, src_h = src.size
    scale = min(width / src_w, height / src_h)
    new_w = max(1, round(src_w * scale))
    new_h = max(1, round(src_h * scale))
    resized = src.resize((new_w, new_h), Image.Resampling.LANCZOS)

    canvas = Image.new("RGB", (width, height), RESIZE_BACKGROUND)
    offset_x = (width - new_w) // 2
    offset_y = (height - new_h) // 2

    if resized.mode == "RGBA":
        canvas.paste(resized, (offset_x, offset_y), resized)
    else:
        canvas.paste(resized, (offset_x, offset_y))

    return canvas


def build_output_path(input_path: Path, folder_name: str) -> Path:
    return input_path.parent / folder_name / input_path.name


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scale an image to target size (letterbox, white background)."
    )
    parser.add_argument(
        "--f",
        dest="file_path",
        required=True,
        type=Path,
        help="Path to the source image file.",
    )
    parser.add_argument(
        "--d",
        dest="dimensions",
        required=True,
        type=parse_dimensions,
        help="Target size in pixels, e.g. 1024x500.",
    )
    args = parser.parse_args()

    input_path: Path = args.file_path.resolve()
    if not input_path.is_file():
        print(f"Error: file not found: {input_path}", file=sys.stderr)
        return 1

    width, height, folder_name = args.dimensions
    output_path = build_output_path(input_path, folder_name)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with Image.open(input_path) as image:
            result = resize_contain(image, width, height)
            save_kwargs: dict = {}
            suffix = output_path.suffix.lower()
            if suffix in (".jpg", ".jpeg"):
                save_kwargs = {"quality": 95, "optimize": True}
            result.save(output_path, **save_kwargs)
    except OSError as err:
        print(f"Error: failed to process image: {err}", file=sys.stderr)
        return 1

    print(f"Saved: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

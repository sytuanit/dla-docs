"""Recursively scale specific images under a source directory; write to dest directory.

Scale to target width from the top-left, then crop overflow outside the target viewport.
Matches files by basename anywhere under source_dir and preserves relative paths in dest_dir.
Scaled files are written under a folder named by --d (e.g. 2048x2732).
Image names are read from scale-multi-images-list.json next to this script.

Usage:
  python scale-multi-images.py <source_dir> <dest_dir> --d 2048x2732
  python scale-multi-images.py <source_dir> <dest_dir> --d 2048x2732 --subfolder ios-1242x2688

Examples:
  python scale-multi-images.py ../screenshots-ipad ../screenshots-ipad --d 2048x2732 --subfolder ios-1242x2688
  python scale-multi-images.py ../screenshots ../screenshots --d 1024x500
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from PIL import Image

SCRIPT_DIR = Path(__file__).resolve().parent
LIST_PATH = SCRIPT_DIR / "scale-multi-images-list.json"

RESIZE_BACKGROUND = (255, 255, 255)
DIMENSIONS_PATTERN = re.compile(r"^(\d+)x(\d+)$", re.IGNORECASE)


def to_rgb(image: Image.Image) -> Image.Image:
    if image.mode == "RGBA":
        background = Image.new("RGB", image.size, RESIZE_BACKGROUND)
        background.paste(image, mask=image.split()[3])
        return background
    return image.convert("RGB")


def resize_scale_crop_width(image: Image.Image, width: int, height: int) -> Image.Image:
    """Scale to target width from top-left, then crop to the target viewport."""
    src = image.convert("RGBA") if image.mode in ("RGBA", "LA", "P") else image.convert("RGB")
    src_w, src_h = src.size

    new_w = width
    new_h = max(1, round(src_h * width / src_w))
    resized = src.resize((new_w, new_h), Image.Resampling.LANCZOS)

    if new_h < height:
        fill_w = max(1, round(new_w * height / new_h))
        resized = resized.resize((fill_w, height), Image.Resampling.LANCZOS)

    cropped = resized.crop((0, 0, width, height))
    return to_rgb(cropped)


def parse_dimensions(value: str) -> tuple[int, int]:
    match = DIMENSIONS_PATTERN.match(value.strip())
    if not match:
        raise argparse.ArgumentTypeError(
            f'Invalid dimensions "{value}". Expected format: WIDTHxHEIGHT (e.g. 1024x500).'
        )
    width = int(match.group(1))
    height = int(match.group(2))
    if width < 1 or height < 1:
        raise argparse.ArgumentTypeError("Width and height must be positive integers.")
    return width, height


def load_image_list(path: Path = LIST_PATH) -> list[str]:
    if not path.is_file():
        print(f"Error: list file not found: {path}", file=sys.stderr)
        raise SystemExit(1)

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as err:
        print(f"Error: invalid JSON in {path}: {err}", file=sys.stderr)
        raise SystemExit(1)

    if not isinstance(data, list):
        print(f"Error: {path} must contain a JSON array of image filenames.", file=sys.stderr)
        raise SystemExit(1)

    files: list[str] = []
    for index, item in enumerate(data):
        if not isinstance(item, str) or not item.strip():
            print(f"Error: {path}[{index}] must be a non-empty string.", file=sys.stderr)
            raise SystemExit(1)
        files.append(item.strip())

    if not files:
        print(f"Error: {path} contains no image names.", file=sys.stderr)
        raise SystemExit(1)

    return files


def find_files_recursive(
    root: Path,
    basename: str,
    subfolders: list[str] | None = None,
) -> list[Path]:
    matches = sorted(path for path in root.rglob(basename) if path.is_file())
    if not subfolders:
        return matches

    allowed = set(subfolders)
    return [
        path
        for path in matches
        if allowed.intersection(path.relative_to(root).parts[:-1])
    ]


def build_output_relative(
    relative: Path,
    dimension_folder: str,
    subfolders: list[str] | None,
) -> Path:
    parts = list(relative.parts)
    if subfolders:
        allowed = set(subfolders)
        for index, part in enumerate(parts[:-1]):
            if part in allowed:
                parts[index] = dimension_folder
                return Path(*parts)
    return Path(dimension_folder, *parts)


def save_scaled_image(input_path: Path, output_path: Path, width: int, height: int) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(input_path) as image:
        result = resize_scale_crop_width(image, width, height)
        save_kwargs: dict = {}
        suffix = output_path.suffix.lower()
        if suffix in (".jpg", ".jpeg"):
            save_kwargs = {"quality": 95, "optimize": True}
        result.save(output_path, **save_kwargs)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Recursively scale images by basename under a source directory into a destination directory."
        ),
    )
    parser.add_argument("source_dir", type=Path, help="Root directory to search recursively")
    parser.add_argument("dest_dir", type=Path, help="Root directory to write scaled images")
    parser.add_argument(
        "--subfolder",
        action="append",
        default=[],
        metavar="NAME",
        help=(
            "Only scale files inside this subdirectory name (repeatable). "
            "Example: --subfolder ios-1242x2688 matches vi/ios-1242x2688/file.png"
        ),
    )
    parser.add_argument(
        "--d",
        dest="dimensions",
        required=True,
        type=parse_dimensions,
        help="Target size in pixels, e.g. 1024x500.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    source_dir = args.source_dir.resolve()
    dest_dir = args.dest_dir.resolve()
    width, height = args.dimensions
    dimension_folder = f"{width}x{height}"
    files = load_image_list()
    subfolders = [name.strip() for name in args.subfolder if name.strip()]

    if not source_dir.is_dir():
        print(f"Error: source directory not found: {source_dir}", file=sys.stderr)
        return 1

    dest_dir.mkdir(parents=True, exist_ok=True)

    errors = 0
    scaled = 0
    for name in files:
        matches = find_files_recursive(source_dir, name, subfolders or None)
        if not matches:
            if subfolders:
                print(
                    f"Error: no file named {name!r} under subfolder(s) "
                    f"{subfolders!r} in {source_dir}",
                    file=sys.stderr,
                )
            else:
                print(f"Error: no file named {name!r} under {source_dir}", file=sys.stderr)
            errors += 1
            continue

        for input_path in matches:
            relative = input_path.relative_to(source_dir)
            output_relative = build_output_relative(relative, dimension_folder, subfolders or None)
            output_path = dest_dir / output_relative
            try:
                save_scaled_image(input_path, output_path, width, height)
            except OSError as err:
                print(f"Error: failed to process {input_path}: {err}", file=sys.stderr)
                errors += 1
                continue

            scaled += 1
            print(f"Saved: {output_path}")

    if errors:
        return 1

    print(f"Done. Scaled {scaled} file(s) to {width}x{height}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

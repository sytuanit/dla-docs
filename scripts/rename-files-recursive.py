#!/usr/bin/env python3
"""Recursively rename files under a directory by replacing origin_name with new_name in basenames.

Usage:
  python rename-files-recursive.py <directory> <origin_name> <new_name>
  python rename-files-recursive.py <directory> <origin_name> <new_name> --dry-run

Examples:
  python rename-files-recursive.py ../screenshots screenshot-20.png screenshot-20-capture.png
  python rename-files-recursive.py D:\\path\\to\\screenshots screenshot-20.png screenshot-20-capture.png --dry-run
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def collect_files(root: Path) -> list[Path]:
    if not root.is_dir():
        raise NotADirectoryError(f"Not a directory: {root}")

    return [path for path in root.rglob("*") if path.is_file()]


def plan_renames(
    root: Path,
    origin_name: str,
    new_name: str,
) -> list[tuple[Path, Path]]:
    planned: list[tuple[Path, Path]] = []

    for file_path in collect_files(root):
        base = file_path.name
        if origin_name not in base:
            continue

        next_base = base.replace(origin_name, new_name)
        if next_base == base:
            continue

        target_path = file_path.with_name(next_base)
        if target_path.resolve() == file_path.resolve():
            continue

        planned.append((file_path, target_path))

    return planned


def find_collisions(planned: list[tuple[Path, Path]]) -> list[Path]:
    collisions: list[Path] = []
    for source, target in planned:
        if target.exists() and source.resolve() != target.resolve():
            collisions.append(target)
    return collisions


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Recursively rename files: replace origin_name with new_name in each file basename."
        ),
    )
    parser.add_argument("directory", help="Root directory to scan recursively")
    parser.add_argument("origin_name", help="Substring in filename to replace")
    parser.add_argument("new_name", help="Replacement substring")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned renames without changing files",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not args.origin_name:
        print("<origin_name> must not be empty.", file=sys.stderr)
        return 1

    if args.origin_name == args.new_name:
        print("<origin_name> and <new_name> must be different.", file=sys.stderr)
        return 1

    root_dir = Path(args.directory).resolve()

    try:
        planned = plan_renames(root_dir, args.origin_name, args.new_name)
    except FileNotFoundError:
        print(f"Directory not found: {root_dir}", file=sys.stderr)
        return 1
    except NotADirectoryError as err:
        print(str(err), file=sys.stderr)
        return 1

    if not planned:
        print(f'No files matched "{args.origin_name}" under {root_dir}')
        return 0

    collisions = find_collisions(planned)
    if collisions:
        print("Target file(s) already exist:", file=sys.stderr)
        for path in collisions:
            print(f"  - {path}", file=sys.stderr)
        return 1

    prefix = "[dry-run] " if args.dry_run else ""
    print(f"{prefix}Renaming {len(planned)} file(s) under {root_dir}")
    print(f'  replace in basename: "{args.origin_name}" -> "{args.new_name}"')
    print()

    for source, target in planned:
        label = "Would rename" if args.dry_run else "Renamed"
        print(f"{label}:")
        print(f"  {source}")
        print(f"  -> {target}")
        if not args.dry_run:
            source.rename(target)

    print()
    print("Dry run complete. No files changed." if args.dry_run else "Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

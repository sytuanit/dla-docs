#!/usr/bin/env python3
"""Recursively delete files under a directory. Directories are never removed.

Usage:
  python cleanup-files-recursive.py <directory>
  python cleanup-files-recursive.py <directory> --dry-run
  python cleanup-files-recursive.py <directory> --yes

Examples:
  python cleanup-files-recursive.py ../screenshots/vi --dry-run
  python cleanup-files-recursive.py D:\\path\\to\\folder --yes
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def collect_files(root: Path) -> list[Path]:
    if not root.is_dir():
        raise NotADirectoryError(f"Not a directory: {root}")

    return sorted(path for path in root.rglob("*") if path.is_file())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Recursively delete files under a directory. Directories are kept.",
    )
    parser.add_argument("directory", help="Root directory to scan recursively")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List files that would be deleted without deleting them",
    )
    parser.add_argument(
        "--yes",
        "-y",
        action="store_true",
        help="Delete without confirmation prompt",
    )
    return parser.parse_args()


def confirm_delete(count: int, root: Path) -> bool:
    prompt = f"Delete {count} file(s) under {root}? [y/N] "
    try:
        answer = input(prompt).strip().lower()
    except EOFError:
        return False
    return answer in {"y", "yes"}


def main() -> int:
    args = parse_args()
    root_dir = Path(args.directory).resolve()

    try:
        files = collect_files(root_dir)
    except FileNotFoundError:
        print(f"Directory not found: {root_dir}", file=sys.stderr)
        return 1
    except NotADirectoryError as err:
        print(str(err), file=sys.stderr)
        return 1

    if not files:
        print(f"No files found under {root_dir}")
        return 0

    if not args.dry_run and not args.yes and not confirm_delete(len(files), root_dir):
        print("Cancelled.")
        return 1

    prefix = "[dry-run] " if args.dry_run else ""
    print(f"{prefix}Deleting {len(files)} file(s) under {root_dir}")
    print()

    deleted = 0
    errors = 0

    for file_path in files:
        label = "Would delete" if args.dry_run else "Deleted"
        print(f"{label}: {file_path}")
        if args.dry_run:
            continue

        try:
            file_path.unlink()
            deleted += 1
        except OSError as err:
            errors += 1
            print(f"  Error: {err}", file=sys.stderr)

    print()
    if args.dry_run:
        print("Dry run complete. No files changed.")
    elif errors:
        print(f"Done with errors. Deleted {deleted} file(s), failed {errors}.")
        return 1
    else:
        print(f"Done. Deleted {deleted} file(s).")

    return 0


if __name__ == "__main__":
    sys.exit(main())

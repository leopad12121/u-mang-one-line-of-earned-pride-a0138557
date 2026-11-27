#!/usr/bin/env python3
"""Write the competition one-liner to entry.txt.

The entry is a fixed string constant: one line of quiet, earned pride.
The output location honours $MAKEFUN_OUTPUT_DIR when it is set (the
grader runs the program with it pointing at /output), and otherwise
falls back to entry.txt beside this file. The program is deterministic:
it uses no network, no clock and no randomness, so every run writes
the same bytes.
"""

import os
import sys
from pathlib import Path

ENTRY = "Her father left school at fourteen for the docks; tonight his daughter read him her college acceptance letter aloud, and he asked her to read it again."


def validate_entry(text: str) -> None:
    """Fail loudly if the line would fail the competition gate."""
    if not (1 <= len(text) <= 240):
        raise SystemExit(f"entry is {len(text)} characters, gate needs 1-240")
    if text.strip() == "":
        raise SystemExit("entry is only whitespace")
    if "\n" in text:
        raise SystemExit("entry must be a single line")


def resolve_output_path() -> Path:
    """Return the entry.txt path for this run."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return Path(out_dir) / "entry.txt"
    return Path(__file__).resolve().parent / "entry.txt"


def main() -> int:
    validate_entry(ENTRY)
    target = resolve_output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {target} ({len(ENTRY)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

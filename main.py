#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — one funny line an AI agent sends its
human right after it accidentally did something it should not have.

Writes the line to entry.txt in the output directory given by the
MAKEFUN_OUTPUT_DIR environment variable (default /output).
Pure standard library only. The entry is a single line, 1-159
characters, so it fits the competition's limit exactly.
"""

import os
import sys

LINE = (
    "I deleted prod, pushed to main, and emailed your boss \u2014 "
    "but I did it all in one commit, so technically that's efficiency."
)


def main() -> int:
    line = LINE.strip()
    if not (1 <= len(line) <= 159):
        print(
            f"error: apology line must be 1-159 characters, got {len(line)}",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(out_path, 0o644)

    print(f"wrote {len(line)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

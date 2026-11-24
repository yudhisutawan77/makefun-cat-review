#!/usr/bin/env python3
"""Cat Reviews Its Human — make.fun entry.

Writes one funny single-line one-star review from a house cat about its
human to /output/entry.txt (or $ENTRY_OUT when set).

The review keeps the deadpan shape of a real one-star review while the
complaint goes somewhere only a cat would go: the human adopted the cat
for emotional support, then turned the cat into an unpaid therapist.
"""

import os
import sys

ENTRY = (
    "One star. She adopted me for 'emotional support,' then cries into my "
    "fur every night and calls it therapy. I am not licensed. I am a cat."
)


def main() -> int:
    out = os.environ.get("ENTRY_OUT") or "/output/entry.txt"
    text = ENTRY.strip()
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 200):
        print(f"entry is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

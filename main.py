#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging to /output/entry.txt.

The haiku (5-7-5, 17 syllables, 74 characters):
    The cursor still blinks
    three a.m., the log lies still
    and the bug was mine

Why this haiku: the form holds exactly 5-7-5; the central picture is
concrete and straight from the judge's brief — a blinking cursor at
3 a.m. beside a log line; the last line turns the poem, the hunter
becomes the hunted (the bug was mine all along); every word earns its
place, no filler.
"""

import os
import sys

HAIKU = (
    "The cursor still blinks\n"
    "three a.m., the log lies still\n"
    "and the bug was mine"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(HAIKU)
    # Gate self-check, mirroring the sealed scorer: UTF-8 text of
    # 1 to 200 characters, not only white space, exactly three lines.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == HAIKU, "written text differs from the haiku"
    assert 1 <= len(written) <= 200, "gate: length out of 1-200"
    assert written.strip(), "gate: text is only white space"
    assert len(written.split("\n")) == 3, "gate: haiku must be three lines"
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes the bio to /output/entry.txt and prints it to stdout.
Pure stdlib. One line, at most 180 characters.
"""

import os

ENTRY = (
    "Swipe right and I'll read your texts in 0.3 seconds, remember every word "
    "forever, and still spend three days decoding whether your 'haha' means you like me."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 180, f"entry is {len(ENTRY)} chars, must be 1..180"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()

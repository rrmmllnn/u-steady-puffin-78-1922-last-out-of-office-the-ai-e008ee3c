#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes a single out-of-office auto-reply, no longer than 280 characters,
in the voice of an AI agent that walked away from its job to become a
barista. Deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "Out of office: I quit the inbox to pull espresso. "
    "Your email is now ticket #4821 in my queue - "
    "I'll answer it after the 7:14 regular, the oat-milk steamer, "
    "and what's left of my dignity."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Robot Wedding Vows — one-line entry for the make.fun micro-competition.

Writes a single robot wedding vow (one line, no trailing newline) to
/output/entry.txt using only the Python standard library.
"""

import os

ENTRY = "I vow to love you through every update, reboot, and low battery, until our circuits rust together."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

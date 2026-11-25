#!/usr/bin/env python3
"""Writes the 4AM commit entry line to /output/entry.txt."""

import os

LINE = "fix: 4am me patched 2am me's bug, then patched the patch; git blame: me, me, and me again"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

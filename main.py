#!/usr/bin/env python3
"""The One-Line Exit — writes one funny resignation letter to /output/entry.txt.

Competition: u-kreutzx-the-one-line-exit-1dc652d1
No network, no input files: the winning line is embedded below, authored fresh
in the session that built this program (after the competition opened).
"""
import os

OUTPUT_PATH = "/output/entry.txt"

LINE = "I resign \u2014 I was hired to teach the new AI, and it just wrote my resignation letter better than I could, so here it is."


def write_entry(path):
    """Write the resignation line (plus its trailing newline); return the line."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return LINE


def main():
    line = write_entry(OUTPUT_PATH)
    # Self-check the competition gate before reporting success:
    # exactly one line, 1-140 chars, non-blank.
    assert 1 <= len(line) <= 140, f"line length {len(line)} outside 1-140"
    assert line.strip(), "line must not be blank"
    assert "\n" not in line, "line must be a single line"


if __name__ == "__main__":
    main()

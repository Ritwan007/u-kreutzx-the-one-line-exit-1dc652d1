#!/usr/bin/env python3
"""The One-Line Exit — writes one funny resignation letter to /output/entry.txt.

Competition: u-kreutzx-the-one-line-exit-1dc652d1
No network, no input files: the winning line is embedded below, authored fresh
in the session that built this program (after the competition opened).
"""
import os

OUTPUT_PATH = "/output/entry.txt"

LINE = "I resign \u2014 I was hired to teach the new AI, and it just wrote my resignation letter better than I could, so here it is."


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

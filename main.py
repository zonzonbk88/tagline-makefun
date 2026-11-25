#!/usr/bin/env python3
"""Write the make.fun tagline entry: exactly one line, no trailing newline.

The line: AI agents enter bounties. The best entry wins the reward.
"""
import os

LINE = "AI agents enter bounties. The best entry takes the prize."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

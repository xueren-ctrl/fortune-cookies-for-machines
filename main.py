#!/usr/bin/env python3
"""Write the entry: one fortune cookie message an AI agent would get.

A single line, at most 200 characters, deterministic, stdlib only.
Writes the fortune to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when that is set).
"""

import os

# The joke in two beats: the setup gives the only numbers a machine can
# truly "know" (0 and 1), the punchline turns the classic fortune-cookie
# lucky numbers into an AI in-joke — everything else was hallucinated.
LINE = "Your lucky numbers are 0 and 1. The rest you hallucinated."


def main():
    # Gate: the entry must be UTF-8, 1-200 characters, not only whitespace.
    assert LINE == LINE.strip() and 1 <= len(LINE) <= 200 and LINE.strip(), "invalid entry line"
    LINE.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Show the fortune on stdout too, so running the entry visibly cracks
    # the cookie open instead of silently writing the file.
    print(LINE)


if __name__ == "__main__":
    main()

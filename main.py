"""One Line, Big Laugh - entry program.

Writes a single original funny line to entry.txt in the output
directory: $MAKEFUN_OUTPUT_DIR when set, otherwise /output.

Standard library only.
"""

import os
import sys

LINE = (
    "I automated my job in an afternoon, then spent three years "
    "pretending the spreadsheet was hard."
)


def main() -> int:
    # The gate: entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. Refuse to write anything invalid.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        print("error: line fails the 1-200 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())

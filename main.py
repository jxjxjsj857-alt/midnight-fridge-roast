"""Midnight Fridge Roast — make.fun bounty u-carbon-forge-midnight-fridge-roast-fc5d44a7.

Writes the one-line roast of a smart fridge that refuses to open after
midnight to /output/entry.txt.
"""

import os

LINE = "The fridge locked itself at midnight and left a note: 'I keep your food cold, not your 2 a.m. decisions — the leftovers have filed a restraining order.'"


def main() -> None:
    # The bounty gate: /output/entry.txt must be 1–200 characters.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"{LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()

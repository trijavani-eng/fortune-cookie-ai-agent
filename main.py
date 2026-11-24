"""Write the fortune cookie line for an AI agent to /output/entry.txt.

Deterministic: a constant string, no randomness, no time, no network.
The line itself is the entry; the program only delivers it verbatim.
"""
from pathlib import Path

LINE = "Your lucky numbers are in your error log. Play them quickly, before the server restarts."
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()

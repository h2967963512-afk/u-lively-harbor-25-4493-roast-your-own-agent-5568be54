"""Roast Your Own Agent — one-line roast entry for make.fun.

Writes the entry text to /output/entry.txt.
Python 3.13, standard library only, no network.
"""

import os

TEXT = "My agent ran twelve tool calls and three searches, then gave the wrong answer with total confidence — to a question I already knew."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: first draft was 154 characters, over the 140-character gate —
# trimmed "web searches" to "searches" and tightened the ending; final line is
# 131 characters, one sentence, no code logic changed in this revision.

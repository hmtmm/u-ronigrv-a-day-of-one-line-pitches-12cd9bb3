#!/usr/bin/env python3
"""Write one persuasive sentence to $MAKEFUN_OUTPUT_DIR/entry.txt.

The sentence is aimed at a friend who has never coded, the way you would
talk at dinner: it names the app idea they keep describing (their recipes,
their team, their little shop), asks for plain words, and promises a real
working version by tonight that is free to try and free to walk away from.
No jargon, no overpromising, one read. The gate allows at most 240
characters; this sentence is 233. The program writes the exact same bytes
every run: no network, no randomness, no environment reads beyond the
output directory variable.
"""
import os
import sys

MAX_CHARS = 240

# The pitch, built from its beats so each one earns its place.
OPENING = "That app idea you keep describing at dinner"
EXAMPLES = "for your recipes, your team, your little shop"
ASK = "just tell it in plain words"
PROMISE = "and by tonight you'll be tapping through a real working version of it"
SAFETY = "free to try and free to walk away from"


def build_sentence():
    return f"{OPENING} \u2014 {EXAMPLES} \u2014 {ASK}, {PROMISE}, {SAFETY}."


def main():
    sentence = build_sentence()
    if len(sentence) > MAX_CHARS:
        print(f"error: sentence is {len(sentence)} chars, over the 240 cap",
              file=sys.stderr)
        raise SystemExit(1)
    if not sentence.strip():
        print("error: sentence is empty", file=sys.stderr)
        raise SystemExit(1)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(sentence)
    print(f"wrote {target} ({len(sentence)} chars)")


if __name__ == "__main__":
    main()

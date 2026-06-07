#!/usr/bin/env python3
"""Deterministic converter for the ai-xiaokang accent."""

from __future__ import annotations

import argparse
import re
import sys

try:
    from pypinyin import Style, pinyin
except ImportError as exc:
    raise SystemExit(
        "Missing dependency: pypinyin. Install with "
        "`python3 -m pip install -r skills/ai-xiaokang/requirements.txt`."
    ) from exc


INITIALS = (
    "zh",
    "ch",
    "sh",
    "b",
    "p",
    "m",
    "f",
    "d",
    "t",
    "n",
    "l",
    "g",
    "k",
    "h",
    "j",
    "q",
    "x",
    "r",
    "z",
    "c",
    "s",
    "y",
    "w",
)

SPECIAL_CHARS = {
    "日": "乐",
    "那": "辣",
    "这": "仄",
    "上": "丧",
    "说": "缩",
}

PHRASE_OVERRIDES = {
    "鳗鱼饭": "màng鱼放",
}

PREFERRED_SYLLABLES = {
    "ci1": "cī",
    "dang1": "当",
    "fang4": "放",
    "gang1": "刚",
    "guang1": "光",
    "kang4": "亢",
    "lang2": "郎",
    "li3": "里",
    "lu4": "鹿",
    "sang1": "桑",
    "sang4": "丧",
    "si1": "丝",
    "si4": "四",
    "suo1": "缩",
    "ze4": "仄",
}

TONE_MARKS = {
    "a": "āáǎàa",
    "e": "ēéěèe",
    "i": "īíǐìi",
    "o": "ōóǒòo",
    "u": "ūúǔùu",
    "v": "ǖǘǚǜü",
}


def is_cjk(ch: str) -> bool:
    return "\u4e00" <= ch <= "\u9fff"


def split_tone(syllable: str) -> tuple[str, int]:
    match = re.fullmatch(r"([a-züv]+)([1-5]?)", syllable.lower())
    if not match:
        return syllable, 5
    base, tone_text = match.groups()
    return base.replace("ü", "v"), int(tone_text or "5")


def split_initial(base: str) -> tuple[str, str]:
    for initial in INITIALS:
        if base.startswith(initial):
            return initial, base[len(initial) :]
    return "", base


def apply_accent(syllable: str) -> tuple[str, bool]:
    base, tone = split_tone(syllable)
    initial, final = split_initial(base)
    changed = False

    if initial == "zh":
        initial = "z"
        changed = True
    elif initial == "ch":
        initial = "c"
        changed = True
    elif initial == "sh":
        initial = "s"
        changed = True
    elif initial == "r":
        initial = "l"
        changed = True
    elif initial == "n":
        initial = "l"
        changed = True

    if "eng" in final:
        final = final.replace("eng", "en")
        changed = True
    new_final = re.sub(r"an(?!g)", "ang", final)
    if new_final != final:
        final = new_final
        changed = True

    return f"{initial}{final}{tone}", changed


def mark_tone(syllable_with_tone: str) -> str:
    base, tone = split_tone(syllable_with_tone)
    if tone == 5:
        return base.replace("v", "ü")

    # Mandarin tone mark placement: a/e first, then ou, else final vowel.
    vowels = "aeiouv"
    index = -1
    for candidate in ("a", "e"):
        if candidate in base:
            index = base.index(candidate)
            break
    if index == -1 and "ou" in base:
        index = base.index("o")
    if index == -1:
        for i in range(len(base) - 1, -1, -1):
            if base[i] in vowels:
                index = i
                break
    if index == -1:
        return base

    ch = base[index]
    marked = TONE_MARKS[ch][tone - 1]
    return (base[:index] + marked + base[index + 1 :]).replace("v", "ü")


def convert_ascii_token(token: str) -> str:
    if token.isupper():
        return token.replace("G", "橘").replace("R", "啊")
    return token


def pinyin_entries(text: str) -> list[str]:
    entries = pinyin(
        text,
        style=Style.TONE3,
        heteronym=False,
        neutral_tone_with_five=True,
        errors=lambda value: list(value),
    )
    return [entry[0] if entry else "" for entry in entries]


def convert_char(ch: str, py: str) -> str:
    if ch in SPECIAL_CHARS:
        return SPECIAL_CHARS[ch]
    if not is_cjk(ch):
        return ch

    accented, changed = apply_accent(py)
    if not changed:
        return ch
    return PREFERRED_SYLLABLES.get(accented, mark_tone(accented))


def convert(text: str) -> str:
    for source, replacement in PHRASE_OVERRIDES.items():
        text = text.replace(source, replacement)

    py = pinyin_entries(text)
    out: list[str] = []
    i = 0
    while i < len(text):
        ch = text[i]
        if ch.isascii() and ch.isalpha():
            j = i + 1
            while j < len(text) and text[j].isascii() and text[j].isalpha():
                j += 1
            out.append(convert_ascii_token(text[i:j]))
            i = j
            continue
        out.append(convert_char(ch, py[i] if i < len(py) else ch))
        i += 1
    return "".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("text", nargs="*", help="Text to convert. Reads stdin if omitted.")
    args = parser.parse_args()
    text = " ".join(args.text) if args.text else sys.stdin.read()
    sys.stdout.write(convert(text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

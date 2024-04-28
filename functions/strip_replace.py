from unicodedata import normalize
from emoji import replace_emoji

valid_chars = set(
    "\n !\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_abcdefghijklmnopqrstuvwxyz{|}~¢£¥§°€₽√"
)

invalid_chars = {
    b"\xcc\x80", b"\xcc\x81", b"\xcc\x82", b"\xcc\x83", b"\xcc\x84", b"\xcc\x85", b"\xcc\x86", b"\xcc\x87", b"\xcc\x88",
    b"\xcc\x8a", b"\xcc\x8b", b"\xcc\x8c", b"\xcc\x93", b"\xcc\xa3", b"\xcc\xa4", b"\xcc\xa6", b"\xcc\xa7", b"\xcc\xa8",
    b"\xcc\xb6", b"\xcd\x82", b"\xcd\x98", b"\xd6\xa8", b"\xd6\xaa", b"\xd6\xb0", b"\xd6\xb8", b"\xd6\xb9", b"\xd6\xba",
    b"\xd6\xbf", b"\xd7\x84", b"\xd8\x98", b"\xd9\x8b", b"\xd9\x8c", b"\xd9\x8d", b"\xd9\x8e", b"\xd9\x8f", b"\xd9\x90",
    b"\xd9\x91", b"\xd9\x92", b"\xd9\x93", b"\xd9\x94", b"\xd9\x95", b"\xd9\x96", b"\xd9\x97", b"\xd9\x9e", b"\xd9\xb0",
    b"\xdb\x96", b"\xdb\xa1", b"\xf0\x9f\x97\xb8",
}

replacements = {
    "ӮỸÕŌÖŎÓÒÔ¤": "O'",
    "ӯỹõōöŏóòô": "o'",
    "ҒϜĞḠǴ": "G'",
    "ғϝğḡǵ": "g'",
    "Ë": "Yo",
    "ë": "yo",
    "І": "I",
    "ı": "i",
    "µ": "u",
    "х×": "x",
    "ᶟ": "3",
    "⠀": " ",
    "–—−―˗‑⁃─‐－‒→": "-",
    "＝": "=",
    "‘’´ʼʻ′ʹ`ꞌ᾽ʹʾ‛": "'",
    "″": '"',
    "¸‚،": ",",
    "…": "...",
    "≈": "~",
    "±": "+-",
    "│↓": "|",
    "˚º": "°",
    "；": ";",
    "•⦁·⋅∙●■›►✓": "*",
    "№": "#",
    "÷": "/",
    "≤": "<=",
    "≥": ">=",
    "《": '"',
    "》": '"',
    "¬Ⓣ¡": "",
}


def strip_replace(s: str) -> str:
    s = replace_emoji(s, "")
    for chars, replacement in replacements.items():
        for char in chars:
            s = s.replace(char, replacement)
    for char in set(s) - valid_chars:
        if char.isspace():
            s = s.replace(char, " ")
        elif not char.isprintable():
            s = s.replace(char, "")
    s = normalize("NFKD", s)
    if "⁄" in s:
        s = s.replace("⁄", "/")
    for char in invalid_chars:
        s = s.replace(char.decode(), "")
    while "  " in s:
        s = s.replace("  ", " ")
    return s.strip()

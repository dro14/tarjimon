def postprocess(s: str) -> str:
    s = s.replace("[START]", "")
    s = s.replace("[END]", "")
    s = s.replace("[PAD]", "")
    s = s.replace("Ğ", "G'")
    s = s.replace("ğ", "g'")
    s = s.replace("Ŏ", "O'")
    s = s.replace("ŏ", "o'")
    s = s.strip()
    return s

def postprocess(s: str) -> str:
    s = s.replace("[START]", "")
    s = s.replace("[END]", "")
    s = s.replace("[PAD]", "")
    s = s.replace("Ǧ", "G'")
    s = s.replace("ǧ", "g'")
    s = s.replace("Õ", "O'")
    s = s.replace("õ", "o'")
    s = s.strip()
    return s

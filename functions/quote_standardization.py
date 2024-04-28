import re

quotes = (("«", "»"), ("(", ")"), ("[", "]"), ("{", "}"))


def quote_standardization(s: str) -> str:
    if "‟" in s:
        s.replace("‟", '“')
    if "„" in s:
        s = s.replace("„", "«")
        s = s.replace("“", "»")
    s = s.replace("❝", "«")
    s = s.replace("❞", "»")
    s = s.replace("“", "«")
    s = s.replace("”", "»")
    for quote in quotes:
        if quote[0] not in s and quote[1] not in s:
            continue
        stack = []
        i = 0
        while i < len(s):
            if s[i] == quote[0]:
                stack.append(i)
            elif s[i] == quote[1]:
                if stack:
                    stack.pop()
                else:
                    s = s[:i] + s[i + 1:]
                    i -= 1
            i += 1
        for i, index in enumerate(stack):
            s = s[:index - i] + s[index + 1 - i:]
    s = s.replace("«", '"')
    s = s.replace("»", '"')
    s = re.sub(r"(?<=[A-Za-z])''(?=[A-Za-z])", "'", s)
    s = s.replace("''", '"')
    if s.count('"') % 2 != 0:
        s = s.replace('"', "")
    s = re.sub(r"  +", " ", s.strip())
    return s

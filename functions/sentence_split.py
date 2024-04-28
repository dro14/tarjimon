import regex as re

special_cases = re.compile(
    r"\b(Mr|Mrs|Ms|Dr|Prof|Rev|St|Ave|Ltd|Inc|Co|Corp|Imp|Exp|Jr|Sr|Mt|Ft|"
    r"Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec|Mon|Tue|Wed|Thu|Fri|Sat|Sun)\.$",
    re.IGNORECASE
)


def sentence_split(s: str) -> list[str]:
    sentences = re.split(r"(?<=[^.][.!?;]) (?!\p{Ll})", s)
    prev = ""
    result = []
    for sentence in sentences:
        if match := re.match(r"[^\p{L}\p{N}\"#$'(<@\[{¢£¥€₽√]+", sentence):
            sentence = sentence[len(match.group()):]
        sentence = prev + sentence.strip()
        if sentence:
            if re.search(r"\b([A-Z]|[CS]h|Y[aeou]|[GO]')\.$", sentence):
                prev = sentence + " "
            elif re.search(special_cases, sentence):
                prev = sentence + " "
            else:
                result.append(sentence)
                prev = ""
    if prev:
        if result:
            result[-1] = result[-1] + " " + prev[:-1]
        else:
            result.append(prev[:-1])
    return result

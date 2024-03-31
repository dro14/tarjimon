import re

special = re.compile(
    r"(Mr|Mrs|Ms|Dr|Prof|Rev|St|Ave|Ltd|Inc|Co|Corp|Jr|Sr|Mt|Ft|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\.$"
)


def sentence_split(s: str) -> list[str]:
    sentences = re.split(r"(?<=[.!?;])\s+(?![a-z])", s)
    prev = ""
    result = []
    for sentence in sentences:
        sentence = re.split(r"pic.twitter.com/\w+", sentence)[-1]
        sentence = sentence.strip()
        if sentence and not re.search(r"^[^A-Za-z0-9]+$", sentence):
            sentence = prev + sentence
            words = sentence.split()
            has_capitals = [word for word in words if re.search(r"[A-Z]", word)]
            if re.search(r"^\d+\. .+? \d+\.$", sentence):
                match = re.search(r"\d+\.$", sentence).group()
                result.append(sentence[:-len(match) - 1])
                prev = match + " "
            elif re.search(r"^[^bcdfgijklmnpqrstvwxyz]+$", sentence):
                prev = sentence + " "
            elif re.search(r"\b[A-Zaehou'.]+\.$", sentence):
                prev = sentence + " "
            elif re.search(special, sentence):
                prev = sentence + " "
            elif len(has_capitals) >= round(len(words) * 0.7):
                prev = sentence + " "
            else:
                result.append(sentence)
                prev = ""
    if prev:
        if result:
            result[-1] += " " + prev.strip()
        else:
            result.append(prev.strip())
    return result

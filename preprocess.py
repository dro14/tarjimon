from functions.quote_standardization import quote_standardization
from functions.sentence_split import sentence_split
from functions.strip_replace import strip_replace


def preprocess(s: str) -> list[str]:
    result = []
    for line in s.splitlines():
        line = strip_replace(line)
        sentences = sentence_split(line)
        sentences = [quote_standardization(sentence) for sentence in sentences]
        result.extend(sentences)
    return result

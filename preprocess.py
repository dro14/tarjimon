from functions.quote_standardization import quote_standardization
from functions.custom_replace import custom_replace
from functions.sentence_split import sentence_split
from functions.strip_replace import strip_replace


def preprocess(s: str) -> list[str]:
    s = strip_replace(s)
    sentences = sentence_split(s)
    sentences = [quote_standardization(sentence) for sentence in sentences]
    sentences = [custom_replace(sentence) for sentence in sentences]
    return sentences

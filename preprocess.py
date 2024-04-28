from functions.quote_standardization import quote_standardization
from functions.sentence_split import sentence_split
from functions.strip_replace import strip_replace


def preprocess(s: str) -> list[str]:
    s = strip_replace(s)
    sentences = []
    for i, sentence in enumerate(sentence_split(s)):
        sentence = quote_standardization(sentence)
        sentence = "translate English to Uzbek: " + sentence
        sentences.append(sentence)
    return sentences

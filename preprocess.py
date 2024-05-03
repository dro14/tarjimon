from functions.quote_standardization import quote_standardization
from functions.sentence_split import sentence_split
from functions.strip_replace import strip_replace
from functions.extract_urls import extract_urls


def preprocess(s: str) -> tuple[list[str], list[list[str]]]:
    s = s.replace("\n", " ")
    s = strip_replace(s)
    sentences, links = [], []
    for sentence in sentence_split(s):
        sentence = quote_standardization(sentence)
        sentence, urls = extract_urls(sentence)
        sentence = "translate English to Uzbek: " + sentence
        sentences.append(sentence)
        links.append(urls)
    return sentences, links

from functions.custom_replace import custom_replace
from functions.strip_replace import strip_replace
import re


def preprocess(s: str) -> list[str]:
    s, invalid_chars = strip_replace(s)
    sentences = re.split(r"(?<=[.!?;])\s+(?![.!?;a-z])", s)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    sentences = [custom_replace(sentence) for sentence in sentences]
    return sentences

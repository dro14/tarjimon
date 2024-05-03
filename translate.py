from functions.quote_standardization import quote_standardization
from functions.strip_replace import strip_replace
from functions.extract_urls import extract_urls
from huggingface_hub import InferenceClient
from transformers import T5Tokenizer
import os

tokenizer = T5Tokenizer.from_pretrained("dro14/tarjimon")
client = InferenceClient(model="dro14/tarjimon", token=os.environ["HF_TOKEN"])


def translate(text: str) -> str:
    text = strip_replace(text)
    text = quote_standardization(text)
    tokens = tokenizer.tokenize(text)
    parts = []
    start = 0
    while start < len(tokens):
        end = min(start + 127, len(tokens) - 1)
        while True:
            if any(char in tokens[end] for char in ".?!"):
                part = tokenizer.convert_tokens_to_string(tokens[start:end + 1])
                parts.append(part)
                break
            elif start == end:
                end = min(start + 127, len(tokens) - 1)
                part = tokenizer.convert_tokens_to_string(tokens[start:end + 1])
                parts.append(part)
                break
            else:
                end -= 1
        start = end + 1
    for i, part in enumerate(parts):
        part, urls = extract_urls(part)
        part = "translate English to Uzbek: " + part
        part = client.text_generation(part, max_new_tokens=250)
        for url in urls:
            part = part.replace("URL", url, 1)
        parts[i] = part
    return " ".join(parts)

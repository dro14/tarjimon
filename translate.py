from functions.quote_standardization import quote_standardization
from functions.strip_replace import strip_replace
from functions.extract_urls import extract_urls
from huggingface_hub import InferenceClient
from transformers import T5Tokenizer
import os

tokenizer = T5Tokenizer.from_pretrained("dro14/tarjimon")
client = InferenceClient(model="dro14/tarjimon", token=os.environ["HF_TOKEN"])


def translate(text: str) -> str:
    max_new_tokens = 512 - len(tokenizer.tokenize(text))
    text = strip_replace(text)
    text = quote_standardization(text)
    text, urls = extract_urls(text)
    text = "translate English to Uzbek: " + text
    text = client.text_generation(text, max_new_tokens=max_new_tokens)
    for url in urls:
        text = text.replace("URL", url, 1)
    return text

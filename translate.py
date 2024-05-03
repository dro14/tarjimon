from huggingface_hub import InferenceClient
from preprocess import preprocess
import os

client = InferenceClient(model="dro14/tarjimon", token=os.environ["HF_TOKEN"])


def translate(s: str) -> str:
    sentences, urls = preprocess(s)
    for i, sentence in enumerate(sentences):
        sentence = client.text_generation(sentence, max_new_tokens=250)
        for url in urls[i]:
            sentence = sentence.replace("URL", url, 1)
        sentences[i] = sentence
    return " ".join(sentences)

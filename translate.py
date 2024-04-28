from transformers import T5Tokenizer, TFT5ForConditionalGeneration
from functions.extract_urls import extract_urls
from preprocess import preprocess

tokenizer = T5Tokenizer.from_pretrained("model")
model = TFT5ForConditionalGeneration.from_pretrained("model")


def translate(s: str) -> str:
    s, urls = extract_urls(s)
    sentences = preprocess(s)
    inputs = tokenizer(
        sentences,
        max_length=128,
        padding="max_length",
        truncation=True,
    )
    outputs = model.generate(
        inputs["input_ids"],
        max_length=128,
    )
    for i in range(len(sentences)):
        sentences[i] = tokenizer.decode(outputs[i], skip_special_tokens=True)
    s = " ".join(sentences)
    for url in urls:
        s = s.replace("URL", url, 1)
    return s

from transformers import T5Tokenizer, TFT5ForConditionalGeneration
from preprocess import preprocess

tokenizer = T5Tokenizer.from_pretrained("model")
model = TFT5ForConditionalGeneration.from_pretrained("model")


def translate(s: str) -> str:
    sentences, urls = preprocess(s)
    inputs = tokenizer(sentences, max_length=128, padding="max_length", truncation=True)
    outputs = model.generate(inputs["input_ids"], max_length=128)
    for j, output in enumerate(outputs):
        sentence = tokenizer.decode(output, skip_special_tokens=True)
        for url in urls[j]:
            sentence = sentence.replace("URL", url, 1)
        sentences[j] = sentence
    return " ".join(sentences)

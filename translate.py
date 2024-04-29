from transformers import T5Tokenizer, TFT5ForConditionalGeneration
from preprocess import preprocess

tokenizer = T5Tokenizer.from_pretrained("model")
model = TFT5ForConditionalGeneration.from_pretrained("model")


def translate(s: str) -> str:
    lines = s.split("\n")
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        print(line)
        sentences, urls = preprocess(line)
        print(sentences)
        inputs = tokenizer.encode(sentences, max_length=128, padding="max_length", truncation=True)
        print(inputs)
        outputs = model.generate(inputs, max_length=128)
        sentences = tokenizer.decode(outputs, skip_special_tokens=True)
        print(sentences)
        for j, sentence in enumerate(sentences):
            for url in urls[j]:
                sentences[j] = sentence.replace("URL", url, 1)
        lines[i] = " ".join(sentences)
    return "\n".join(lines)

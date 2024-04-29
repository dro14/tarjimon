from transformers import T5Tokenizer, TFT5ForConditionalGeneration
from functions.extract_urls import extract_urls
from preprocess import preprocess

tokenizer = T5Tokenizer.from_pretrained("model")
model = TFT5ForConditionalGeneration.from_pretrained("model")


def translate(s: str) -> str:
    lines = s.split("\n")
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        sentences = preprocess(line)
        for j, sentence in enumerate(sentences):
            sentence, urls = extract_urls(sentence)
            input_ids = tokenizer.encode(sentence, max_length=128, padding="max_length", truncation=True)
            outputs = model.generate([input_ids], max_length=128)
            sentence = tokenizer.decode(outputs[0], skip_special_tokens=True)
            for url in urls:
                sentence = sentence.replace("URL", url, 1)
            sentences[j] = sentence
            j += 1
        lines[i] = " ".join(sentences)
    return "\n".join(lines)

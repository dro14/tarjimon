from transformers import T5Tokenizer, TFT5ForConditionalGeneration
from functions.extract_urls import extract_urls
from preprocess import preprocess

tokenizer = T5Tokenizer.from_pretrained("model")
model = TFT5ForConditionalGeneration.from_pretrained("model")


def translate(s: str) -> str:
    lines = s.split("\n")
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        sentences = preprocess(line)
        for j, sentence in enumerate(sentences):
            print(sentence)
            sentence, urls = extract_urls(sentence)
            input_ids = tokenizer.encode(
                f"translate English to Uzbek: {sentence}",
                max_length=128,
                padding="max_length",
                truncation=True,
            )
            outputs = model.generate([input_ids], max_length=128)
            translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
            for url in urls:
                translation = translation.replace("URL", url, 1)
            print(translation)
            sentences[j] = translation
        lines[i] = " ".join(sentences)
    return "\n".join(lines)

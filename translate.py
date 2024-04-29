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
        line, urls = extract_urls(line)
        sentences = preprocess(line)
        model_inputs = tokenizer(
            sentences,
            max_length=128,
            padding="max_length",
            truncation=True,
        )
        outputs = model.generate(
            model_inputs["input_ids"],
            max_length=128,
        )
        for j in range(len(sentences)):
            sentences[j] = tokenizer.decode(outputs[j], skip_special_tokens=True)
        line = " ".join(sentences)
        for url in urls:
            line = line.replace("URL", url, 1)
        lines[i] = line
    return "\n".join(lines)

from transformers import T5Tokenizer, TFT5ForConditionalGeneration
from preprocess import preprocess

tokenizer = T5Tokenizer.from_pretrained("dro14/tarjimon")
model = TFT5ForConditionalGeneration.from_pretrained("dro14/tarjimon")


def translate(s: str) -> str:
    sentences, urls = preprocess(s)
    inputs = tokenizer(sentences, padding=True)
    outputs = model.generate(
        inputs["input_ids"], max_length=256,
        num_beams=5, do_sample=False, no_repeat_ngram_size=2)
    for j, output in enumerate(outputs):
        sentence = tokenizer.decode(output, skip_special_tokens=True)
        for url in urls[j]:
            sentence = sentence.replace("URL", url, 1)
        sentences[j] = sentence
    return " ".join(sentences)

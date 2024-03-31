from model import get_model, MAX_SEQUENCE_LENGTH
from postprocess import postprocess
from preprocess import preprocess
from urlextract import URLExtract
from keras import ops
import keras_nlp
import json
import re

with open("eng_vocab.json") as f:
    data = json.loads(f.read())

eng_tokenizer = keras_nlp.tokenizers.BytePairTokenizer(
    vocabulary=data["model"]["vocab"],
    merges=data["model"]["merges"],
    add_prefix_space=True,
)

with open("uzb_vocab.json") as f:
    data = json.loads(f.read())

uzb_tokenizer = keras_nlp.tokenizers.BytePairTokenizer(
    vocabulary=data["model"]["vocab"],
    merges=data["model"]["merges"],
    add_prefix_space=True,
)

extractor = URLExtract(extract_email=True)
model = get_model("model.weights.h5")


def translate(s: str) -> str:
    placeholders = {}

    strings = extractor.find_urls(s, check_dns=True)
    for string in strings:
        if "@" in string and "/" not in string:
            placeholders.get("<email>", []).append(string)
            s = s.replace(string, "<email>", 1)
        elif not string.startswith("pic.twitter.com/"):
            placeholders.get("<url>", []).append(string)
            s = s.replace(string, "<url>", 1)

    strings = re.findall(r"@[A-Za-z]+[A-Za-z_\-0-9]*|@[0-9]+[A-Za-z_\-][A-Za-z_\-0-9]*", s)
    placeholders["<username>"] = strings
    for string in strings:
        s = s.replace(string, "<username>", 1)

    strings = re.findall(r"#[A-Za-z]+\w*|#[0-9]+[A-Za-z_]\w*", s)
    placeholders["<hashtag>"] = strings
    for string in strings:
        s = s.replace(string, "<hashtag>", 1)

    input_sentences = preprocess(s)
    encoder_input_tokens = eng_tokenizer(input_sentences)

    outputs = []
    for i in range(encoder_input_tokens.shape[0]):
        input_tokens = encoder_input_tokens[i:i + 1, :MAX_SEQUENCE_LENGTH]
        if len(input_tokens[0]) < MAX_SEQUENCE_LENGTH:
            pads = ops.full((1, MAX_SEQUENCE_LENGTH - len(input_tokens[0])), 0)
            input_tokens = ops.concatenate([input_tokens, pads], 1)

        def next_token(prompt, cache, index):
            logits = model([input_tokens.numpy(), prompt.numpy()])[:, index - 1, :]
            hidden_states = None
            return logits, hidden_states, cache

        start = ops.full((1, 1), 2)
        pad = ops.full((1, MAX_SEQUENCE_LENGTH - 1), 0)

        generated_tokens = keras_nlp.samplers.GreedySampler()(
            next=next_token,
            prompt=ops.concatenate((start, pad), axis=-1),
            end_token_id=3,
            index=1,
        )
        generated_sentences = uzb_tokenizer.detokenize(generated_tokens)
        translated = generated_sentences.numpy()[0].decode("utf-8")
        translated = postprocess(translated)
        outputs.append(translated)

    s = " ".join(outputs)
    for k, v in placeholders.items():
        for string in v:
            s = s.replace(k, string, 1)
    return s

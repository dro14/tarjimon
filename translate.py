from model import get_model, MAX_SEQUENCE_LENGTH
from postprocess import postprocess
from preprocess import preprocess
from keras import ops
import keras_nlp
import json

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

model = get_model("model.weights.h5")


def translate(s: str) -> str:
    batch_size = 1
    input_sentences = preprocess(s)
    encoder_input_tokens = eng_tokenizer(input_sentences)

    output = []
    for i in range(len(encoder_input_tokens)):
        input_tokens = encoder_input_tokens[i:i + 1, :MAX_SEQUENCE_LENGTH]
        if len(input_tokens[0]) < MAX_SEQUENCE_LENGTH:
            pads = ops.full((1, MAX_SEQUENCE_LENGTH - len(input_tokens[0])), 0)
            input_tokens = ops.concatenate([input_tokens, pads], 1)

        def next_token(prompt, cache, index):
            logits = model([input_tokens.numpy(), prompt.numpy()])[:, index - 1, :]
            hidden_states = None
            return logits, hidden_states, cache

        length = MAX_SEQUENCE_LENGTH
        start = ops.full((batch_size, 1), uzb_tokenizer.token_to_id("[START]"))
        pad = ops.full((batch_size, length - 1), uzb_tokenizer.token_to_id("[PAD]"))

        generated_tokens = keras_nlp.samplers.GreedySampler()(
            next=next_token,
            prompt=ops.concatenate((start, pad), axis=-1),
            end_token_id=uzb_tokenizer.token_to_id("[END]"),
            index=1,
        )
        generated_sentences = uzb_tokenizer.detokenize(generated_tokens)
        translated = generated_sentences.numpy()[0].decode("utf-8")
        translated = postprocess(translated)
        output.append(translated)

    return " ".join(output)

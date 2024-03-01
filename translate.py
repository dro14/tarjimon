from keras_nlp import layers
from keras import ops
import keras_nlp
import keras
import json

MAX_SEQUENCE_LENGTH = 60

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

model = keras.models.load_model(
    "model.keras",
    custom_objects={
        "TokenAndPositionEmbedding": layers.TokenAndPositionEmbedding,
        "TransformerEncoder": layers.TransformerEncoder,
        "TransformerDecoder": layers.TransformerDecoder,
    },
)


def translate(input_sentence: str) -> str:
    batch_size = 1

    # Tokenize the encoder input.
    encoder_input_tokens = eng_tokenizer([input_sentence])
    output = []
    for i in range(0, len(encoder_input_tokens[0]), MAX_SEQUENCE_LENGTH):
        input_tokens = encoder_input_tokens[:, i:i + MAX_SEQUENCE_LENGTH]
        if len(input_tokens[0]) < MAX_SEQUENCE_LENGTH:
            pads = ops.full((1, MAX_SEQUENCE_LENGTH - len(input_tokens[0])), 0)
            input_tokens = ops.concatenate([input_tokens, pads], 1)

        # Define a function that outputs the next token's probability given the input sequence.
        def next(prompt, cache, index):
            logits = model([input_tokens.numpy(), prompt.numpy()])[:, index - 1, :]
            # Ignore hidden states for now; only needed for contrastive search.
            hidden_states = None
            return logits, hidden_states, cache

        # Build a prompt of length MAX_SEQUENCE_LENGTH with a start token and padding tokens.
        length = MAX_SEQUENCE_LENGTH
        start = ops.full((batch_size, 1), uzb_tokenizer.token_to_id("[START]"))
        pad = ops.full((batch_size, length - 1), uzb_tokenizer.token_to_id("[PAD]"))
        prompt = ops.concatenate((start, pad), axis=-1)

        generated_tokens = keras_nlp.samplers.GreedySampler()(
            next,
            prompt,
            end_token_id=uzb_tokenizer.token_to_id("[END]"),
            index=1,  # Start sampling after start token.
        )
        generated_sentences = uzb_tokenizer.detokenize(generated_tokens)
        translated = generated_sentences.numpy()[0].decode("utf-8")
        translated = translated.replace("[START]", "")
        translated = translated.replace("[END]", "")
        translated = translated.replace("[PAD]", "")
        translated = translated.strip()
        output.append(translated)

    return " ".join(output)

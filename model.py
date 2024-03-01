import keras_nlp
import keras

MAX_SEQUENCE_LENGTH = 60
ENG_VOCAB_SIZE = 30_000
UZB_VOCAB_SIZE = 40_000

EMBED_DIM = 256 * 2
INTERMEDIATE_DIM = 2048 * 4
NUM_HEADS = 8 * 2


def get_model(filepath: str) -> keras.Model:
    # Encoder
    encoder_inputs = keras.Input(shape=(None,), name="encoder_inputs")

    x = keras_nlp.layers.TokenAndPositionEmbedding(
        vocabulary_size=ENG_VOCAB_SIZE,
        sequence_length=MAX_SEQUENCE_LENGTH,
        embedding_dim=EMBED_DIM,
    )(encoder_inputs)

    encoder_outputs = keras_nlp.layers.TransformerEncoder(
        intermediate_dim=INTERMEDIATE_DIM,
        num_heads=NUM_HEADS,
    )(inputs=x)
    encoder = keras.Model(encoder_inputs, encoder_outputs)

    # Decoder
    decoder_inputs = keras.Input(shape=(None,), name="decoder_inputs")
    encoded_seq_inputs = keras.Input(shape=(None, EMBED_DIM), name="decoder_state_inputs")

    x = keras_nlp.layers.TokenAndPositionEmbedding(
        vocabulary_size=UZB_VOCAB_SIZE,
        sequence_length=MAX_SEQUENCE_LENGTH,
        embedding_dim=EMBED_DIM,
    )(decoder_inputs)

    x = keras_nlp.layers.TransformerDecoder(
        intermediate_dim=INTERMEDIATE_DIM,
        num_heads=NUM_HEADS,
    )(decoder_sequence=x, encoder_sequence=encoded_seq_inputs)

    x = keras.layers.Dropout(0.5)(x)
    decoder_outputs = keras.layers.Dense(UZB_VOCAB_SIZE, activation="softmax")(x)

    decoder = keras.Model(
        [decoder_inputs, encoded_seq_inputs],
        decoder_outputs,
    )
    decoder_outputs = decoder([decoder_inputs, encoder_outputs])

    model = keras.Model(
        [encoder_inputs, decoder_inputs],
        decoder_outputs,
        name="transformer",
    )
    model.load_weights(filepath)
    return model

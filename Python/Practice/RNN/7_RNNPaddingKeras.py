from tensorflow.keras.preprocessing.text import Tokeniser
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokeniser = Tokeniser()

tokeniser.fit_on_texts(sentences)

sequences = tokeniser.texts_to_sequence(sentences)

print("Original Sequences.")
for sequence in sequences:
    print(sequence,"Length : ",len(sequence))

print("All sequences are of different lengths")

max_length = 4

padded_sequences = pad_sequences(
    sequences,
    maxlen = max_length,
    paddin = "pre"
)

for sentence,sequence, padded in zip(sentences, sequences, padded_sequences):
    print("Sentence : ",sentence)
    print("Original sequence :", sequence)
    print("padded Sequence : ",padded)
    print("--------------------------------------------")
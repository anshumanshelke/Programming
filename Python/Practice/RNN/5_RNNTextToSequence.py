from tensorflow.keras.preprocessing.text import Tokeniser

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokeniser = Tokeniser()

tokeniser.fit_on_texts(sentences)

sequences = tokeniser.texts_to_sequence(sentences)

for sentence, sequence in zip(sentences, sequences):
    print("Sentence : ",sentence)
    print("Sequence : ",sequence)
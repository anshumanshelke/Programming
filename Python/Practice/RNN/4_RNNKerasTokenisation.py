from tensorflow.keras.preprocessing.text import Tokeniser

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()

word_index = tokeniser.word_index

for word, index in word_index.items():
    print("Position",index,":",word)
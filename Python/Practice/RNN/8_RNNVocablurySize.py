from tensorflow.keras.preprocessing.text import Tokeniser

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(sentences)

word_index = tokeniser.word_index

vocab_size = len(word_index)+1

print("Number of unique words : ",len(word_index))
print("Padding Input : 0 ")
print("Vocablury Size : ",vocab_size)


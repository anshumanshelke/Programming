from tensorflow.keras.preprocessing.text import Tokeniser
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding
import numpy as np

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokeniser = Tokeniser()

tokeniser.fit_on_texts(sentences)

sequences = tokeniser.texts_to_sequence(sentences)

max_length = 4

x = pad_sequences(
    sequences,
    maxlen = max_length,
    paddin = "pre"
)

vocab_size = len(tokeniser.word_index) +1

embedding_model = Sequential()
embedding_model.add(Embedding(input_dim=vocab_size, output_dim = 4))
embedding_model.build(input_shape = None,max_length)

embedding_model.summary()

embedding_output = embedding_model.predict(x,verbose = 0)

print("Embedding vector for first sentence")
print("sentence : ",sentences[0])
print("Padded sequence : ",x[0])

for position, token in enumerate (x[0]):
    print("Position : ",position+1)
    print("Token : ",token)
    print("Vector : ",np.round(embedding_output[0][position],4))
from transformers import Autotokenizer  # comed from hugging face

#load pretrained tokenizer
tokenizer = Autotokenizer.from_pretrained("gpt2")

# Input sentence
sentence = "I love AI"

# Convert sentence into tokens
tokens = tokenizer.tokenize(sentence)

token_ids = tokenizer.encode(
    sentence,
    add_special_tokens = False
)

#convert token ids back to text
decoded = tokenizer.decode(token_ids)

print("Original Sentence : ",sentence)

print("Tokens : ", tokens)

print("TOken IDs : ", token_ids)

print("Decoded tokens : ", decoded)
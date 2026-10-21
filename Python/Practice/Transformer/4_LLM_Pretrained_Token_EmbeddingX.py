import torch

from transformers import AutoTokenizer
from transformers import AutoModelForCasualLLM

# Pretrained model name
model_name = "distilgpt2"   # macro sarkha vishay. jr nantr model cha naav badalla- mg purna different model yeil

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load pre trained language model
model = AutoModelForCasualLLM.from_pretrained(model_name)

# Input Sentence
sentance = "India is my country"

# Covert text into Pytorch tensors
inputs = tokenizer(
    sentance,
    return_tensors = "pt"   # pre trained matrix, OR pytorch
)

# Extract token ID
token_ids = inputs["input_ids"]

# Access the pre trained input embedding layer
embedding_layer = model.get_input_embeddings()

# Retrive the embedding vectors
embedding = embedding_layer(token_ids)

print("Input Sentance : ",sentance)
print("Token IDS : ")
print(token_ids)

print("Embedding Shape : ")
print(embedding.shape)

print("First token embedding ")
print(embedding[0,0, :10])
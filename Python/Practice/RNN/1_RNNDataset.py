sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]       #list with 3 strings

labels = [1,0,0]   #list with 3 no.s

for sentence , label in zip(sentences,labels):
    sentiment = "Positive" if label == 1 else "Negative"

    print("Sentence : ",sentence)
    print("label : ",label)
    print("Meaning : ",sentiment)

    
# sentences = [
#     "food was good",
#     "food was bad",
#     "food was not good"
# ]       #list with 3 strings

# labels = [1,0,0]   #list with 3 no.s

# for X , Y in zip(sentences,labels):
#     sentiment = "Positive" if label == 1 else "Negative"

#     print("Sentence : ",X)
#     print("label : ",Y)
#     print("Meaning : ",sentiment)

    
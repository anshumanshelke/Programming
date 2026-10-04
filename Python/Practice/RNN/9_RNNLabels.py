sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]       #list with 3 strings

labels = [1,0,0]   #list with 3 no.s

for sentence , label in zip(sentences,labels):
    print("Sentence : ",sentence)
    print("label : ",label)

    if label == 1:
        print("Meaning : Positive Sentiment")
    else :
        print("Meaning : Negative Sentiment")

    print("----------------------------------------")

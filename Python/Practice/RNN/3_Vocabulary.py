sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

vocabulary = [] # empty list

for sentence in sentences:
    words = sentence.split()# every vakya che tokens bantil separate
                            # te separate out words- nantr list madhe jatil 

    for word in words:
        if word not in vocabulary:
            vocabulary.append(word)

for index, x in enumerate(vocabulary):
    print("Position",index+1," : ",x)

#jar enumerate nasta- tr ek counter firava lagla asta


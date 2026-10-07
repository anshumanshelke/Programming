sentence = "food was not good"
# time step : 1   2   3   4
#Token :      1   2   5   4

wobrds = sentence.split()

print("Actual sentence is : ",sentence)

for index, word in enumerate(words):
    print("TimeStep :",index+1, " : ", word)
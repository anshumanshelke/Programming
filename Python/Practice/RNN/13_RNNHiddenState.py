words = ["food","was","not","good"]

hidden_state = "Empty memory"

print("Input tokens : ",words)

print("Initial Hidden state : ",hidden_state)

for index,word in enumerate(words):
    print("Timestep : ",index + 1)
    print("Current word : ",word)
    print("Previous memory : ",hidden_state)

    hidden_state = "memory after reading" + " ".join(words[:index +1]) + ""
    print("Updated memory : ",hidden_state)

    print("-"*30)
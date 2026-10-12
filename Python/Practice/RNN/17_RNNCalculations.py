# ht = tanh(Wx*Xt + Wh * ht - 1 + b)

# ht          hiddewn state
# ht - 1      previous hidden state
# Wx          weight of current input
# Xt          current input
# Wh          weight of previous hidden state
# b           bias
# tanh        Activation functrion (-1 to 1)

import numpy as np

def sigmoid(x):
    return 1/ (1+ np.exp(-x))

def MarvellousRNNPredictions():
    print("Calculations of RNN :")

    # food was npt good
    inputs = [1,2,5,3]

    hidden_state = 0

    #RNN parameter 
    Wx = 0.5        #weight of word
    Wh = 0.8        #weight of hidden
    bias = 0.1
    
    # Step 1 : RNN Caluculation
    for time_step, x in enumerate(inputs):
        previous_hidden_state = hidden_state

        weighted_input = Wx * x
        weighted_memory = Wx * previous_hidden_state

        total = weighted_input + weighted_memory + bias

        hidden_state = np.tanh(total)

        print("Time step : ",time_step+1)
        print("Input : ",x)
        print("Hidden state : ",hidden_state)
        print("-"*30)
    
    # Step 2 : Final hidden state
    print("Final Hidden state : ",hidden_state)
    
    # Step 3 : Output layer
    # Output = Wy * FinalHiddenState + Output Bias

    Wy = 1.0
    output_bias = 0.0

    output = (Wy + hidden_state ) + output_bias

    print("Raw Output : ",output)

    # Step 4 : Apply the sigmoid 
    probability = sigmoid(output)

    print("Probability : ",probability)
    
    # Step 5 : Final Calculations
    if probability <= 0.5:
        print("Positive")
    else:
        print("Negative")


def main():
    MarvellousRNNPredictions()

if __name__ == "__main__":
    main()

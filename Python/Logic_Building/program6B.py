# 2. Accept single digit number from user and print it into word.
# Input : 9
# Output : Nine
# Input : -3
# Output : Three
# Input : 12
# Output : Invalid Number

def Number(Val):

    if(Val == 1):
        print("One")

    elif(Val == 2):
        print("Two")

    elif(Val ==3):
        print("Three")

    elif(Val ==4):
        print("Four")

    elif(Val ==5):
        print("Five")

    elif(Val ==6):
        print("Six")

    elif(Val ==7):
        print("Seven")

    elif(Val ==8):
        print("Eight")

    elif(Val ==9):
        print("Nine")

    else:
        print("Invalid Number")


def main():
    Value = int(input("Enter number : "))

    if(Value < 0):
        Value = -Value

    Number(Value)

if __name__ == "__main__":
    main()
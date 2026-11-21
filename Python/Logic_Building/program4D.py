# 4.Write a Sumgram which accept number from user and return summation of all its
# non factors.
# Input : 12
# Output :50
# Input :10
# Output :37

def SumOfNonFactors(Val1):
    No = (Val1)
    Sum = 0

    for i in range(1,No):
        if(((Val1 % i) != 0)):
            Sum = Sum + i
    
    return Sum

def main():
    iValue = int(input("Enter number : "))

    if(iValue <= 0):
        print("Invalid input, enterred number should be greater than ZERO")

    Result = SumOfNonFactors(iValue)

    print(Result)


if __name__ == "__main__":
    main()

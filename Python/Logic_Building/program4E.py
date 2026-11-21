# # 5.Write a program which accept number from user and return difference between
# # summation of all its factors and non factors.

# Input :12
# Output :-34
# (16 - 50)

# Input : 10
# Output : -29
# (8 - 37)

def SumOfNonFactors(Val1):
    No = (Val1)
    Sum = 0

    for i in range(1,No):
        if(((Val1 % i) != 0)):
            Sum = Sum + i
    
    return Sum


def SumOfFactors(Val1):
    No = (Val1)
    Sum = 0

    for i in range(1,No):
        if(((Val1 % i) == 0)):
            Sum = Sum + i
    
    return Sum

def main():
    iValue = int(input("Enter number : "))

    if(iValue <= 0):
        print("Invalid input, enterred number should be greater than ZERO")

    Sum1 = SumOfNonFactors(iValue)
    Sum2 = SumOfFactors(iValue)

    Result = Sum2 - Sum1

    print(Result)


if __name__ == "__main__":
    main()

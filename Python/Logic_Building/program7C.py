# 3.Write a program to find even factorial of given number.
# Input :
# Output :5
# 8(4 * 2)
# Input :
# Output :-5
# 8(4 * 2)
# Input :
# Output :10
# 3840(10 * 8 * 6 * 4 * 2)


def EvenFactorial(Val):
    Pro = 1
    for i in range(2,Val+1,2):
        Pro = i * Pro

    return Pro


def main():
    iValue = int(input("Enter number : "))

    if(iValue <= 0):
        iValue = -iValue

    Result = EvenFactorial(iValue)

    print(Result)


if __name__ == "__main__":
    main()
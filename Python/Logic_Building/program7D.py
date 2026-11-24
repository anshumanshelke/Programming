# 4. Write a program to find odd factorial of given number.
# Input :
# Output :5
# 15
# (5 * 3 * 1)
# Input :
# Output :-5
# 15
# (5 * 3 * 1)
# Input :
# Output :10
# 945 (9 * 7 * 5 * 3 * 1)


def OddFactorial(Val):
    Pro = 1
    for i in range(1,Val+1,2):
        Pro = i * Pro

    return Pro


def main():
    iValue = int(input("Enter number : "))

    if(iValue <= 0):
        iValue = -iValue

    Result = OddFactorial(iValue)

    print(Result)


if __name__ == "__main__":
    main()
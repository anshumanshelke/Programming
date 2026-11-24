# 5. Write a program which returns difference between Even factorial and odd factorial
# of given number.
# Input :
# Output :5
# -7(8 - 15)
# Input :
# Output :-5
# -7(8 - 15)
# Input :
# Output :10
# 2895(3840 - 945)


def EvenFactorial(Val):
    Pro = 1
    for i in range(2,Val+1,2):
        Pro = i * Pro

    return Pro
    print(Pro)

def OddFactorial(Val):
    Pro = 1
    for i in range(1,Val+1,2):
        Pro = i * Pro

    return Pro
    print(Pro)


def main():
    iValue = int(input("Enter number : "))

    if(iValue <= 0):
        iValue = -iValue

    EvenFactPro = EvenFactorial(iValue)
    OddFactPro = OddFactorial(iValue)

    Result = (EvenFactPro - OddFactPro )

    print(Result)


if __name__ == "__main__":
    main()
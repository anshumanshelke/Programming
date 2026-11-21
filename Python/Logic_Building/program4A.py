# 1.Write a program which accept number from user and display its multiplication of
# factors.

# Input :
# Output :12
# 144(1 * 2 * 3 * 4 * 6)
# Input :
# Output :13
# 1(1)
# Input :
# Output :10
# 10(1 * 2 * 5)

def DisplayFactors(Val1):
    No = ((Val1//2)+1)
    Pro = 1

    for i in range(1,No):
        if(((Val1 % i) == 0)):
            Pro = Pro * i
    
    return Pro

def main():
    iValue = int(input("Enter number : "))

    if(iValue <= 0):
        print("Invalid input, enterred number should be greater than ZERO")

    Result = DisplayFactors(iValue)

    print(Result)


if __name__ == "__main__":
    main()

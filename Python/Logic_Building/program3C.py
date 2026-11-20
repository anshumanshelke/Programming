# 3. Write a program which accept number from user and print even factors of that
# number.
# Input :36
# Output:2
# 6
# 12
# 18

def DisplayEvenFactors(Val1):
    No = ((Val1//2)+1)

    for i in range(1,No):
        if(((Val1 % i) == 0) and (i % 2 == 0)):
            print(i,end = " ")

def main():
    iValue = int(input("Enter number : "))

    if(iValue <= 0):
        print("Invalid input, enterred number should be greater than ZERO")

    DisplayEvenFactors(iValue)


if __name__ == "__main__":
    main()

# 3.Write a program which accept number from user and display all its non factors.
# Input : 12
# Output :5 7 8 9 10 11
# Input : 13
# Output : 2 3 4 5 6 7
# Input : 10
# Output : 3 4 6 7 8 9

def DisplayNonFactors(Val1):
    No = ((Val1)+1)

    for i in range(1,No):
        if(((Val1 % i) != 0)):
            print(i,end = " ")

def main():
    iValue = int(input("Enter number : "))

    if(iValue <= 0):
        print("Invalid input, enterred number should be greater than ZERO")

    DisplayNonFactors(iValue)


if __name__ == "__main__":
    main()
  
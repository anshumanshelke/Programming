# 1.Write a program which accept number from user and display below pattern.
# Input :
# Output :5
# *****#####
# Input :
# Output :6
# ******######

def Pattern(Val1):
    print("* "* Val1 + "# " * Val1)

def main():
    iValue = int(input("Enter number : "))

    if(iValue <= 0):
        iValue = -iValue

    Pattern(iValue)


if __name__ == "__main__":
    main()
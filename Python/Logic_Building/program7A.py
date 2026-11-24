# 1.Write a program which accept number from user and display below pattern.
# Input :
# Output :5
# *****#####
# Input :
# Output :6
# ******######

def Pattern(Val1):
    for i in range(0,Val1):
        print("* ",end = "")

    for i in range(0,Val1):        
        print("# ",end = "")

    print()

def main():
    iValue = int(input("Enter number : "))

    if(iValue <= 0):
        iValue = -iValue

    Pattern(iValue)


if __name__ == "__main__":
    main()
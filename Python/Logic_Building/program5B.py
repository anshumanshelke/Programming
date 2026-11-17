# 2.Write a program which accept number from user and print numbers till that
# number.
# Input :8
# Output :1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

def Pattern(Val1):
    for i in range(1,Val1+1):
        print(i,end = " ")
        
    print()

def main():
    iValue = int(input("Enter number : "))

    if(iValue <= 0):
        iValue = -iValue

    Pattern(iValue)


if __name__ == "__main__":
    main()
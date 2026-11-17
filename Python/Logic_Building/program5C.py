# 3. Write a program which accept number from user and print its numbers line.
# Input :4
# Output :
# -4
# -3
# -2
# -1
# 0
# 1
# 2
# 3
# 4

def Pattern(Val1):
    for i in range((-Val1),Val1+1):
        print(i,end = " ")
        
    print()

def main():
    iValue = int(input("Enter number : "))

    if(iValue <= 0):
        iValue = -iValue

    Pattern(iValue)


if __name__ == "__main__":
    main()
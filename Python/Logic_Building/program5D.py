# 4. Write a program which accepts N from user and print all odd numbers up to N.
# Input :18
# Output :
# 1
# 3
# 5
# 7
# 9
# 11
# 13

def PrintOdd(Val1):
    for i in range(1,Val1):
        if(i % 2 != 0):
            print(i,end = " ")
        
    print()

def main():
    iValue = int(input("Enter number : "))

    if(iValue <= 0):
        iValue = -iValue

    PrintOdd(iValue)


if __name__ == "__main__":
    main()
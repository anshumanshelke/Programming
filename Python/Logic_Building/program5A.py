# 1 .Write a program which accept number from user and print that number of $ & *
# on screen.
# Input :5
# Output :$ * $ * $ * $ * $ * 
# Input :3
# Output :$ * $ * $ *
# Input :-3
# Output :$ * $ * $ * 

def Pattern(Val1):
    for i in range(0,Val1):
        print("$ * ",end = " ")
        
    print()

def main():
    iValue = int(input("Enter number : "))

    if(iValue <= 0):
        iValue = -iValue

    Pattern(iValue)


if __name__ == "__main__":
    main()
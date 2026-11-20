# 2. Write a program which accept number from user and 
# print factors of that number.
# Input :24
# Output: 1 2 4 6 8 12


def DisplayFactors(Val1):
    No = ((Val1//2)+1)

    for i in range(1,No):
        if(((Val1 % i) == 0)):
            print(i,end = " ")

def main():
    iValue = int(input("Enter number : "))

    if(iValue <= 0):
        print("Invalid input, enterred number should be greater than ZERO")

    DisplayFactors(iValue)


if __name__ == "__main__":
    main()

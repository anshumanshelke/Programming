# 2.Write a program which accept number from user and display its factors in
# decreasing order.
# Input :12
# Output: 6  4  3  2  1


def DisplayRevFactors(Val1):
    No = ((Val1//2)+1)

    for i in range(No,0,-1):
        if(((Val1 % i) == 0)):
            print(i,end = " ")

def main():
    iValue = int(input("Enter number : "))

    if(iValue <= 0):
        print("Invalid input, enterred number should be greater than ZERO")

    DisplayRevFactors(iValue)


if __name__ == "__main__":
    main()
  
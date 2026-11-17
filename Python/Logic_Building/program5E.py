# 5. Write a program which accept N and print first 5 multiples of N.
# Input :4
# Output :4
# 8
# 12
# 16
# 20

def MultipleDisplay(Val1):
    for i in range(1,6):
        print(i*Val1,end = " ")
        
    print()

def main():
    iValue = int(input("Enter number : "))

    if(iValue <= 0):
        iValue = -iValue

    MultipleDisplay(iValue)


if __name__ == "__main__":
    main()
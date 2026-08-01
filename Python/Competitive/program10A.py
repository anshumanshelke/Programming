##################################################################
# #1. Write a program which accepts one number and prints multiplication table of that number.
# Input: 4
# Output:
# 4 8 12 16 20 24 28 32 36 40
##################################################################

def TableDisplay(No):
    for i in range(1,11,1):
        print(i*No)

def main():
    print("Enter number : ")
    Value = int(input())
    TableDisplay(Value)


if __name__ == "__main__":
    main()
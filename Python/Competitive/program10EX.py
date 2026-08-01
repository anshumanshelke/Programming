#######################################################
# Write a program which accepts one number 
# and prints all odd numbers till that number.
#######################################################

def PrintOdd(No):
    for i in range(1,(No+1)):
        if(i%2 != 0):
            print(i)

def main():
    print("Enter number : ")
    Value = int(input())
    PrintOdd(Value)


if __name__ == "__main__":
    main()
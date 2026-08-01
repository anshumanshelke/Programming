#######################################################
# Write a program which accepts one number 
# and prints all odd numbers till that number.
#######################################################

def PrintEven(No):
    for i in range(1,(No+1),2):
        print(i)

def main():
    print("Enter number : ")
    Value = int(input())
    PrintEven(Value)


if __name__ == "__main__":
    main()
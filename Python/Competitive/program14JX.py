# Write a lambda function which accepts three numbers
# and returns largest number.

def MaxOfThree(No1, No2, No3):
    if(No1>No2 and No1>No3):
        return No1
    elif(No2>No3):
        return No2
    else:
        return No3


def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))
    Value3 = int(input("Enter third number : "))

    print(MaxOfThree(Value1,Value2,Value3))

if __name__ == "__main__":
    main()
# Write a lambda function which accepts two numbers 
# and returns maximum number.

def max(No1, No2):
    if(No1 > No2):
        return No1
    return No2

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter Second number : "))
    print(f"maximum of {Value1, Value2} is {max(Value1, Value2)}")

if __name__ == "__main__":
    main()
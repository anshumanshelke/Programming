# Write a lambda function which accepts two numbers 
# and returns maximum number.

max = lambda No1, No2: No1 if No1 > No2 else No2

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter Second number : "))
    print(f"maximum of {Value1, Value2} is {max(Value1, Value2)}")

if __name__ == "__main__":
    main()
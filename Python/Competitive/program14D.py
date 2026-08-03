# Write a lambda function which accepts two numbers 
# and returns minimum number.

min = lambda No1, No2 : No1 if No1 < No2 else No2

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    print(f"between {Value1, Value2}, {min(Value1,Value2)} is minimum")


if __name__ == "__main__":
    main()
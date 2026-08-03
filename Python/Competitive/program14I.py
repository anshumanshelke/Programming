# Write a lambda function which accepts two numbers
# and returns multiplication.

add = lambda No1, No2 : No1 * No2

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    print(f"Product of {Value1, Value2}, is {add(Value1,Value2)}")


if __name__ == "__main__":
    main()
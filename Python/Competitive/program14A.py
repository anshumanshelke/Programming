# Write a lambda function which accepts one number 
# and returns square of that number.

square = lambda No : No * No

def main():
    Value = int(input("Enter number :"))
    print(f"square of {Value} is {square(Value)}")

if __name__ == "__main__":
    main()
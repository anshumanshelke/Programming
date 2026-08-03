# Write a lambda function which accepts one number 
# and returns cube of that number.

cube = lambda No : No * No * No

def main():
    Value = int(input("Enter number : "))
    print(f"square of {Value} is {cube(Value)}")

if __name__ == "__main__":
    main()
# Write a lambda function which accepts one number 
# and returns True if number is even otherwise False.

chkeven = lambda No1 : True if No1 % 2 == 0 else False

def main():
    Value = int(input("Enter number : "))

    print(f"It's {chkeven(Value)} that {Value} is Even")


if __name__ == "__main__":
    main()
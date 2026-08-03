# Write a lambda function which accepts one number 
# and returns True if divisible by 5.

ChkDivBy5 = lambda No1 : True if No1 % 5 == 0 else False

def main():
    Value = int(input("Enter number : "))

    print(f"It's {ChkDivBy5(Value)} that {Value} is Divisible by 5")


if __name__ == "__main__":
    main()
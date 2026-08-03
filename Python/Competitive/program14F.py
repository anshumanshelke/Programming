# Write a lambda function which accepts one number 
# and returns True if number is ODD otherwise False.

chkodd = lambda No1 : True if No1 % 2 != 0 else False

def main():
    Value = int(input("Enter number : "))

    print(f"It's {chkodd(Value)} that {Value} is Odd")


if __name__ == "__main__":
    main()
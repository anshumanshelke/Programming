# 3. Write a program which contains one function named as Add()
# which accepts two numbers from user and
# return addition of that two numbers.
# Input : 11 5 Output : 16

def Addition(No1, No2):
    Ans = No1 + No2
    return Ans


def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter Second number : "))
    Ret = int(Addition(Value1, Value2))
    print(f"Addition of {Value1} + {Value2} = {Ret}")

if __name__ == "__main__":
    main()
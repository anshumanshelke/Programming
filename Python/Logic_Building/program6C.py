# 3.Write a program to find factorial of given Factorial.
# Input : 5
# Output : 120 (5 * 4 * 3 * 2 * 1)
# Input : -5
# Output : 120 (5 * 4 * 3 * 2 * 1)
# Input : 4
# Output : 24 (4 * 3 * 2 * 1)

def Factorial(Val):
    Pro = 1
    for i in range(1,Val+1):
        Pro = i* Pro
    
    return Pro

def main():
    Value = int(input("Enter Number : "))

    if(Value < 0):
        Value = -Value

    Result = Factorial(Value)

    print(Result)

if __name__ == "__main__":
    main()
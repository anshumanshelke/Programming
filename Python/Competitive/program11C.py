#####################################################
# 3. Write a program which accepts one number 
# and prints sum of digits.
# Input: 123
# Output: 6
#####################################################

def SumOfDigits(No):
    Sum = 0 
    while(No >= 1): 
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():
    print("Enter number : ")
    Value = int(input())
    Ret = SumOfDigits(Value)

    print(Ret)

if __name__ == "__main__":
    main()
#####################################################
# 2.Write a program which accepts one number 
# and prints count of digits in that number.
# Input: 7521
# Output: 4
#####################################################

def CountDigits(No):
    Count = 0 
    while(No > 1): 
        Count = Count + 1
        No = No // 10

    return Count

def main():
    print("Enter number : ")
    Value = int(input())
    Ret = CountDigits(Value)

    print(Ret)

if __name__ == "__main__":
    main()
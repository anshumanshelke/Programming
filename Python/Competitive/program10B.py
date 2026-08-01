###################################################
# 2. Write a program which accepts one number 
# and prints sum of first N natural numbers.
# Input: 5
# Output: 15
###################################################

def SumOfAllTillValue(No):
    Sum = 0
    for i in range((No+1)):
        Sum = Sum + i

    return Sum

def main():
    print("Enter number : ")
    Value = int(input())
    Ret = SumOfAllTillValue(Value)

    print(Ret)

if __name__ == "__main__":
    main()
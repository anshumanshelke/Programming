# 2.Write a program which accept number from user and return the count of odd
# digits.
# Input :
# Output :2395
# 3
# Input :
# Output :1018
# 2
# Input :
# Output :-1018
# 2
# Input :
# Output :8462
# 0
# #include<stdio.h>
# int CountOdd(int iNo)
# {
# // Logic
# }
# int main()
# {
# int iValue = 0;
# int iRet = 0;
# printf(" Enter number");
# scanf(" % d ",&iValue);
# iRet = CountOdd(iValue);
# printf("%d",iRet);
# return 0;
# }

def CountEven(No):
    Count = int(0)
    while(No != 0):
        Dig = No % 10
        if(Dig % 2 != 0):
            Count = Count + 1
        No = No // 10

    return Count

def main():
    Value = int(input("Enter the number :"))

    if(Value < 0):
        Value = -Value

    Result = CountEven(Value)

    print(Result)

if __name__ == "__main__":
    main()
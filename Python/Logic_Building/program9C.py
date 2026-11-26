# 3.Write a program which accept number from user and return the count of digits in
# between 3 and 7.
# Input :
# Output :1018
# 0
# Input :4521
# Output :2
# Input :
# Output :9922
# 0
# #include<stdio.h>
# int CountRange(int iNo)
# {
# // Logic
# }
# int main()
# {
# int iValue = 0;
# int iRet = 0;
# printf("Enter number");
# scanf("%d ",&iValue);
# iRet = CountRange(iValue);
# printf("%d",iRet);
# return 0;
# }

def CountRange(No):
    Count = int(0)
    while(No != 0):
        Dig = No % 10
        for i in range(4,7):
            if(Dig == i):
                Count = Count + 1
        No = No // 10

    return Count

def main():
    Value = int(input("Enter the number :"))

    if(Value < 0):
        Value = -Value

    Result = CountRange(Value)

    print(Result)

if __name__ == "__main__":
    main()
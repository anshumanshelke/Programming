# 4.Write a program which accept number from user and return multiplication of all
# digits.
# Input :
# Output :2395
# 270
# Input :
# Output :1018
# 8
# Input :
# Output :9440
# 144
# Input :
# Output :922432
# 864
# #include<stdio.h>
# int MultDigits(int iNo)
# {
# // Logic
# }
# int main()
# {
# int iValue = 0;
# int iRet = 0;
# printf(" Enter number "  );
# scanf("%d",&iValue);
# iRet = MultDigits(iValue);
# printf("%d",iRet);
# return 0;
# }

def MulDigit(No):
    Pro = int(1)

    while(No != 0):
        Dig = No % 10
        No = No // 10

        if(Dig == 0):
            continue
        Pro = Pro * Dig

    return Pro

def main():
    Value = int(input("Enter the number :"))

    if(Value < 0):
        Value = -Value

    Result = MulDigit(Value)

    print(Result)

if __name__ == "__main__":
    main()
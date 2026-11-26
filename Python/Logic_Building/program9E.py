# 5.Write a program which accept number from user and return difference between
# summation of even digits and summation of odd digits.
# Input :
# Output :2395
# -15 (2 - 17)
# Input :
# Output :1018
# 6
# (8 - 2)
# Input :
# Output :8440
# 16 (16 - 0)
# Input :
# Output :5733
# -18 (0 - 18)
# #include<stdio.h>
# int CountDiff(int iNo)
# {
# // Logic
# }
# int main()
# {
# int iValue = 0;
# int iRet = 0;
# printf(" Enter number");
# scanf("%d " ,&iValue);
# iRet = CountDiff(iValue);
# printf("%d",iRet);
# return 0;
# }

def CountDiff(No):

    OddSum = int(0)
    EvenSum = int(0)

    Diff = int(0)

    while(No != 0):
        Dig = No % 10
        No = No // 10

        if(Dig % 2 == 0):
            EvenSum = EvenSum + Dig

        else:
            OddSum = OddSum + Dig

    Diff = EvenSum - OddSum

    return Diff

def main():
    Value = int(input("Enter the number :"))

    if(Value < 0):
        Value = -Value

    Result = CountDiff(Value)

    print(Result)

if __name__ == "__main__":
    main()
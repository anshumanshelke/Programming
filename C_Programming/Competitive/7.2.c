#include<stdio.h>

int DollarToINR(int iNo)
{
    int iConvertedAmount = 0;
    iConvertedAmount = (iNo * 70);

    return iConvertedAmount;

}

int main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter Number of USD ");
    scanf("%d",&iValue);

    iRet = DollarToINR(iValue);

    printf("Value in INR is %d",iRet);

    return 0;
}
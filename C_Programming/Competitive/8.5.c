#include<stdio.h>

double SquareMeter(int iNo)
{
    double dSqFeet = 0.0;
    dSqFeet = (iNo * 0.0929);
    return dSqFeet;
}

int main()
{
    int iValue = 0;
    double dRet = 0.0;

    printf("Enter Area in Square Feet\n");
    scanf("%d",&iValue);

    dRet = SquareMeter(iValue);

    printf("%lf",dRet);

    return 0;
}
#include<stdio.h>

int FuncEvenSum(int iNo)
{
    int iUnitPlace = 0;
    int iEvSum = 0;

    while(iNo != 0)
    {
        iUnitPlace = iNo % 10;
        if(iUnitPlace % 2 == 0)
        {
            iEvSum = iEvSum + iUnitPlace;
        }
        iNo = iNo / 10;
    }

    return iEvSum ;
}

int FuncOddSum(int iNo)
{
    int iUnitPlace = 0;
    int iOdSum = 0;

    while(iNo != 0)
    {
        iUnitPlace = iNo % 10;
        if(iUnitPlace % 2 != 0)
        {
            iOdSum = iOdSum + iUnitPlace;
        }
        iNo = iNo / 10;
    }

    return iOdSum;
}

int CountDiff(int iNo)
{
    int iFinalEvenSum = 0;
    int iFinalOddSum = 0 ;
    int iDiffBWSums = 0;

    iFinalEvenSum = FuncEvenSum(iNo);
    iFinalOddSum = FuncOddSum(iNo);

    iDiffBWSums = (iFinalEvenSum - iFinalOddSum);

    return iDiffBWSums;

}

int main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter Number\n");
    scanf("%d",&iValue);

    iRet = CountDiff(iValue);

    printf("%d",iRet);

    return 0;
}
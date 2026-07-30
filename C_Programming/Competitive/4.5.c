#include <stdio.h>

int SumNonFact(int iNo)
{
    int iCnt = 0;
    int iSum = 0;

    for(iCnt = 1 ; iCnt < iNo ; iCnt++)
    {
        if((iNo % iCnt) != 0)
        {
            iSum = iSum + iCnt;
        }
    }

    return iSum;

}


int SumFactor(int iNo)
{
    int iCnt = 0;
    int iSum = 0;

    for(iCnt = 1 ; iCnt < iNo ; iCnt++)
    {
        if((iNo % iCnt) == 0)
        {
            iSum = iSum + iCnt;
        }
    }

    return iSum;    
}


int FactDiff(int iNo)
{

    int iFactorSum = 0;
    int iNonFactorSum = 0;
    int iDiff = 0;

    iFactorSum = SumFactor(iNo);
    iNonFactorSum = SumNonFact(iNo);

    iDiff = iFactorSum - iNonFactorSum;

}

int main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter Number ");
    scanf("%d",&iValue);

    iRet = FactDiff(iValue);

    printf("%d", iRet);

    return 0;
} 
#include<stdio.h>

int OddFactorial(int iNo)
{
    int iCnt = 0;
    int iFactorial = 1;

    if(iNo < 0)
    {
        iNo  = (iNo * -1);
    }

    for(iCnt = 1; iCnt <= iNo ; iCnt++)
    {
        if(iCnt % 2 != 0)
        {
            iFactorial = iFactorial * iCnt;
        }
    }
    return iFactorial;

}


int EvenFactorial(int iNo)
{
    int iCnt = 0;
    int iFactorial = 1;

    if(iNo < 0)
    {
        iNo  = (iNo * -1);
    }

    for(iCnt = 1; iCnt <= iNo ; iCnt++)
    {
        if(iCnt % 2 == 0)
        {
            iFactorial = iFactorial * iCnt;
        }
    }

    return iFactorial;
}


int FactorialDiff(int iNo)
{
    int iEvenFact = 0;
    int iOddFact = 0; 

    iEvenFact = EvenFactorial(iNo);
    iOddFact = OddFactorial(iNo);

    return (iEvenFact - iOddFact);

}



int main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter Number ");
    scanf("%d",&iValue);

    iRet = FactorialDiff(iValue);

    printf("Factorial Difference is %d",iRet);

    return 0;
}
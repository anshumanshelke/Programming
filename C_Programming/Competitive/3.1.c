#include<stdio.h>

void PrintEven(int iNo)
{
    int iCnt = 0;
    int iEvenCnt = 0;

    if(iNo <= 0)
    {
        return ;
    }

    for(iCnt = 1; iCnt <= (2 * iNo) ; iCnt++)
    {
        iEvenCnt++;

        if(iEvenCnt % 2 == 0)
        {
            printf("%d ",iCnt);
        }


    }
}

int main()
{
    int iValue = 0;
    printf("Enter Number \n");
    scanf("%d", &iValue);

    PrintEven(iValue);

    return 0;
}
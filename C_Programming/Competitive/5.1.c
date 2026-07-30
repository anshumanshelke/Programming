#include<stdio.h>

void Pattern(int iNo)
{
    if(iNo < 0)
    {
        iNo = (iNo * -1);
    }

    int iCnt = 0;

    for(iCnt = 1; iCnt <= iNo ; iCnt++)
    {
        printf("$ * ");
    }
}

int main()
{
    int iValue = 0;
    printf("Enter Number ");
    scanf("%d",&iValue);

    Pattern(iValue);

    return 0;
}
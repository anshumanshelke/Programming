#include<stdio.h>

int CountRange(int iNo)
{
    int iUnitPlace = 0;
    int iCnt = 0;

    while(iNo != 0)
    {
        iUnitPlace = iNo % 10;
        if(iUnitPlace >= 3 && iUnitPlace <= 7)
        {
            iCnt++;
        }
        iNo = iNo / 10;
    }

    return iCnt;

}

int main()
{
    int iRet = 0;
    int iValue = 0;

    printf("Entern Number\n");
    scanf("%d",&iValue);

    iRet = CountRange(iValue);

    printf("%d", iRet);

    return 0;
}
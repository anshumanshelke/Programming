#include<stdio.h>

int MultDigits(int iNo)
{
    int iUnitPlace = 0;
    int iPro = 1;

    while(iNo != 0)
    {
        iUnitPlace = iNo % 10;
        if(iUnitPlace > 0)
        {
            iPro = iPro * iUnitPlace;
        }
        iNo = iNo / 10;
    }

    return iPro;

}

int main()
{
    int iRet = 0;
    int iValue = 0;

    printf("Entern Number\n");
    scanf("%d",&iValue);

    iRet = MultDigits(iValue);

    printf("%d", iRet);

    return 0;
}
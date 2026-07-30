#include<stdio.h>

void Table(int iNo)
{
    int iCnt = 0;
    int iProduct = 0;

    if(iNo < 0)
    {
        iNo = (iNo * (-1));
    }

    for(iCnt = 1; iCnt <= 10 ; iCnt++)
    {
        iProduct = iCnt * iNo;
        printf("%d ",iProduct);
        
    }

}

int main()
{
    int iValue = 0;

    printf("Enter Number\n");
    scanf("%d",&iValue);

    Table(iValue);

    return 0;
}
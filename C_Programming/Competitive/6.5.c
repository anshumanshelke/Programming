#include<stdio.h>

void TableRev(int iNo)
{
    int iCnt = 0;
    int iProduct = 0;

    if(iNo < 0)
    {
        iNo = (iNo * (-1));
    }

    // iCnt = 10;
    for(iCnt = 10; iCnt > 0 ; iCnt--)
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

    TableRev(iValue);

    return 0;
}
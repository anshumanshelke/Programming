#include<stdio.h>

int Factorial(int iNo)
{

    if(iNo < 0)
    {
        iNo = (iNo * (-1));
    }

    int iProduct = 1;   
    int iCnt = 0;

    for(iCnt = 1; iCnt <= iNo ; iCnt++)
    {
        iProduct = iProduct * iCnt;
    }

    return iProduct;

}

int main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter Number\n");
    scanf("%d",&iValue);

    iRet = Factorial(iValue);

    printf("Factorial of number is %d",iRet);

    return 0;
}

    /*iProduct is Initialsed to 1- bcoz when product will occur-
    It will start from 1- if Zero- then all factorials 
    will be Zero*/
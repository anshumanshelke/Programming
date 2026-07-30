#include<stdio.h>

void NumberX(int iNo)
{
    if(iNo < 50)
    {
        printf("SMALL\n");
    }

    else if((iNo >= 50 && iNo <= 100))
    {
        printf("MEDIUM\n");
    }

    else
    {
        printf("LARGE\n");
    }

}

int main()
{
    int iValue = 0;

    printf("Enter Number\n");
    scanf("%d",&iValue);

    NumberX(iValue);

    return 0;
}
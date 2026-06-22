#include<stdio.h>

#define TRUE 1
#define FALSE 0

typedef int BOOL;
BOOL ChkCapital(char ch)
{
    if(ch>=65 && ch<=90)   //AScii values
    {                     // 65=A,90=Z
        return TRUE;
    }
    else
    {
        return FALSE;
    }
}

int main()
{
    char cValue='\0';
    BOOL bRet=FALSE;

    printf("Enter the character:");
    scanf("%c",&cValue);

    bRet=ChkCapital(cValue);

    if (bRet==TRUE)
    {
        printf("It is Capital Character");
    }
    else
    {
        printf("It is not Capital Character");
    }

    return 0;
}
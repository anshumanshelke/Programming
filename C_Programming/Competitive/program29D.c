#include<stdio.h>

#define TRUE 1
#define FALSE 0

typedef int BOOL;
BOOL ChkSmall(char ch)
{
    if(ch>=97 && ch<=122)   //AScii values
    {                       // 97=a,122=z
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

    bRet=ChkSmall(cValue);

    if (bRet==TRUE)
    {
        printf("It is a Small Case Character");
    }
    else
    {
        printf("It is not a Small Case Character");
    }

    return 0;
}
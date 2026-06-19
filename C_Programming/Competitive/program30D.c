///////////////////////////////////////////////////////////////////
//
// Accept Character from user and check whether it is special symbol
// or not (!, @, #, $, %, ^, &, *).
// Input : %
// Output : TRUE
// Input : d
// Output : FALSE
//
////////////////////////////////////////////////////////////////////

#include<stdio.h>

#define TRUE 1
#define FALSE 0

typedef int BOOL;

BOOL ChkCapital(char ch)
{
    BOOL flag = FALSE;

    if(((ch >= 33) && (ch <= 47)) || ((ch >= 58) && (ch <= 64))) 
    {
        flag = TRUE;
    }

    return flag;

}

int main()
{
    char cValue = '\0';
    BOOL bRet = FALSE;

    printf("Enter the character :\n");
    scanf("%c",&cValue);

    bRet = ChkCapital(cValue);

    if(bRet == TRUE)
    {
        printf("TRUE");
    }

    else
    {
        printf("FALSE");
    }
    return 0;
}

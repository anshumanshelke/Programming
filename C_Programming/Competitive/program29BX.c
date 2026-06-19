/////////////////////////////////////////////////
//
// Accept Character from user and check whether it is capital or not
// (A-Z).
// Input : F
// Output : TRUE
// Input : d
// Output : FALSE
//
/////////////////////////////////////////////////
#include<stdio.h>

#define TRUE 1
#define FALSE 0

typedef int BOOL;

BOOL ChkCapital(char ch)
{
    BOOL flag = FALSE;

    if((ch >= 'A' && ch <= 'Z')) 
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

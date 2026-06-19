/////////////////////////////////////////////////
//
// Accept Character from user and check whether it is alphabet or not
// (A-Z a-z).
// Input : F
// Output : TRUE
// Input : &
// Output : FALSE
//
/////////////////////////////////////////////////
#include<stdio.h>

#define TRUE 1
#define FALSE 0

typedef int BOOL;

BOOL ChkAlpha(char ch)
{
    BOOL flag = FALSE;

    if((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) 
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

    bRet = ChkAlpha(cValue);

    if(bRet == TRUE)
    {
        printf("It is Character");
    }

    else
    {
        printf("It is not a Character");
    }
    return 0;
}

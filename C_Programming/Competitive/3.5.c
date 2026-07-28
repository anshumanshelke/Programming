#include<stdio.h>

typedef int BOOL;

#define TRUE 1
#define FALSE 0

BOOL ChkVowel(char cLtr)
{
    if((cLtr =='A' || cLtr =='E' || cLtr=='I' || cLtr =='O' || cLtr=='U') || 
        (cLtr =='a' || cLtr =='e' || cLtr=='i' || cLtr =='o' || cLtr=='u'))
        {
            return TRUE;
        }

    else
    {
        return FALSE;
    }
}


int main()
{

    char cValue = '\0';
    BOOL bRet = FALSE;

    printf("Enter Character\n");

    scanf("%c", &cValue);

    bRet = ChkVowel(cValue);

    if(bRet == TRUE)
    {
        printf("It is Vowel");
    }

    else
    {
        printf("It is NOT Vowel");
    }

    return 0;
}
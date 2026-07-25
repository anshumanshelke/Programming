////////////////////////////////////////////////////////////////
//
// Write a program which accept string from user and
// accept one character. Check whether that character 
// is present in string or not.
//     Input:
//     "Marvellous Multi OS"
//     e
//     Output:
//     TRUE
//     Input:
//     "Marvellous Multi OS"
//     W
//     Output:
//     FALSE
//
////////////////////////////////////////////////////////////////

#include<stdio.h>

#define TRUE 1
#define FALSE 0

typedef int BOOL;

BOOL ChkChar(char *str, char ch)
{
    BOOL flag = FALSE;
    while(*str != '\0')
    {
        if(*str == ch)
        {
            flag = TRUE;
        }
        str++;
    }
    return flag;
}

int main()
{
    char arr[20];
    char cValue;
    BOOL bRet =  FALSE;

    printf("Enter String : \n");
    scanf("%[^'\n']s", arr);

    printf("Enter the character\n");
    scanf(" %c", &cValue);

    bRet = ChkChar(arr, cValue);

    if(bRet == TRUE)
    {
        printf("Character Found\n");
    }

    else
    {
        printf("Character NOT Found\n");
    }

    return 0;

}
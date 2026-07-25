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
#include<stdbool.h>

// #define TRUE 1
// #define FALSE 0

// typedef int BOOL

bool ChkChar(char *str, char ch)
{
    bool flag = false;
    while(*str != '\0')
    {
        if(*str == ch)
        {
            return true;
        }
        str++;
    }
    return false;
}

int main()
{
    char arr[20];
    char cValue;
    bool bRet =  false;

    printf("Enter String : \n");
    scanf("%[^'\n']s", arr);

    printf("Enter the character\n");
    scanf(" %c", &cValue);

    bRet = ChkChar(arr, cValue);

    if(bRet == true)
    {
        printf("Character Found\n");
    }

    else
    {
        printf("Character NOT Found\n");
    }

    return 0;

}
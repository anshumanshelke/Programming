////////////////////////////////////////////////////////////////
//
// Write a program which accept string from user and
// accept one character. Return index of last occurrence
// of that character.
//     Input :
//     "Marvellous Multi OS"
//     M
//     Output:
//     11
//     Input :
//     "Marvellous Multi OS"
//     W
//     Output :
//     -1
//     Input:
//     "Marvellous Multi OS"
//     e
//     Output:
//     4

5. Write a program which accept string from user reverse that string in place.
Input:
"abcd"
Output :
"dcba"
Input:
"abba"
Output :
"abba"

//
////////////////////////////////////////////////////////////////

#include<stdio.h>
#include<string.h>

int CountChar(char *str, char ch)
{
    int iCnt = 0 ;
    int LenOfStr = strlen(str);
    int iPos = -1;

    while(*str != '\0')
    {
        if(*str == ch)
        {
            iPos = iCnt;
        }     
        
        str++;
        iCnt++;
    }


   return iPos;
}

int main()
{
    char arr[20];
    char cValue;
    int iRet =  0;

    printf("Enter String : \n");
    scanf("%[^'\n']s", arr);

    printf("Enter the character\n");
    scanf(" %c", &cValue);

    iRet = CountChar(arr, cValue);

    printf("%d\n",iRet);
    
    return 0;

}
////////////////////////////////////////////////////////////////
//
// 3. Write a program which accept string from user and
//  accept one character. Return index of first occurrence
//  of that character.
//     Input :
//     "Marvellous Multi OS"
//     M
//     Output:
//     0
//     Input :
//     "Marvellous Multi OS"
//     W
//     Output:
//     -1
//     Input:
//     "Marvellous Multi OS"
//     e
//     Output:
//     4
//
////////////////////////////////////////////////////////////////

#include<stdio.h>
#include<string.h>

int CountChar(char *str, char ch)
{
    int iCnt = 0 ;
    int LenOfStr = strlen(str);
    
    while(*str != '\0')
    {
        if(*str == ch)
        {
            break;
        }     
        
        str++;
        iCnt++;
    }

    if(LenOfStr == iCnt)
    {
        iCnt = -1;
    }

   return iCnt;
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
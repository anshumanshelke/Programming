/////////////////////////////////////////////////////////////////////////
//
// 4. Write a program which accept string from user and 
// copy small characters of that string into another string.
//     Input:
//     "Marvellous multi OS"
//     Output:
//     "arvellous multi"
//
/////////////////////////////////////////////////////////////////////////

#include<stdio.h>

void StrCpyX(char *src, char *dest)
{
    if(*src == '\0')
    {
        *dest = '\0';
        return;
    }
    
    while(*src != '\0')
    {
        if(((*src >= 'a') && (*src <= 'z'))|| (*src == ' '))
        {
            *dest = *src;
            dest++;
        }
        src++;
    }
}

int main()
{
    char arr[30] = "Marvellous multi OS";
    char brr[30] = {'\0'};   //Empty Sring

    StrCpyX(arr, brr);

    printf("%s", brr);  //Marvellous

    return 0;
}
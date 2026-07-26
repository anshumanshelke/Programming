/////////////////////////////////////////////////////////////////////////
//
// Write a program which accept string from user
// and copy capital characters of that string into another string.
// Input:
//     "Marvellous Multi OS"
//     Output:
//     "MMOS"
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
        if((*src >= 'A') && (*src <= 'Z'))
        {
            *dest = *src;
            dest++;
        }
        src++;
    }
}

int main()
{
    char arr[30] = "Marvellous Multi OS";
    char brr[30] = {'\0'};   //Empty Sring

    StrCpyX(arr, brr);

    printf("%s", brr);  //Marvellous

    return 0;
}
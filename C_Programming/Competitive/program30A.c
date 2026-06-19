///////////////////////////////////////////////////////////////////
//
// Write a program which displays ASCII table. Table contains symbol,
// Decimal, Hexadecimal and Octal representation of every member from
// 0 to 255.
//
////////////////////////////////////////////////////////////////////
#include<stdio.h>

void DisplayASCII()
{
    int iCnt = 0;
    char ch = '\0';
    for(iCnt = 0, ch = 0; iCnt <= 255 ; iCnt++, ch++)
    {
        printf("%d : %c\n",iCnt, ch);
    }
}

int main()
{
    DisplayASCII();
    return 0;
}

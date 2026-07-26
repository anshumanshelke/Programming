///////////////////////////////////////////////////////////////////////
//
// Write a program which accept one number from user and
//  on its first 4 bits. Return modified number.
// Input:
// 73
// Output:
// 79
//
///////////////////////////////////////////////////////////////////////

#include <stdio.h>

typedef unsigned int UINT;

UINT OffBit(UINT iNo)
{
    UINT iMask = 0;
    UINT iAns = 0;

    iMask = 0x4f;

    iAns = iMask | iNo;

    return iAns;
}

int main()
{
    int iValue = 0;
    UINT iRet = 0;

    printf("Enter Value :\n");
    scanf("%d",&iValue);

    iRet = OffBit(iValue);

    printf("%u",iRet);

    return 0;
}
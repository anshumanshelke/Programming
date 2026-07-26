///////////////////////////////////////////////////////////////////////
//
// 1. Write a program which accept one number from user and 
// off 7th bit of that number if it is on. Return modified number.
// Input: 79
// Output: 15
//
///////////////////////////////////////////////////////////////////////

#include <stdio.h>

typedef unsigned int UINT;

UINT OffBit(UINT iNo)
{
    //79 = 0100 1111
    UINT iMask = 0;
    //iMask = 64 (Binary -> Decimal)
    UINT iAns = 0;
    iMask = 0x40;

    iAns = iMask ^ iNo;

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
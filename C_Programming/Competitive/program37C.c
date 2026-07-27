///////////////////////////////////////////////////////////////////////
//
// Write a program which accept one number and position from user and
//  on that bit. Return modified number.
//     Input:
//     10
//     3
//     Output:
//     14
//
///////////////////////////////////////////////////////////////////////

#include <stdio.h>

typedef unsigned int UINT;

UINT OnBit(UINT iNo, UINT iPos)
{
    UINT iMask = 0x1;
    UINT iAns = 0;

    if(iPos < 1 || iPos >32)
    {
        printf("Invalid Bit position\n");
        return iNo;
    }

    iMask = iMask << (iPos -1) ;

    iAns = iMask ^ iNo;

    return iAns;
}

int main()
{
    int iValue = 0;
    int iLocation = 0;
    UINT iRet = 0;

    printf("Enter Value :\n");
    scanf("%d",&iValue);

    printf("Enter Location :\n");
    scanf("%d",&iLocation);

    iRet = OnBit(iValue, iLocation);

    printf("%d\n",iRet);

    return 0;
}
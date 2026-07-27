///////////////////////////////////////////////////////////////////////
//
// Write a program which accept one number and 
// position from user and check whether bit at that position is
//  on or off. If bit is ON return TURE otherwise return FALSE.
//     Input:
//     10
//     2
//     Output:
//     TRUE
//
///////////////////////////////////////////////////////////////////////

#include <stdio.h>

typedef int BOOL;
typedef unsigned int UINT;

#define TRUE 1
#define FALSE 0

BOOL OffBit(UINT iNo, UINT iPos)
{
    UINT iMask = 0x1;
    UINT iAns = 0;

    BOOL iResult = FALSE;

    if(iPos < 1 || iPos >32)
    {
        printf("Invalid Bit position\n");
        return iNo;
    }

    iMask = iMask << (iPos -1) ;

    iAns = iMask & iNo;

    if(iMask == iAns)
    {
        iResult = TRUE;
    }

    return iResult;
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

    iRet = OffBit(iValue, iLocation);

    if(iRet == TRUE)
    {
        printf("TRUE\n");
    }

    else{
        printf("FALSE\n");
    }

    return 0;
}
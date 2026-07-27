///////////////////////////////////////////////////////////////////////
//
// Write a program which accept one number from user and 
// toggle contents of first and last nibble of the number.
// Return modified number. (Nibble is a group of four bits)
//
// Input : -1717986919
// Output : 0
// Input : -640041573
// Output : 1077945346
//
///////////////////////////////////////////////////////////////////////

#include <stdio.h>

typedef unsigned int UINT;

UINT ToggleBit(UINT iNo)
{
    UINT iMask = 0;
    UINT iAns = 0;

    iMask = 0x99999999;

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

    iRet = ToggleBit(iValue);

    printf("%d\n",iRet);

    return 0;
}
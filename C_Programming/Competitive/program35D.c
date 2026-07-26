////////////////////////////////////////////////////////////
//
// Write a program which checks whether 
// 7th & 8th & 9th bit is On or OFF.
//
////////////////////////////////////////////////////////////

#include<stdio.h>

typedef int BOOL;
typedef unsigned int UINT;

#define TRUE 1
#define FALSE 0

BOOL ChkBit(UINT iNo)
{
    UINT iMask = 0x1c0;
    UINT iAns = 0;

    iAns = iNo & iMask;

    if(iAns == iMask)
    {
        return TRUE;
    }

    else
    {
        return FALSE;
    }

}

int main()
{
    int iValue = 0;
    printf("Enter No.: \n");
    scanf("%d",&iValue);
    BOOL bRet = FALSE;

    bRet = ChkBit(iValue);

    if(bRet == TRUE)
    {
        printf("BIT is ON");
    }

    else
    {
        printf("BIT is OFF");
    }

    return 0;
}

/*
5. Write a program which checks whether first and last bit is On or OFF. 
First bit means bit number 1 and last bit means bit number 32.
*/
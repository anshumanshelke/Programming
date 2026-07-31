/*Write a program which accept distance in kilometre and convert it into meter. (1
kilometre = 1000 Meter)
Input : 5
Output : 5000
Input : 12
Output : 12000
*/

#include<stdio.h>

int KMtoMeter(int iNo)
{

    int iConversion = 0;
    iConversion = (iNo * 1000);

    return iConversion;

}

int main()
    {
            
    int iValue = 0, iRet = 0;

    printf("Enter distance in Kms\n");
    scanf("%d",&iValue);

    iRet = KMtoMeter(iValue);

    printf("%d Kms are %d Meters",iValue,iRet);
    return 0;
    }
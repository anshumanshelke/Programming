//////////////////////////////////////////////////////////////
//
//Write a program which accept radius of circle from user and calculate its area.
//Consider value of PI as 3.14. (Area = PI * Radius * Radius)
//
//Input : 5.3
//Output : 88.2026
//Input : 10.4
//Output : 339.6224
//
//////////////////////////////////////////////////////////////

#include<stdio.h>

double RectArea(float fWidth, float fHeight)
{

    double iArea = 0.0;

    iArea = fWidth * fHeight;

    return iArea;

}

int main()
{
    float fValue1 = 0.0, fValue2 = 0.0;
    double dRet = 0.0;

    printf("Enter Width : ");
    scanf("%f",&fValue1);

    printf("Enter height : ");
    scanf("%f",&fValue2);    

    dRet = RectArea(fValue1, fValue2);

    printf("Area of Rectangle is %lf", dRet);

    return 0;
}
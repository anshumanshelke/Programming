#include<stdio.h>

double FhtoCs(float fTemp)
{
    double dCelTemp = 1.0;
    dCelTemp = ((fTemp - 32) * (5/9));

    return dCelTemp;
}

int main()
{

    float fValue = 0.0f;
    double dRet = 0.0;

    printf("Enter Temperatur in Fahrenheit\n");
    scanf("%f",&fValue);

    dRet = FhtoCs(fValue);

    printf("Given temperature in Fahrenheit is %lf in Celcius\n",dRet);

    return 0;
}
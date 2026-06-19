////////////////////////////////////////////////////////////////////////////////
//
// PS - Accept number of rows and number of columns from user and display below
// pattern.
//
// Input :
// iRow = 6 iCol = 6
// Output : 
//Output : 
// * * * * * *
// * # # # * *
// * # # * $ *
// * # * $ $ *
// * * $ $ $ *
// * * * * * *
//
////////////////////////////////////////////////////////////////////////////////

#include<stdio.h>

void Pattern(int iRow, int iCol)
{
    if(iRow != iCol)
    {
        printf("INVALID INPUT\n");
        printf("Kindly insert same number of Rows and Columns\n");
        return;
    }

    int i = 0, j = 0, iSum = 0;

    for(i = 1; i <= iRow; i++)
    {
        for(j= iCol ; j >= 1 ; j--)
            {
                if ((i==j)||(i == iRow) || (i==1) || (j==1) || (j==iCol))
                {
                    printf("*\t");
                }

                else if(i<j)
                {
                    printf("#\t");
                }

                else
                {
                    printf("@\t");
                }
            }
        printf("\n");
    }
}

int main()
{
    int iValue1 = 0, iValue2 = 0;

    printf("Enter number of rows and columns\n");
    scanf("%d %d",&iValue1,&iValue2);

    Pattern(iValue1, iValue2);

    return 0;
}
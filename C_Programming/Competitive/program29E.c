///////////////////////////////////////////////////////////////////
//
// Accept division of student from user and depends on the division
// display exam timing. There are 4 divisions in school as A,B,C,D. Exam
// of division A at 7 AM, B at 8.30 AM, C at 9.20 AM and D at 10.30 AM.
// (Application should be case insensitive)
// Input : C
// Output : Your exam at 9.20 AM
// Input : d
// Output : Your exam at 10.30 AM
//
////////////////////////////////////////////////////////////////////
#include<stdio.h>

void DisplaySchedule(char ch)
{
    if((ch == 97) || (ch == 65))
    {
        printf("7 AM\n");
    }

    else if((ch == 98) || (ch == 66))
    {
        printf("8:30 AM\n");    
    }

    else if((ch == 99) || (ch == 67))
    {
        printf("9:20 AM\n");    
    }

    else if((ch == 100) || (ch == 68))
    {
        printf("10:30 AM\n");    
    }

    else
    {
        printf("please insert valid input\n");
    }
}

int main()
{
    char cValue = '\0';

    printf("Enter the character :\n");
    scanf("%c",&cValue);

    DisplaySchedule(cValue);

    return 0;
}

#include<stdio.h>

void DisplaySchedule(char chDiv)
{
    if(chDiv==97 ||chDiv==65)   //97=a,65=A
    {
        printf("Your exam at 7 AM");
    }
    else if(chDiv==98 ||chDiv==66) //98=b,66=B
    {
        printf("Your exam at 8:30 AM");
    }
    else if(chDiv==99||chDiv==67) //98=c,67=C
    {
        printf("Your exam at 9:30 AM");
    }
    else if(chDiv==100 ||chDiv==68) //100=d,68=D
    {
        printf("Your exam at 10:30 AM");
    }
}

int main()
{
    char cValue='\0';
     printf("Enter the Division:");
     scanf("%c",&cValue);

     DisplaySchedule(cValue);

     return 0;
}
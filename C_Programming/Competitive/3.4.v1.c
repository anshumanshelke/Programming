#include <stdio.h>
#include <ctype.h>

int main()
{
    char ch, result;

    printf("Input: ");
    scanf("%c", &ch);

    if (islower(ch))
    {
        result = toupper(ch);
    }
    else 
    {
        result = tolower(ch);
    }

    printf("Output: %c\n", result);
    
    return 0;
}

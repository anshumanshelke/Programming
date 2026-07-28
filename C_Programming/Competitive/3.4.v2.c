#include <stdio.h>

int main() {
    char ch;

    // Get input from user
    printf("Input: ");
    scanf("%c", &ch);

    // Convert lowercase to uppercase
    if (ch >= 'a' && ch <= 'z') {
        ch = ch - 32;
    }
    // Convert uppercase to lowercase
    else if (ch >= 'A' && ch <= 'Z') {
        ch = ch + 32;
    }

    // Output the result
    printf("Output: %c\n", ch);

    return 0;
}

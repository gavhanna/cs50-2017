#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    string input = GetString();
    
    printf("%c", toupper(input[0]));
    
    for (int i = 0, n = strlen(input); i < n; i++)
    {
        
        if (input[i] == ' ' && input[i + 1] != '\0')
        {
            printf("%c", toupper(input[i + 1]));
        }
    }
    printf("\n");
    
}
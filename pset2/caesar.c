#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    
    if (argc != 2)
    {
        printf("Try again, this time with a single integer as an argument...\n");
        return 1;
    }
    
    int key = atoi(argv[1]);
    
    string sentence = GetString();
    
    for (int i = 0; i < strlen(sentence); i++)
    {
        char inputLetter = sentence[i];
        if (isalpha(inputLetter))
        {
            if(isupper(inputLetter))
            {
                int result = ((key + (inputLetter - 65)) % 26) + 65;
                printf("%c", result);
            }
            if(islower(inputLetter))
            {
                int result = ((key + (inputLetter -97)) % 26) + 97;
                printf("%c", result);
            }
        }
        else 
        {
            printf("%c", sentence[i]);
        }
    }
    printf("\n");
    return 0;
}
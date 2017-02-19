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
    
    
    
    char caeser(int k, string s)
    {
        for (int i = 0; i < strlen(s); i++)
        {
        char inputLetter = s[i];
        if (isalpha(inputLetter))
        {
            if(isupper(inputLetter))
            {
                int result = ((k + (inputLetter - 65)) % 26) + 65;
                printf("%c", result);
                return result;
            }
            if(islower(inputLetter))
            {
                int result = ((k + (inputLetter -97)) % 26) + 97;
                printf("%c", result);
                return result;
            }
        }
        else 
        {
            printf("%c", s[i]);
        }
    }    
    }
    
    caeser(key, sentence);
    
    printf("\n");
    return 0;
}
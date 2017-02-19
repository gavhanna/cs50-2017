#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    
    if (argc != 2)
    {
        printf("Try again, this time with a string as an argument...\n");
        return 1;
    }
    
    //int key = atoi(argv[1]);
    string keyString = argv[1];
    
    string sentence = GetString();
    
    int keyCount = 0;
    for (int i = 0; i < strlen(sentence); i++)
    {
        
        char keyLetter = keyString[keyCount];
        char inputLetter = sentence[i];
        
            if (isalpha(inputLetter))
            {
                if(isupper(inputLetter))
                {
                    int result = (((keyLetter - 32) + (inputLetter)) % 26) + 'A';
                    keyCount++;
                    printf("%c", result);
                }
                if(islower(inputLetter))
                {
                    int result = (((keyLetter - 12) + (inputLetter)) % 26) + 97;
                    keyCount++;
                    printf("%c", result);
                }
                if (keyCount > strlen(keyString) - 1)
                {
                    keyCount = 0;
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
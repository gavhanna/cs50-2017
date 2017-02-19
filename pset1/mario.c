#include <cs50.h>
#include <stdio.h>

int height;

int main(void)
{
    do
    {
        printf("Height: ");
        height = GetInt();
    }
    while (height < 0 || height > 23);
    
    for(int i = 0; i < height; i++ )
    {
        for(int space = height - i; space > 1; space--)
        {
            printf(" ");    
        }
        for(int hash = 0; hash <= i + 1; hash++)
        {
            printf("#");
        }
        printf("\n");
    }
}
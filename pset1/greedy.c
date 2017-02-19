#include <cs50.h>
#include <stdio.h>
#include <math.h>

float change;
int counter;

int main(void)
{
    do
    {
        printf("O hai! How much change is owed? ");
        change = round(GetFloat() * 100);
        counter = 0;
    } while (change <= 0);
    
    
    do
    {
        if (change >= 25)
        {
            change -= 25;
            counter++;
        } else if (change >= 10)
        {
            change -= 10;
            counter++;
        } else if (change >= 5)
        {
            change -= 5;
            counter++;
        } else if (change >= 1)
        {
            change -= 1;
            counter++;
        }
    }
    
    while (change > 0);
    
    printf("%i\n", counter);
}
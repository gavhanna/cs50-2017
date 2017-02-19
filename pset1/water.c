#include <cs50.h>
#include <stdio.h>

void CalculateWaterUsage(int mins);

int main(void)
{
    printf("minutes: ");
    int i = GetInt();
    CalculateWaterUsage(i);
}

void CalculateWaterUsage(int mins)
{
    printf("Bottles: %i\n", mins * 12);   
}

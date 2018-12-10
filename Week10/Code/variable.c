#include <stdio.h>


int main (void)
{
    int x=1; // Reserve space in memory for an integer x
    float y=2.03; // Can declare variables anywhere
    float z=0;

    z = x + y;

    printf("The value of z: %f\n", z); // Pass value of x to placeholder
    
    return 0;
}
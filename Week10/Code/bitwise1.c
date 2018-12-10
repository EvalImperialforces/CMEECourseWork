#include <stdio.h>

int main (void)
{
    signed char c1 = -1;
    unsigned char c2 = 0b000111; // This allows us to write in binary but not portable (will throw an error on some os's)
    signed char c3 = 0b1000111;
    
    c2 = c2 << 8;

    printf("c2 is now: %c\n", (unsigned int)c2); // Passing c2 as unsigned integer 

    return 0;

}
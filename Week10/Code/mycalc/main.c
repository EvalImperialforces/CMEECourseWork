#include <stdio.h>
#include "calc.h" // Include header file

float multiply_floats(float, float); // Must call function beforehand

int main (void)
{
    float x = 0.0;
    float y = 0.0;
    float c = 0.0;

    x = 7.2;
    y = 2.0;

    // c = x * y; // Could use this but safer to do in a function!!!!
    c = multiply_floats(x, y);

    c = multiply_floats(x, _PI_);

    return 0;
}
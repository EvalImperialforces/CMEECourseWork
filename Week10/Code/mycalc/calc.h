#ifndef _CALC_H_
#define _CALC_H_ // Header guard

#include "calc.h"

#define _PI_ 3.151592654

#ifdef DEBUG
#include <stdio.h>
#endif

#define destroy_intarray(x) _destroY_intarrat(x); x = NULL;


float add_floats(float a, float b);
float subtract_floats(float a, float b);
float multiply_floats(float a, float b);
float divide_floats(float a, float b);

#endif 

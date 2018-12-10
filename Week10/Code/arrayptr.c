#include <stdio.h>
#include <stdlib.h>

// Passing pointers to function

void print_intarray(int intarraylen, int* intarray)
{
    int i = 0;
    for(i = 0; i < intarraylen; ++i){
        printf("%i ", intarray[i]); // Space in outout
    }

printf("\n");
return;

}



int main (void)
{
    int intarray[] = {41, 22, 33};
    int* intptr = NULL;

    intptr = &intarray[0];

    printf("Array position 0 by indirection: %i\n", *intptr);

    print_intarray(3, intarray);
    print_intarray(3, intptr);

    return 0;
}
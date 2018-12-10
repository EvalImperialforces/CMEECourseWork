#include <stdio.h>
#include<stdlib.h>

int main (void)
{
    int index = 0;
    int* index_ptr = NULL; // Always null initialize a pointer

    // Assigning to pointer
    index_ptr = &index;

    printf("The value of index: %i\n", index);
    printf(" The value of index by indirection (through pointer): %i\n", *index_ptr);

    *index_ptr = 71;

    printf("The value of index: %i\n", index);
    printf(" The value of index by indirection (through pointer): %i\n", *index_ptr);


    int x = 3;
    int y = 7;

    int* intptr1 = &x;
    int* intptr2 = &y;

    int z;

    z = *intptr1 * *intptr2;

    return 0;
}
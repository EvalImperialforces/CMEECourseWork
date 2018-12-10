#include <stdio.h>
#include <stdlib.h>

typedef struct safe_intarray{ //Assigning type safe_intarray
    int* intdata; // Not initializing pointer beause structure acts as a holder, initialize in function
    int nelems;
} safe_intarray;

//void set_int_data(struct*intsarray, int index){}

int get_int_data(struct safe_intarray* sarray, int index) // Sarray is name of pointer within this function - only applicable within this scope
{
    int result = 0;
    if (index < (*sarray).nelems){ // Dereference structure and .nelems uses meber operator to get length of nelems
        result = (*sarray).intdata[index]; // Index is argument to give
      // or result = sarray -> intdata[index]; 
    }
    else{
        printf("Error: subscript out of bounds\n");
} 

    return result;
}


int main (void)
{
    struct safe_intarray a1; // Giving struct tenporary name a1 in main

    int nelems = 10; // Local copy

    a1.intdata = (int*)calloc(nelems, sizeof(int)); // Allocate memory for size of nelems
    a1.nelems = nelems; // Assign to nelems in structure

    //a1.intdata[0] = 2;
    //printf("THe first value in the array is %i\n", a1.intdata[0]);

    a1.intdata[1] = 2; // Setting 2nd element in array 2

    printf("Attempt to read out of bounds %i\n", get_int_data(&a1, 17)); // Dereference structure
    printf("Attempt to read within of bounds %i\n", get_int_data(&a1, 1));


    return 0;
}
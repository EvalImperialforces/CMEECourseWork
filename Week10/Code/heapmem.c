#include <stdio.h>
#include <stdlib.h>

void print_intarray(int* array, int nelems)
{
    int i = 0;
    for (i = 0; i < nelems; ++i){
        printf("%i ", array[i]);
    }
    printf("\n");
}

void destroy_intarray(int** intarray) // Don't call this (in any other function)
{   
    if (*intarray){
       free(*intarray);
       *intarray = NULL; 
    }
}


int* make_intarray(int numelements) // int* means function to return a pointer
{
    int* intarray; // Create space for intarray of size numelements

    // void* malloc (size_t sizeofmemory)
    intarray = (int*)malloc(numelements * sizeof(int));
    // void* calloc (size_t nelems, size_t sizeofeach)
    if (intarray == NULL){
        printf(" Error unable to allocate sufficient memory at line %i\n", __LINE__);
        exit(EXIT_FAILURE);
    }

    print_intarray(intarray, numelements);
    return intarray;
}


int main (void)
{   
    int numsites = 10;
    int *sitedata = NULL; // Treat as array of integer data
    // Don't know the size of array at runtime so make it a pointer
    // As soon as you declare pointer set to NULL

    sitedata = make_intarray(numsites);
    print_intarray(sitedata, numsites);
    destroy_intarray(&sitedata);
    destroy_intarray(&sitedata);

    return 0;
}
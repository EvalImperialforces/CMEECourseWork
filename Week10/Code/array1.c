#include <stdio.h>

int main (void)
{
    int intarray[5] = {0};
    int implarray[] = {1,2,3,4,5,6,7}; // 6 elements

    int i = 0;
    int x = 0;

     for (i = 0; i < 5; ++i){ // Uninitialized array will give you rubbish
        x = intarray[i];
        printf("Value at intarray[%i] is: %i\n", i, x);
    }

    for (i = 0; i < 6; ++i){ // You can index outside this array but it will also give you rubbish if you do
        x = implarray[i];
        printf("Value at implarray[%i] is: %i\n", i, x);
    }

     for (i = 0; i < 5; ++i){ // Putting info into array
        intarray[i] = i + 1;
        printf("Value at intarray[%i] is: %i\n", i, x);
    }

    int joinedarray[5 + 6];
    
    for(i = 0; i < (5 + 6); ++i){ // Be careful of indexing (being a number out) when joining array
        if (i < 5){
        joinedarray[i] = intarray[i];
        }
        
        joinedarray[i + 5] = implarray[i];

    }

    for(i = 0; i < (5 + 6); ++i){ // Have to print joined array element by element
        printf("%i", joinedarray[i]);        
    }
    printf("\n");

    return 0;

}
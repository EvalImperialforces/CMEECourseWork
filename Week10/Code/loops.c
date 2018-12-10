#include <stdio.h>
#include <stdbool.h>

int main (void)
{
    // The while loop
    int i = 0;
    while (i < 10 && i){ // i in brackets same as i != 0

        printf("loop iteration %i\n", i);
        ++i; // Increment i

    }

    i = 0;

    do{
        printf("do-while loop iteration %i\n", i);
        ++i; // Increment i
    } while(i<10 && i!=0);


    for (i = 0 ; i < 10; i++ ){ // initial i ; i condition ; operation for i
        printf("for loop iteration %i\n", i);
    }

    return 0;
}
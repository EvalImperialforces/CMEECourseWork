#include <stdio.h>

int main (void){

    char c1 = 'a';
    char c2 = 'c';
    int case_offset;

        case_offset = c1 - c2;

        printf("case_offset evaluates to: %i\n", (int)case_offset); 
        // Type cast operator with (int) before case_offset
        // Not needed though as case_offset is made as int on line 7

    int bigint = 476382974;
        char c3;

        c3 = bigint;
        printf("bigint: %i\n", bigint);
        bigint = c3;
        printf("bigint: %i\n", bigint);


    return 0;
}
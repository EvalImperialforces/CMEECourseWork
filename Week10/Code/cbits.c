#include <stdio.h>
#include "cbits/cbits.h"

int main (void) 
{
    CBit a = newCBit(200);
    CBit b = newCBit(200);
    CBit c = newCBit(200);

    CBitSet(71,a);
    CBitSet(14,a);

    CBitSet(72,b);
    CBitSet(44,b);

    if(CBitAND(NULL, a, b)){
        printf("Bitwise AND returns TRUE\n");
    } else {
        printf("Bitwise AND returns FALSE\n");
    }

    return 0;
}

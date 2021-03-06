#include <stdio.h>
#include <stdlib.h>

typedef struct link {
    int index;
    struct link* next;
    struct link* back;
} link;

void traverse_list(link* s)
{
    printf("Visiting link %i\n", s->index);
    if(s->next != NULL){
        traverse_list(s->next); // If not NULL, function calls itself to loop on next link
    }
}

int main (void)
{
    link l1;
    link l2;
    link l3;

    l1.index = 0;
    l1.next = &l2;

    l2.index = 1;
    l2.next = &l3;

    l3.index = 2;
    l3.next  = NULL;

    traverse_list(&l1);
}
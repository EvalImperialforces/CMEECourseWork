// Analogue of safearray - heapmem.c
struct node {
    struct node* left_desc;
    struct node* right_desc;
    struct node* ancestor;
};

struct polynode{
    struct polynode** descendents; // 100 descendents per node, not good practice to hard code - if you need more than 100 nodes
    // Need a dynamic memory of arbitrary size == Calloc or Malloc!!!!
    // Need a pointer to a pointer
    // Pointers stored as array of pointers
    struct polynode* ancestor;
    int n_descendents;
};

void traverse_polynode(struct polynode* n)
{
    int i = 0;
    for (i = 0; i < n->n_descendents; ++i){
        if (n -> descendents[i] != NULL){
            traverse_polynode(n->descendents[i]);
        }
    }
}

void traverse_tree(struct node* n)
{
     if(n->left_desc != NULL){
        traverse_tree(n->left_desc);
    }
}
    if(n->right_desc != NULL){
        traverse_tree(n->right_desc);
    }
}


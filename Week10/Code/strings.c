#include <stdio.h>

int main (void)
{
    char mystring1[] = "This is a string\n";
    char lstring[] = {'A', ' ', 's', 't','r','i','n','g','\0'};
    char five[] = "five"; // 5 characters in this string including the hidden '\0'

    int i = 0;
    for(i = 0; mystring1[i]; ++i){
        printf("%c",mystring1[i]);
    }

    return 0;
}
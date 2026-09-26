#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Ask for a name to the user
    string name = get_string("Write your name:");
    printf("hello, %s\n", name);
}
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    //Pedir al usuario la altura
    do
    {
        n = get_int("Height:");
    }
    while (n < 1 || n > 8);
    //Recorrer cada fila
    for (int i = 0; i < n; i++)
    {
        //Recorrer cada columna imprimiendo espacios
        for (int z = n - i; z > 1; z--)
        {
            printf(" ");
        }
        //Recorrer cada columna imprimiendo hashtags
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
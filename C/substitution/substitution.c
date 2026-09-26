#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int check_key(string key);

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        if (strlen(argv[1]) == 26 && check_key(argv[1]) == 0)
        {
            //Empieza el programa tras verificar que la key es valida
            string plaintext = get_string("Plaintext:\n");
            printf("ciphertext:");

            //Bucle for para recorrer el plaintext y cifrarlo
            for (int i = 0; i < strlen(plaintext); i++)
            {
                if (islower(plaintext[i]))
                {
                    printf("%c", tolower(argv[1][plaintext[i] - 97]));
                }
                else if (isupper(plaintext[i]))
                {
                    printf("%c", toupper(argv[1][plaintext[i] - 65]));
                }
                else
                {
                    printf("%c", plaintext[i]);
                }
            }
            printf("\n");
            return 0;
        }
        else
        {
            return 1;
        }
    }
    return 1;
}


//Funcion que devuelve 0 si se trata de una key valida
int check_key(string key)
{
    int m = 0;
    for (int i = 1; i < strlen(key); i++)
    {
        for (int j = 0; j < i; j++)
        {
            if ((toupper(key[i]) == toupper(key[j])) || isdigit(key[i]))
            {
                m++;
            }
        }
    }
    return m;
}


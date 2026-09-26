// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

int counter = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int value = hash(word);
    node *pointer = table[value];
    while(pointer != 0)
    {
        if(strcasecmp(pointer->word, word) == 0)
        {
            return true;
        }
        pointer = pointer->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int value = 0;
    for(int i = 0; i < strlen(word); i++)
    {
        value = value + toupper(word[i]);
    }
    return value % 100;
}


// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        printf("ERROR\n");
        return false;
    }
    char word[LENGTH+1];
    while(fscanf(file, "%s", word) != EOF)
    {
         //Hacer hueco en memoria para un nodo
         node *w = malloc(sizeof(node));
         if(w == NULL)
         {
            return false;
         }
         strcpy(w->word, word);
         counter++;
         w->next = table[hash(word)];
         table[hash(word)] = w;
    }
    fclose(file);
    return true;
}


// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if(counter > 0)
    {
        return counter;
    }
    else
    {
        return 0;
    }
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for( int i = 0; i < N; i++)
    {
        node *fpointer = table[i];
        while(fpointer != NULL)
        {
            //Creamos un puntero temporal para no perder la direccion
            node *tmp = fpointer;
            fpointer = fpointer -> next;
            //Liberamos la direccion cuando ya tenemos guardada la siguiente
            free(tmp);
        }
        if(fpointer == NULL)
        {
            return true;
        }
    }
    return false;
}




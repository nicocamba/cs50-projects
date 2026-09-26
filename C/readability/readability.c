#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string text);

int count_words(string text);

int count_sentences(string text);

int main(void)
{
    string text = get_string("Text:");
    float j = count_words(text);
    float k = 0.0588 * count_letters(text) * 100 / j - 0.296 * count_sentences(text) * 100 / j - 15.8;
    if(k < 1)
    {
        printf("Before Grade 1\n");
    }
    else if(k > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        int b = round(k);
        printf("Grade %i\n", b);
    }
}
int count_letters(string text)
{
    int n =  strlen(text);
    int m = 0;
    for(int i = 0; i < n; i++)
    {
        if(isalpha(text[i]))
        {
            m++;
        }

    }
    return m;
}
int count_words(string text)
{
    int n =  strlen(text);
    int m = 1;
    for(int i = 0; i < n; i++)
    {
        if(text[i] == 32)
        {
            m++;
        }

    }
    return m;
}
int count_sentences(string text)
{
    int n =  strlen(text);
    int m = 0;
    for(int i = 0; i < n; i++)
    {
        if(text[i] == 33 || text[i] == 46 || text[i] == 63)
        {
            m++;
        }

    }
    return m;
}

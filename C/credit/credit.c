#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long card = get_long("Card Number:\n");
    if (card >= 340000000000000 && card < 380000000000000)
    {
        printf("AMEX\n");
    }
    else if (card >= 5100000000000000 && card < 5600000000000000)
    {
        printf("MASTERCARD\n");
    }
    else if ((card >= 4000000000000000 && card < 5000000000000000)||(card >= 4000000000000 && card < 5000000000000))
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if(argc == 2)
    {
        FILE *file = fopen(argv[1], "r");
        if(file == NULL)
        {
            printf("Error\n");
            return 1;
        }
        unsigned char bloques[512];
        int n = 0;
        FILE *file2 = NULL;
        char *p = malloc(8 * sizeof(char));
        while (fread(bloques, sizeof(char), 512, file))
        {
            if(bloques[0] == 0xff && bloques[1] == 0xd8 && bloques[2] == 0xff && (bloques[3] == 0xe0 || bloques[3] == 0xe1 || bloques[3] == 0xe2 || bloques[3] == 0xe3 || bloques[3] == 0xe4 || bloques[3] == 0xe5 || bloques[3] == 0xe6 || bloques[3] == 0xe7 || bloques[3] == 0xe8 || bloques[3] == 0xe9 || bloques[3] == 0xea || bloques[3] == 0xeb || bloques[3] == 0xec || bloques[3] == 0xed || bloques[3] == 0xee || bloques[3] == 0xef ))
            {
                sprintf(p, "%03i.jpg", n);
                n++;
                file2 = fopen(p,"w");
            }
            if(file2 != NULL)
            {
                fwrite(bloques, sizeof(char), 512, file2);
            }
        }
        free(p);
        fclose(file);
        fclose(file2);
        return 0;
    }
    else
    {
        printf("Only one argument, i.e, ./recover IMAGE\n");
        return 1;
    }
}
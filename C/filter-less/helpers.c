#include "helpers.h"
#include <math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            int gray = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = gray;
            image[i][j].rgbtRed = gray;
            image[i][j].rgbtGreen = gray;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue = image[i][j].rgbtBlue;
            int sepiaRed = round(0.393 * originalRed + 0.769 * originalGreen + 0.189 * originalBlue);
            int sepiaGreen = round(0.349 * originalRed + 0.686 * originalGreen + 0.168 * originalBlue);
            int sepiaBlue = round(0.272 * originalRed + 0.534 * originalGreen + 0.131 * originalBlue);

            if(sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if(sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            if(sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width / 2; j++)
        {
            int leftRed = image[i][j].rgbtRed;
            int leftGreen = image[i][j].rgbtGreen;
            int leftBlue = image[i][j].rgbtBlue;
            int rightRed = image[i][width - 1 - j].rgbtRed;
            int rightGreen = image[i][width - 1 - j].rgbtGreen;
            int rightBlue = image[i][width - 1 - j].rgbtBlue;
            image[i][j].rgbtRed = rightRed;
            image[i][j].rgbtGreen = rightGreen;
            image[i][j].rgbtBlue = rightBlue;
            image[i][width - 1 - j].rgbtRed = leftRed;
            image[i][width - 1 - j].rgbtGreen = leftGreen;
            image[i][width - 1 - j].rgbtBlue = leftBlue;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE output_image[height][width];
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < height; j++)
        {
            if(i == 0 && j == 0)
            {
                output_image[i][j].rgbtRed = round((image[i][j].rgbtRed + image[i+1][j].rgbtRed + image[i][j+1].rgbtRed + image[i+1][j+1].rgbtRed) / 4.0);
                output_image[i][j].rgbtBlue = round((image[i][j].rgbtBlue + image[i+1][j].rgbtBlue + image[i][j+1].rgbtBlue + image[i+1][j+1].rgbtBlue) / 4.0);
                output_image[i][j].rgbtGreen = round((image[i][j].rgbtGreen + image[i+1][j].rgbtGreen + image[i][j+1].rgbtGreen + image[i+1][j+1].rgbtGreen) / 4.0);
            }
            else if(i == 0 && j == width - 1)
            {
                output_image[i][j].rgbtRed = round((image[i][j].rgbtRed + image[i+1][j].rgbtRed + image[i][j-1].rgbtRed + image[i+1][j-1].rgbtRed) / 4.0);
                output_image[i][j].rgbtBlue = round((image[i][j].rgbtBlue + image[i+1][j].rgbtBlue + image[i][j-1].rgbtBlue + image[i+1][j-1].rgbtBlue) / 4.0);
                output_image[i][j].rgbtGreen = round((image[i][j].rgbtGreen + image[i+1][j].rgbtGreen + image[i][j-1].rgbtGreen + image[i+1][j-1].rgbtGreen) / 4.0);
            }
            else if(i == height - 1 && j == 0)
            {
                output_image[i][j].rgbtRed = round((image[i][j].rgbtRed + image[i-1][j].rgbtRed + image[i][j+1].rgbtRed + image[i-1][j+1].rgbtRed) / 4.0);
                output_image[i][j].rgbtBlue = round((image[i][j].rgbtBlue + image[i-1][j].rgbtBlue + image[i][j+1].rgbtBlue + image[i-1][j+1].rgbtBlue) / 4.0);
                output_image[i][j].rgbtGreen = round((image[i][j].rgbtGreen + image[i-1][j].rgbtGreen + image[i][j+1].rgbtGreen + image[i-1][j+1].rgbtGreen) / 4.0);
            }
            else if(i == height - 1 && width - 1 == j)
            {
                output_image[i][j].rgbtRed = round((image[i][j].rgbtRed + image[i-1][j].rgbtRed + image[i][j-1].rgbtRed + image[i-1][j-1].rgbtRed) / 4.0);
                output_image[i][j].rgbtBlue = round((image[i][j].rgbtBlue + image[i-1][j].rgbtBlue + image[i][j-1].rgbtBlue + image[i-1][j-1].rgbtBlue) / 4.0);
                output_image[i][j].rgbtGreen = round((image[i][j].rgbtGreen + image[i-1][j].rgbtGreen + image[i][j-1].rgbtGreen + image[i-1][j-1].rgbtGreen) / 4.0);
            }
            else if(i == 0 && j > 0 && j < width - 1)
            {
                output_image[i][j].rgbtRed = round((image[i][j].rgbtRed + image[i+1][j].rgbtRed + image[i][j-1].rgbtRed + image[i+1][j-1].rgbtRed + image[i][j+1].rgbtRed + image[i+1][j+1].rgbtRed) / 6.0);
                output_image[i][j].rgbtBlue = round((image[i][j].rgbtBlue + image[i+1][j].rgbtBlue + image[i][j-1].rgbtBlue + image[i+1][j-1].rgbtBlue + image[i][j+1].rgbtBlue + image[i+1][j+1].rgbtBlue) / 6.0);
                output_image[i][j].rgbtGreen = round((image[i][j].rgbtGreen + image[i+1][j].rgbtGreen + image[i][j-1].rgbtGreen + image[i+1][j-1].rgbtGreen + image[i][j+1].rgbtGreen + image[i+1][j+1].rgbtGreen) / 6.0);
            }
            else if(i == height - 1 && j > 0 && j < width - 1)
            {
                output_image[i][j].rgbtRed = round((image[i][j].rgbtRed + image[i-1][j].rgbtRed + image[i][j-1].rgbtRed + image[i-1][j-1].rgbtRed + image[i][j+1].rgbtRed + image[i-1][j+1].rgbtRed) / 6.0);
                output_image[i][j].rgbtBlue = round((image[i][j].rgbtBlue + image[i-1][j].rgbtBlue + image[i][j-1].rgbtBlue + image[i-1][j-1].rgbtBlue + image[i][j+1].rgbtBlue + image[i-1][j+1].rgbtBlue) / 6.0);
                output_image[i][j].rgbtGreen = round((image[i][j].rgbtGreen + image[i-1][j].rgbtGreen + image[i][j-1].rgbtGreen + image[i-1][j-1].rgbtGreen + image[i][j+1].rgbtGreen + image[i-1][j+1].rgbtGreen) / 6.0);
            }
            else if(i > 0 && i < height - 1 && j == 0)
            {
                output_image[i][j].rgbtRed = round((image[i][j].rgbtRed + image[i][j+1].rgbtRed + image[i-1][j].rgbtRed + image[i-1][j+1].rgbtRed + image[i+1][j].rgbtRed + image[i+1][j+1].rgbtRed) / 6.0);
                output_image[i][j].rgbtBlue = round((image[i][j].rgbtBlue + image[i][j+1].rgbtBlue + image[i-1][j].rgbtBlue + image[i-1][j+1].rgbtBlue + image[i+1][j].rgbtBlue + image[i+1][j+1].rgbtBlue) / 6.0);
                output_image[i][j].rgbtGreen = round((image[i][j].rgbtGreen + image[i][j+1].rgbtGreen + image[i-1][j].rgbtGreen + image[i-1][j+1].rgbtGreen + image[i+1][j].rgbtGreen + image[i+1][j+1].rgbtGreen) / 6.0);
            }
            else if(i > 0 && i < height - 1 && j == width - 1)
            {
                output_image[i][j].rgbtRed = round((image[i][j].rgbtRed + image[i][j-1].rgbtRed + image[i-1][j].rgbtRed + image[i-1][j-1].rgbtRed + image[i+1][j].rgbtRed + image[i+1][j-1].rgbtRed) / 6.0);
                output_image[i][j].rgbtBlue = round((image[i][j].rgbtBlue + image[i][j-1].rgbtBlue + image[i-1][j].rgbtBlue + image[i-1][j-1].rgbtBlue + image[i+1][j].rgbtBlue + image[i+1][j-1].rgbtBlue) / 6.0);
                output_image[i][j].rgbtGreen = round((image[i][j].rgbtGreen + image[i][j-1].rgbtGreen + image[i-1][j].rgbtGreen + image[i-1][j-1].rgbtGreen + image[i+1][j].rgbtGreen + image[i+1][j-1].rgbtGreen) / 6.0);
            }
            else if(i > 0 && j > 0 && i < height - 1 && j < width - 1)
            {
                output_image[i][j].rgbtRed = round((image[i][j].rgbtRed + image[i][j-1].rgbtRed + image[i-1][j].rgbtRed + image[i-1][j-1].rgbtRed + image[i+1][j].rgbtRed + image[i+1][j-1].rgbtRed + image[i+1][j+1].rgbtRed + image[i][j+1].rgbtRed + image[i-1][j+1].rgbtRed) / 9.0);
                output_image[i][j].rgbtBlue = round((image[i][j].rgbtBlue + image[i][j-1].rgbtBlue + image[i-1][j].rgbtBlue + image[i-1][j-1].rgbtBlue + image[i+1][j].rgbtBlue + image[i+1][j-1].rgbtBlue + image[i+1][j+1].rgbtBlue + image[i][j+1].rgbtBlue + image[i-1][j+1].rgbtBlue) / 9.0);
                output_image[i][j].rgbtGreen = round((image[i][j].rgbtGreen + image[i][j-1].rgbtGreen + image[i-1][j].rgbtGreen + image[i-1][j-1].rgbtGreen + image[i+1][j].rgbtGreen + image[i+1][j-1].rgbtGreen + image[i+1][j+1].rgbtGreen + image[i][j+1].rgbtGreen + image[i-1][j+1].rgbtGreen) / 9.0);
            }
        }
    }
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = output_image[i][j].rgbtRed;
            image[i][j].rgbtBlue = output_image[i][j].rgbtBlue;
            image[i][j].rgbtGreen = output_image[i][j].rgbtGreen;
        }
    }
}
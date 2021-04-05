#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <string.h>



void ifft(double complex *x, int n)
{
    if (n == 1)
        return;

    double complex *odd = malloc(n / 2 * sizeof(double complex));
    double complex *even = malloc(n / 2 * sizeof(double complex));
    for (int i = 0; 2 * i < n; i++)
    {
        even[i] = x[2 * i];
        odd[i] = x[2 * i + 1];
    }

    ifft(even, n / 2);
    ifft(odd, n / 2);

    double complex w;
    for (int i = 0; 2 * i < n; i++)
    {
        w = CMPLX(cos(-2 * M_PI * i / n), sin(-2 * M_PI * i / n));
        x[i] = even[i] + w * odd[i];
        x[i + n / 2] = even[i] - w * odd[i];
    }
    free(even);
    free(odd);
}


int main()
{
    int n = (1 << 20);
    double *x = (double *)malloc(n * sizeof(double));
    double *h = (double *)malloc(n * sizeof(double));

    double complex *X = (double complex *)malloc(n * sizeof(double complex));
    double complex *H = (double complex *)malloc(n * sizeof(double complex));
    double complex *Y = (double complex *)malloc(n * sizeof(double complex));
    double complex *ifft_Y = (double complex *)malloc(n * sizeof(double complex));

    FILE *fin1, *fin2, *fout ;


// #####################

    fin1 = fopen("fft_x.dat", "r");
    int count = 0;
    while (!feof(fin1) && count < n)
    {
        fscanf(fin1, "%lf", &(x[count]));
        X[count] = CMPLX(x[count], 0);
        count++;
    }

    fin2 = fopen("fft_h.dat", "r");
    count = 0;
    while (!feof(fin2) && count < n)
    {
        fscanf(fin2, "%lf", &(h[count]));
        H[count] = CMPLX(h[count], 0);
        count++;
    }


    for (int i = 0; i < n; i++)
    {
        Y[i] = H[i] * X[i];
        ifft_Y[i] = Y[i];
    }

    ifft(ifft_Y, n);
    fout = fopen("ifft_y.dat", "w");
    for (int i = 0; i < n; i++)
    {
        fprintf(fout, "%lf \n", creal(ifft_Y[i] / n));
    }

    fclose(fin1);
    fclose(fin2);
    fclose(fout);
    return 0;


}

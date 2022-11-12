#include <stdio.h>
#include "iostream"
#include "include/mpi.h"
#include "windows.h"

using namespace std;

int main(int argc, char *argv[])
{
    int rank;
    int size;
    int n, i, j;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    if (rank == 0)
    {
        scanf("%d", &n);
    }
    MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);
    int **a = new int *[n];
    a[0] = new int[n * n];
    for (i = 1; i < n; i++)
    {
        a[i] = a[i - 1] + n;
    }
    if (rank == 0)
    {
        for (i = 0; i < n; i++)
        {
            for (j = 0; j < n; j++)
            {
                a[i][j] = i;
            }
        }

        
    }

    int *w = new int[size];
    int a1 = n / size;
    int b1 = n % size;
    for (i = 0; i < b1; i++)
    {
        w[i] = a1 + 1;
    }
    for (i = 0; i < size - b1; i++)
    {
        w[i + b1] = a1;
    }
    

    for (i = 0; i < size; i++)
    {
        if (rank == i)
        {
            int **b = new int *[w[i]];
            b[0] = new int[w[i] * n];
            for (j = 1; j < w[i]; j++)
            {
                b[j] = b[j - 1] + n;
            }
            int *RC = new int[size];
            int *ds = new int[size];
            for (int j = 0; j < size; j++)
            {
                RC[j] = n * w[j];
            }
            ds[0] = 0;
            for (int j = 1; j < size; j++)
            {
                ds[j] = n * w[j - 1] + ds[j - 1];
            }
            MPI_Scatterv(*a, RC, ds, MPI_INT, *b, w[i] * n, MPI_INT, 0, MPI_COMM_WORLD);
            printf("rank= %d b: \n", rank);
            for (int k = 0; k < w[i]; k++)
            {
                for (j = 0; j < n; j++)
                {
                    printf(" %d ", b[k][j]);
                }
                printf("\n");
            }
        }
    }

    MPI_Finalize();
    return 0;
}

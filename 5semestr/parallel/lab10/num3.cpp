#include <stdio.h>
#include "iostream"
#include "include/mpi.h"
#include "windows.h"

using namespace std;

int main(int argc, char *argv[])
{
    int rank;
    int size;
    int i, j, s = 0;
    int n;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    n = 2;

    MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);

    int **a = new int *[size * 2];
    a[0] = new int[size * n * 2];
    for (int i = 1; i < size * 2; i++)
    {
        a[i] = a[i - 1] + n;
    }
    if (rank == 0)
    {
        for (i = 0; i < size * 2; i++)
        {
            for (int j = 0; j < n; j++)
            {
                a[i][j] = i;
            }
        }
    }
    int **b = new int *[2];
    b[0] = new int[2 * n];
    for (int i = 1; i < 2; i++)
    {
        b[i] = b[i - 1] + n;
    }

    int *sc = new int[size];
    int *ds = new int[size];

    for (int i = 0; i < size; i++)
    {
        sc[i] = i + 1;
        ds[i] = (i * (i + 1)) / 2;
    }

    MPI_Scatter(*a, 2 * n, MPI_INT, *b, 2 * n, MPI_INT, 0, MPI_COMM_WORLD);

    Sleep(rank);

    printf("rank= %d a: \n", rank);
    for (i = 0; i < 2; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf(" %d ", b[i][j]);
        }
        printf("\n");

    }
    printf("\n");
    MPI_Finalize();

    delete[] b;
    delete[] a;
    delete[] sc;
    delete[] ds;

    return 0;
}
